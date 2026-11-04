"""sources.yml의 블로그들을 확인해 지난번 이후 새로 올라온 글을 모은다.

- 처음 보는 블로그는 현재 글 목록을 기록만 하고 새 글로 치지 않는다.
- 결과는 state/seen.json에 저장하고, 새 글이 있으면 이슈 본문을 만든다.

사용법: python scripts/check_new_posts.py --body issue.md
새 글 개수는 표준 출력 마지막 줄에 `new_count=N`으로 남긴다.
"""

import argparse
import calendar
import concurrent.futures as cf
import gzip
import json
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser
import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources.yml"
STATE = ROOT / "state" / "seen.json"

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0 Safari/537.36"
)
KST = timezone(timedelta(hours=9))
KEEP_PER_SOURCE = 500  # 블로그별로 기억해 둘 글 개수
MAX_AGE_DAYS = 7  # 날짜가 있는 글은 이보다 오래되면 새 글로 치지 않는다 (피드 주소·형식이 바뀐 경우 대비)
MAX_PER_SOURCE = 10  # 한 번에 한 블로그에서 보고할 최대 글 수


def fetch(url: str) -> tuple[str, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "ko,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        body = r.read()
        # 요청하지 않아도 gzip으로 보내는 서버가 있다 (예: DeepMind)
        if body[:2] == b"\x1f\x8b":
            body = gzip.decompress(body)
        return r.geturl(), body


def read_feed(src: dict) -> list[dict]:
    _, body = fetch(src["feed"])
    parsed = feedparser.parse(body)
    if not parsed.entries:
        raise RuntimeError("피드에 글이 없음")
    posts = []
    for e in parsed.entries:
        link = e.get("link") or ""
        pid = e.get("id") or link
        if not pid:
            continue
        ts = e.get("published_parsed") or e.get("updated_parsed")
        posts.append({
            "id": pid,
            "title": (e.get("title") or link).strip(),
            "link": link or pid,
            "ts": calendar.timegm(ts) if ts else None,
        })
    return posts


def read_page(src: dict) -> list[dict]:
    final, body = fetch(src["url"])
    html = body.decode("utf-8", "ignore")
    host = urllib.parse.urlparse(final).netloc
    pattern = re.compile(src["page_pattern"])
    titles: dict[str, str] = {}  # 페이지에 나온 순서를 유지한다
    for m in re.finditer(r'<a\b[^>]*?href=["\']([^"\'#?]+)[^>]*>(.*?)</a>', html, re.I | re.S):
        link = urllib.parse.urljoin(final, m.group(1)).rstrip("/")
        p = urllib.parse.urlparse(link)
        if p.netloc != host or not pattern.search(p.path + ("/" if m.group(1).endswith("/") else "")):
            continue
        text = re.sub(r"<[^>]+>", " ", m.group(2))
        text = re.sub(r"\s+", " ", text).strip()
        # 같은 글이 이미지·"Learn more"·제목 링크로 여러 번 나오면 가장 긴 글자를 제목으로 쓴다
        if len(text) > len(titles.get(link, "")):
            titles[link] = text[:120]
        titles.setdefault(link, "")
    if not titles:
        raise RuntimeError("페이지에서 글 링크를 찾지 못함")
    return [
        {"id": link, "title": t or urllib.parse.unquote(link.rsplit("/", 1)[-1]).replace("-", " "), "link": link, "ts": None}
        for link, t in titles.items()
    ]


def check(src: dict) -> list[dict]:
    reader = read_feed if "feed" in src else read_page
    try:
        return reader(src)
    except Exception:  # noqa: BLE001 - 큰 페이지(Mercari, PayPal)가 가끔 잘려 와서 한 번 더 시도한다
        time.sleep(5)
        return reader(src)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--body", required=True, help="이슈 본문을 쓸 파일")
    args = ap.parse_args()

    sections = yaml.safe_load(SOURCES.read_text(encoding="utf-8"))
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    sources = [(sec, s) for sec, items in sections.items() for s in items]

    with cf.ThreadPoolExecutor(16) as ex:
        futures = {ex.submit(check, s): (sec, s) for sec, s in sources}
        results = {}
        for f in cf.as_completed(futures):
            sec, s = futures[f]
            try:
                results[s["name"]] = f.result()
            except Exception as e:  # noqa: BLE001 - 한 곳이 실패해도 나머지는 계속 확인
                results[s["name"]] = e

    cutoff = time.time() - MAX_AGE_DAYS * 86400
    report: dict[str, list[tuple[str, list[dict]]]] = {sec: [] for sec in sections}
    failed, seeded = [], []
    shown_links = set()  # 여러 블로그에 같은 글이 걸린 경우(예: Meta와 Instagram) 한 번만 보여준다

    for sec, s in sources:
        name = s["name"]
        res = results[name]
        if isinstance(res, Exception):
            failed.append(f"{name} ({type(res).__name__}: {str(res)[:80]})")
            continue
        known = state.get(name)
        ids = [p["id"] for p in res]
        if known is None:
            seeded.append(name)
            state[name] = ids[:KEEP_PER_SOURCE]
            continue
        known_set = set(known)
        new = [p for p in res if p["id"] not in known_set and (p["ts"] is None or p["ts"] >= cutoff)]
        new = [p for p in new if p["link"] not in shown_links][:MAX_PER_SOURCE]
        shown_links.update(p["link"] for p in new)
        if new:
            report[sec].append((s, new))
        # 새로 본 글을 앞에 두고, 이전 기록을 이어 붙여 개수를 제한한다
        merged = ids + [i for i in known if i not in set(ids)]
        state[name] = merged[:KEEP_PER_SOURCE]

    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")

    new_count = sum(len(posts) for items in report.values() for _, posts in items)
    lines = []
    for sec, items in report.items():
        if not items:
            continue
        lines.append(f"## {sec}\n")
        for s, posts in items:
            lines.append(f"### {s['name']}")
            for p in posts:
                when = ""
                if p["ts"]:
                    when = " · " + datetime.fromtimestamp(p["ts"], KST).strftime("%m-%d")
                title = p["title"].replace("[", "\\[").replace("]", "\\]")
                lines.append(f"- [{title}]({p['link']}){when}")
            lines.append("")
    if seeded:
        lines.append(f"<sub>처음 등록되어 기준만 잡은 곳: {', '.join(seeded)}</sub>\n")
    if failed:
        lines.append("<details><summary>확인 실패 " + str(len(failed)) + "곳</summary>\n")
        lines.extend(f"- {f}" for f in failed)
        lines.append("\n</details>")
    Path(args.body).write_text("\n".join(lines) + "\n", encoding="utf-8")

    for f in failed:
        print(f"확인 실패: {f}")
    print(f"sources={len(sources)} failed={len(failed)} seeded={len(seeded)}")
    print(f"new_count={new_count}")


if __name__ == "__main__":
    main()
