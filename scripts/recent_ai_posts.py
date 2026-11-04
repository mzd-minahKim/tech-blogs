"""최근 N일 동안 올라온 AI 관련 글을 한 번에 모은다. (state/seen.json은 건드리지 않는다)

사용법: python scripts/recent_ai_posts.py --days 90 --out recent.md

- RSS는 피드에 남아 있는 글까지만 볼 수 있다. Medium 등은 최근 10개만 주므로 그보다 오래된 글은 빠질 수 있다.
- 목록 페이지 방식 블로그는 글마다 페이지를 열어 작성일(meta·JSON-LD)을 읽는다. 날짜를 못 찾은 글은 따로 모은다.
"""

import argparse
import concurrent.futures as cf
import re
import time
from datetime import datetime
from email.utils import parsedate_to_datetime
from pathlib import Path

import yaml

from check_new_posts import KST, SOURCES, check, fetch, is_ai, post_line

DATE_PATTERNS = [
    r'property=["\']article:published_time["\'][^>]*content=["\']([^"\']+)',
    r'content=["\']([^"\']+)["\'][^>]*property=["\']article:published_time',
    r'"datePublished"\s*:\s*"([^"]+)"',
    r'<time[^>]*datetime=["\']([^"\']+)',
]


def parse_date(s: str) -> float | None:
    s = s.strip()
    for fn in (lambda x: datetime.fromisoformat(x.replace("Z", "+00:00")), parsedate_to_datetime):
        try:
            d = fn(s)
            return (d if d.tzinfo else d.replace(tzinfo=KST)).timestamp()
        except Exception:  # noqa: BLE001
            pass
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s)
    return datetime(int(m[1]), int(m[2]), int(m[3]), tzinfo=KST).timestamp() if m else None


def page_date(link: str) -> float | None:
    try:
        _, body = fetch(link)
    except Exception:  # noqa: BLE001
        return None
    html = body.decode("utf-8", "ignore")
    for pat in DATE_PATTERNS:
        m = re.search(pat, html, re.I)
        if m and (ts := parse_date(m.group(1))):
            return ts
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=90)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    sections = yaml.safe_load(SOURCES.read_text(encoding="utf-8"))
    sources = [(sec, s) for sec, items in sections.items() for s in items]
    cutoff = time.time() - args.days * 86400

    with cf.ThreadPoolExecutor(16) as ex:
        fetched = dict(zip([s["name"] for _, s in sources], ex.map(lambda x: _safe(check, x[1]), sources)))

    # 날짜가 없는 글(목록 페이지 방식) 중 AI 글만 열어서 작성일을 채운다
    undated = [(sec, p) for sec, s in sources if isinstance(fetched[s["name"]], list)
               for p in fetched[s["name"]] if p["ts"] is None and is_ai(sec, p)]
    with cf.ThreadPoolExecutor(16) as ex:
        for (_, p), ts in zip(undated, ex.map(lambda x: page_date(x[1]["link"]), undated)):
            p["ts"] = ts

    report = {sec: [] for sec in sections}
    no_date, failed, seen_links = [], [], set()
    for sec, s in sources:
        res = fetched[s["name"]]
        if isinstance(res, Exception):
            failed.append(s["name"])
            continue
        posts = []
        for p in res:
            if p["link"] in seen_links or not is_ai(sec, p):
                continue
            seen_links.add(p["link"])
            if p["ts"] is None:
                no_date.append((s, p))
            elif p["ts"] >= cutoff:
                posts.append(p)
        if posts:
            posts.sort(key=lambda p: p["ts"], reverse=True)
            report[sec].append((s, posts))

    total = sum(len(ps) for items in report.values() for _, ps in items)
    since = datetime.fromtimestamp(cutoff, KST).strftime("%Y-%m-%d")
    today = datetime.now(KST).strftime("%Y-%m-%d")
    lines = [f"# AI 관련 글 모음 ({since} ~ {today})\n",
             f"총 {total}개, 블로그 {sum(len(v) for v in report.values())}곳. 블로그 이름을 누르면 글 목록이 펼쳐집니다.\n",
             "- 해외 AI 블로그는 모든 글을, 그 외 블로그는 제목에 AI 관련 키워드가 있는 글만 담았습니다.",
             "- RSS에 남아 있는 글까지만 볼 수 있어서, 최근 글만 주는 피드(Medium 등)는 오래된 글이 빠졌을 수 있습니다.\n"]
    for sec, items in report.items():
        if not items:
            continue
        lines.append(f"## {sec} ({sum(len(ps) for _, ps in items)}개)\n")
        for s, ps in sorted(items, key=lambda x: -len(x[1])):
            lines.append(f"<details><summary><b>{s['name']}</b> ({len(ps)}개)</summary>\n")
            lines.extend(f"- {post_line(p)}" for p in ps)
            lines.append("\n</details>\n")
    if no_date:
        lines.append(f"<details><summary>작성일을 확인하지 못한 AI 글 {len(no_date)}개</summary>\n")
        lines.extend(f"- {s['name']}: {post_line(p)}" for s, p in no_date)
        lines.append("\n</details>\n")
    if failed:
        lines.append(f"<sub>확인 실패: {', '.join(failed)}</sub>")
    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"total={total} no_date={len(no_date)} failed={len(failed)}")


def _safe(fn, *a):
    try:
        return fn(*a)
    except Exception as e:  # noqa: BLE001
        return e


if __name__ == "__main__":
    main()
