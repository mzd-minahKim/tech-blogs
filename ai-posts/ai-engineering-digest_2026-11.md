# AI 엔지니어링 글 요약: 공통 메시지와 먼저 읽을 글 (2026-08 ~ 2026-11)

[AI 엔지니어링 실무 글 모음](ai-engineering-picks_2026-08-06_2026-11-04.md) 140개 중 44개를 실제로 읽고, 세 곳 이상에서 반복된 메시지와 구체적인 글만 추렸습니다.

## 여러 글이 공통으로 말하는 것

### 1. 숫자·라우팅·형식 검사는 코드로, LLM은 해석만

프롬프트 하나에 다 맡기면 수치 오류와 누락이 생겼습니다. 잘 된 팀은 계산·후보 선정·라우팅·형식 검사를 결정적인 코드로 먼저 확정하고, LLM에는 해석과 판단만 남겼습니다.

- LINE: [숫자는 코드로 확정하고 탐색 범위는 그래프·호출 상한으로 제한](https://techblog.lycorp.co.jp/ko/ai-agent-ad-report-automation)
- Meta: [LLM이 추론하는 건 7단계 중 1단계, 3~4일 작업이 1시간 미만](https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/)
- 토스: [형식 규칙은 스킬이 아니라 CLI가 판정](https://toss.tech/article/dataops-log-definition-skill)
- Netflix: [LLM은 줄 번호 두 개만 고르고 본문은 원본 로그에서 복원](https://netflixtechblog.com/making-failure-diagnosis-reliable-with-pensive-ai-6b0811a1c015)

### 2. '하지 마'는 프롬프트가 아니라 구조로 막는다

CLAUDE.md나 프롬프트에 적은 규칙은 지켜지지 않을 때가 많습니다. 훅, 기본값, 권한 경로처럼 아예 그렇게 동작할 수 없게 만든 사례가 반복해서 나옵니다.

- Spotify: [큰 파일 읽기를 PreToolUse 훅으로 막아 싼 모델로 보냄](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90/)
- SK텔레콤 DEVOCEAN: [발행 도구는 confirm=true로 다시 불러야만 실행](http://devocean.sk.com/blog/techBoardDetail.do?id=168583&boardType=techBlog&isShared=Y)
- Uber: [새로 등록된 도구는 기본 비활성, 소유 팀이 승인해야 켜짐](https://www.uber.com/us/en/blog/designing-mcp-gateway)
- 우아한형제들: [View·Form·Store 경계를 린트·테스트로 강제](https://techblog.woowahan.com/27604/)

### 3. 비용은 단가가 아니라 캐시·라우팅·위임 구조에서 줄어든다

더 싼 모델로 바꾸는 것만으로는 오히려 비싸질 수 있습니다. 효과가 컸던 건 프롬프트 캐시 관리, 요청 난이도별 라우팅, 잡일을 싼 모델에 넘기는 위임이었고, 비교 기준은 '성공한 작업 1건당 비용'이었습니다.

- 당근마켓: [모델 교체 후 캐시 적중률 85.8%→2.3%, 요청당 비용 3.2배](https://medium.com/daangn/%EB%AA%A8%EB%8D%B8%EB%A7%8C-%EB%B0%94%EA%BF%A8%EB%8A%94%EB%8D%B0-llm-%EB%B9%84%EC%9A%A9%EC%9D%B4-3%EB%B0%B0%EA%B0%80-%EB%90%9C-%EC%9D%B4%EC%9C%A0-5ae60ab5108b)
- 토스: [작은 모델이 확신하는 트래픽만 떼어내 6일간 입력 토큰 약 76억 절감](https://toss.tech/article/snap-llm-cost-reduction)
- 인프랩 (인프런): [서비스엔 모델 이름 대신 등급만 노출, 최고치 대비 비용 78% 감소](https://tech.inflab.com/20260825-ai-gateway/)
- Spotify: [코딩 에이전트의 읽기 토큰 약 90% 절감](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90/)
- Cohere: [리드만 상위 모델, 일꾼은 싼 모델로 비용 70% 절감](https://cohere.com/blog/lessons-from-scaling-teams-of-frontier-coding-agents)
- Google: [정규식 라우터는 미공개 세트에서 93.8%→70.6%로 무너짐](https://developers.googleblog.com/cost-per-task-using-cheap-classifiers-to-route-across-gemini-models-and-thinking-levels/)

### 4. 모델은 리더보드가 아니라 자체 벤치와 회귀 세트로 고른다

공개 리더보드 순위는 언어·설정이 바뀌면 뒤집혔습니다. 실제 운영 프롬프트에서 뽑은 평가 세트와 '기존에 되던 것' 회귀 세트를 통과해야 교체하는 방식이 공통입니다.

- 채널톡: [회귀 세트 점수 유지를 필수 조건으로, 결과 비용 약 1/13](https://tech.channel.io/kr/articles/d1671db1)
- 토스: [공개 지표와 실제 업무 점수 상관 ρ 0.02, 자체 지시 평가는 0.71](https://toss.tech/article/toss-benchmark)
- 인프랩 (인프런): [등급별 테스트 세트를 통과한 모델만 교체](https://tech.inflab.com/20260825-ai-gateway/)

### 5. 에이전트는 '끝났다'는 말이 아니라 최종 상태와 반복 성공으로 채점한다

에이전트는 그럴듯하게 끝내고도 결과가 틀린 경우가 많습니다. 평균 정확도 대신 DB 같은 최종 상태와 k번 반복해도 성공하는지(pass^k)를 보고, 배포 전에 eval을 게이트로 둡니다.

- Hugging Face: [실패의 67%는 오류 없이 깔끔하게 종료됐지만 DB는 틀려 있었음](https://huggingface.co/blog/microsoft/thinkingbox)
- Hugging Face: [평균 77.4%인데 5번 연속 성공은 53.0%](https://huggingface.co/blog/ibm-research/altk-evolve-consistency)
- Grab: ['근거 전부 인용' 같은 지름길 답안이 통과하면 그 eval은 못 씀](https://engineering.grab.com/grab-bench-evaluating-ai)
- Google: [judge는 1~5점이 아니라 Yes/No, 사람이 채점한 트레이스와 대조](https://developers.googleblog.com/evaluating-ai-agents-moving-past-the-vibe-check/)
- LinkedIn: [AI 리뷰 품질은 병합된 코드에 반영됐는지로 측정, 채택률 63.9%](https://www.linkedin.com/blog/engineering/ai/high-signal-ai-code-review-that-adapts-to-your-codebase-at-scale)

### 6. 컨텍스트는 개인 설정이 아니라 팀이 관리하는 자산이다

같은 지표도 사람마다 다른 로그에서 뽑히는 문제가 개인 CLAUDE.md에서 생겼습니다. 도메인 지식을 팀 공용 문서로 구조화하고, 코드·PR을 기준으로 갱신하고, 쓰고 버릴 기록은 서브에이전트로 격리합니다.

- 카카오: [What(데이터 카탈로그)·How(분석 절차)·Why(Jira 맥락)로 나눠 팀 공용 관리](https://tech.kakao.com/posts/844)
- 카카오: [이후에도 쓰는 정보만 메인에, 실패 SQL은 서브에이전트에 격리](https://tech.kakao.com/posts/838)
- 무신사 (29CM 통합): [표준 Core 위에 조직 특화 Overlay, 표준 인용 1.6→7.6](https://techblog.musinsa.com/ai-native-%EC%A1%B0%EC%A7%81%EC%9D%80-%EB%8F%84%EB%A9%94%EC%9D%B8-%EC%A7%80%EC%8B%9D%EC%9D%84-%EC%96%B4%EB%96%BB%EA%B2%8C-%EA%B3%B5%EC%9C%A0%ED%95%98%EB%8A%94%EA%B0%80-f2e3de607df3)
- LINE: [PR이 병합될 때마다 지식 문서 갱신 PR 자동 생성](https://techblog.lycorp.co.jp/ko/llm-wiki-code-driven-knowledge-ssot)
- LINE: [21팀 112명 워크숍 결론: 병목은 도구가 아니라 컨텍스트](https://techblog.lycorp.co.jp/ko/conditions-for-organizational-aidd-adoption)

### 7. 흩어진 MCP·API 키·스킬은 중앙 플랫폼 하나로

팀마다 MCP 서버, 인증, API 키, 스킬을 따로 만들던 회사들이 게이트웨이나 허브로 모으고 있습니다. 한 곳을 거치게 하면 인증·관측·비용 통제·보안 검증을 같이 얻습니다.

- LINE: [MCP 서버 650개 이상, 인증 준비 1주→5분](https://techblog.lycorp.co.jp/ko/flava-mcp-hub-ai-infrastructure)
- Uber: [MCP 서버 800개·도구 5,000개, 필요한 도구만 점진 탐색](https://www.uber.com/us/en/blog/designing-mcp-gateway)
- PayPal: [공개 스킬 36.8%에 보안 이슈, 등록·검증·승인 경로를 하나로](https://developer.paypal.com/community/blog/agent_skills_at_enterprise_scale)
- 오늘의집 (버킷플레이스): [비개발자 앱 51개를 하네스·템플릿으로 3주 안에 운영 배포](https://www.bucketplace.com/post/2026-10-16-ai로-만든-앱-실제-서비스가-되려면-오늘의집-ai-개발-플랫폼-구축-오디세이)

### 8. 사람은 마지막 검수자가 아니라 앞단의 작은 승인자

AI가 만드는 속도보다 사람이 이해하고 검증하는 속도가 병목이 됐습니다. 판단은 사람에게 남기되, 승인을 작게 쪼개 구현 앞에 두고 검증·롤백 능력에 투자합니다.

- 우아한형제들: [명세→승인→테스트→승인→구현, 구현 약 2배 빠르게](https://techblog.woowahan.com/27604/)
- LINE: [AI는 판단 준비만, 확인된 규정만 단정형으로](https://techblog.lycorp.co.jp/ko/ai-agent-platform-sage-dev-log-part-1)
- Spotify: [머지된 PR 8,100→17,000건, 다음 병목은 검증 능력](https://engineering.atspotify.com/2026/9/ai-changed-how-spotify-builds-what-we-learned-and-fixed-about-quality-at-higher-velocity/)
- 우아한형제들: [코치 1명에서 세 기수 만에 AI 코치 65명](https://techblog.woowahan.com/27640/)

## 먼저 읽을 17편


### 비용

- **[모델만 바꿨는데 LLM 비용이 3배가 된 이유](https://medium.com/daangn/%EB%AA%A8%EB%8D%B8%EB%A7%8C-%EB%B0%94%EA%BF%A8%EB%8A%94%EB%8D%B0-llm-%EB%B9%84%EC%9A%A9%EC%9D%B4-3%EB%B0%B0%EA%B0%80-%EB%90%9C-%EC%9D%B4%EC%9C%A0-5ae60ab5108b)** · 당근마켓  
  모델만 바꿨더니 캐시가 깨져 요청당 비용 3.2배. 캐시를 깨는 요인과 제공사별 규칙 비교까지.
- **[손가락 튕기기로 LLM 비용 줄이기](https://toss.tech/article/snap-llm-cost-reduction)** · 토스  
  자체 모델로 '전부 대체' 대신 일치율 99.9%를 지키는 트래픽만 떼어냄. 임계값 정하는 법까지 공개.
- **[사내 LLM 요청을 한곳으로 모은 AI Gateway 구축기](https://tech.inflab.com/20260825-ai-gateway/)** · 인프랩 (인프런)  
  LLM 사용처 30곳 이상을 게이트웨이 하나로. 모델 이름 대신 비용 상한이 있는 등급으로 추상화.
- **[Spotify의 Portal로 Claude Code 토큰 사용량 90% 줄이기](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90/) <sub>Portal by Spotify cut my Claude Code token usage by 90%</sub>** · Spotify  
  Claude Code의 파일 읽기를 훅으로 가로채 Gemini Flash로 위임. 설정과 한계까지 재현 가능.
- **[코딩 에이전트 팀을 키우며 배운 것: 비용 30%로 최상위 성능 내기](https://cohere.com/blog/lessons-from-scaling-teams-of-frontier-coding-agents) <sub>Lessons from scaling teams of coding agents: reach the frontier at 30% of the cost</sub>** · Cohere  
  코딩 에이전트 팀 통제 실험. 탐색·계획만 위임해도 성능은 같고 비용은 절반.

### 에이전트 설계

- **[Thin Orchestrator: 라우터 일을 줄여 AI 에이전트를 더 안정적으로 만든 방법](https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/) <sub>The Thin Orchestrator: How We Made Our AI Agents More Reliable by Giving the Router Less to Do</sub>** · Meta  
  만능 에이전트 대신 결정적 라우터와 격리된 전문 서브에이전트 14개. 확장은 템플릿으로.
- **[LLM에게 어디까지 맡길 것인가: AI 에이전트 기반 광고 분석 리포트 자동화](https://techblog.lycorp.co.jp/ko/ai-agent-ad-report-automation)** · LINE  
  광고 리포트 자동화. 계산은 코드, 해석은 LLM, 원인 탐색은 그래프와 호출 상한으로 제한.
- **[Pensive AI로 장애 진단을 믿을 수 있게 만들기](https://netflixtechblog.com/making-failure-diagnosis-reliable-with-pensive-ai-6b0811a1c015) <sub>Making Failure Diagnosis Reliable with Pensive AI</sub>** · Netflix  
  규칙 기반 진단의 'unknown' 절반을 AI로 메움. 신뢰성은 모델이 아니라 주변 시스템에서.
- **[팀이 신뢰할 수 있는 AI 분석 환경 만들기: 추천팀의 컨텍스트 설계](https://tech.kakao.com/posts/844)** · 카카오  
  개인 CLAUDE.md의 한계를 팀 공용 컨텍스트(What·How·Why)로 해결한 구조 예시.

### 평가·모델 선택

- **[채널톡이 글로벌 상담 Agent를 GPT-5.6 Luna로 갈아탄 이유](https://tech.channel.io/kr/articles/d1671db1)** · 채널톡  
  리더보드에 없던 모델을 고른 과정. 탈락 기준, pass^k, 점진 배포 절차.
- **[리더보드 1등 LLM, 토스에서도 1등일까? - Toss Benchmark 구축기](https://toss.tech/article/toss-benchmark)** · 토스  
  사내 벤치마크 구축기. 공개 지표가 실제 업무 성과와 상관이 없다는 것을 수치로 보여줌.
- **[에이전트는 끝났다고 했다. 데이터베이스는 아니라고 했다.](https://huggingface.co/blog/microsoft/thinkingbox) <sub>The Agent Said It Was Done. The Database Disagreed.</sub>** · Hugging Face  
  업무 507개를 모델당 20회씩 반복. 한 번 성공과 매번 성공의 차이, 성공당 비용.
- **[Grab Bench: Grab의 실제 업무로 AI 평가하기](https://engineering.grab.com/grab-bench-evaluating-ai) <sub>Grab Bench: Evaluating AI on Grab-shaped production work</sub>** · Grab  
  그럴듯한 오답을 잡는 eval 설계 원칙. 일부러 나쁜 답안으로 eval 자체를 검증.

### 플랫폼·지식

- **[Flava MCP Hub가 걸어온 길: AI 시대를 위한 배관 공사](https://techblog.lycorp.co.jp/ko/flava-mcp-hub-ai-infrastructure)** · LINE  
  전사 MCP 허브 4층 구조와 오픈소스 게이트웨이를 버리고 직접 만든 이유.
- **[사내 지식으로 Agentic RAG 만들기 (2/3) : 검색을 얹기, LightRAG와 Navigator](https://techblog.gccompany.co.kr/%EC%82%AC%EB%82%B4-%EC%A7%80%EC%8B%9D%EC%9C%BC%EB%A1%9C-agentic-rag-%EB%A7%8C%EB%93%A4%EA%B8%B0-2-3-%EA%B2%80%EC%83%89%EC%9D%84-%EC%96%B9%EA%B8%B0-lightrag%EC%99%80-navigator-9f3119060242)** · 여기어때  
  사내 문서 17만 건 Agentic RAG. 리트리버 분업, 청크 경로 붙이기, 적재 81% 단축. (2편)
- **[사내 지식으로 Agentic RAG 만들기 (3/3) : 관측 가능한 RAG, 운영되는 도구로](https://techblog.gccompany.co.kr/%EC%82%AC%EB%82%B4-%EC%A7%80%EC%8B%9D%EC%9C%BC%EB%A1%9C-agentic-rag-%EB%A7%8C%EB%93%A4%EA%B8%B0-3-3-%EA%B4%80%EC%B8%A1-%EA%B0%80%EB%8A%A5%ED%95%9C-rag-%EC%9A%B4%EC%98%81%EB%90%98%EB%8A%94-%EB%8F%84%EA%B5%AC%EB%A1%9C-dbac813832db)** · 여기어때  
  같은 시리즈 3편. Langfuse로 RAG 평가, MCP 도구 명세만 다듬어 정확도 3~9%p 향상.

### 사람의 역할

- **[배달의민족 전자계약서 화면 개편기: AI에게 맡긴 것과 사람이 챙긴 것](https://techblog.woowahan.com/27604/)** · 우아한형제들  
  명세→승인→테스트→승인→구현으로 AI 개발. 버그가 오히려 늘어난 실패 경험까지 솔직하게.

## 함께 보면 좋은 글

- [코드베이스에 맞춰 적응하는, 신호 높은 대규모 AI 코드 리뷰](https://www.linkedin.com/blog/engineering/ai/high-signal-ai-code-review-that-adapts-to-your-codebase-at-scale) <sub>High-Signal AI Code Review That Adapts to Your Codebase at Scale</sub> · LinkedIn
- [MCP Gateway 설계: Uber의 MCP 관리 플랫폼](https://www.uber.com/us/en/blog/designing-mcp-gateway) <sub>Designing MCP Gateway</sub> · Uber
- [PayPal이 전사 규모로 에이전트 스킬을 관리하는 방법](https://developer.paypal.com/community/blog/agent_skills_at_enterprise_scale) <sub>How PayPal is governing agent skills at enterprise scale</sub> · PayPal
- [에이전트가 작업을 해냈다. 다음에도 해낼까?](https://huggingface.co/blog/ibm-research/altk-evolve-consistency) <sub>Your Agent Aced the Task. Will It Do It Again?</sub> · Hugging Face
- [블로그 발행 MCP를 직접 만들며 확인한 AI 에이전트 실무 원칙 - 구성요소부터 사람 승인까지](http://devocean.sk.com/blog/techBoardDetail.do?id=168583&boardType=techBlog&isShared=Y) · SK텔레콤 DEVOCEAN
- [머릿속에 있던 로그 정의 기준을 모두의 AI 스킬로 만들기](https://toss.tech/article/dataops-log-definition-skill) · 토스
- [데이터 분석 에이전트를 만들며 배운 컨텍스트 설계](https://tech.kakao.com/posts/838) · 카카오
- [AI로 만든 앱, 실제 서비스가 되려면? - 오늘의집 AI 개발 플랫폼 구축 오디세이 AI시대 ‘진짜’ 병목을 해결하는, AI 개발 플랫폼 ‘올리고’ 개발 기록 AI frontier](https://www.bucketplace.com/post/2026-10-16-ai로-만든-앱-실제-서비스가-되려면-오늘의집-ai-개발-플랫폼-구축-오디세이) · 오늘의집 (버킷플레이스)
- [LLM Wiki: 코드 기준으로 자동 최신화되는 도메인 지식 SSOT 만들기](https://techblog.lycorp.co.jp/ko/llm-wiki-code-driven-knowledge-ssot) · LINE
- [AI Native 조직은 도메인 지식을 어떻게 공유하는가](https://techblog.musinsa.com/ai-native-%EC%A1%B0%EC%A7%81%EC%9D%80-%EB%8F%84%EB%A9%94%EC%9D%B8-%EC%A7%80%EC%8B%9D%EC%9D%84-%EC%96%B4%EB%96%BB%EA%B2%8C-%EA%B3%B5%EC%9C%A0%ED%95%98%EB%8A%94%EA%B0%80-f2e3de607df3) · 무신사 (29CM 통합)
- [보안 업무를 위한 AI 에이전트 플랫폼 「SAGE」 개발기 1편: 판단은 사람에게 남기는 설계](https://techblog.lycorp.co.jp/ko/ai-agent-platform-sage-dev-log-part-1) · LINE
- [AI 에이전트 평가: 감으로 보는 단계에서 벗어나기](https://developers.googleblog.com/evaluating-ai-agents-moving-past-the-vibe-check/) <sub>Evaluating AI agents: moving past the vibe check</sub> · Google
- [작업당 비용: 저렴한 분류기로 Gemini 모델과 사고 수준 라우팅하기](https://developers.googleblog.com/cost-per-task-using-cheap-classifiers-to-route-across-gemini-models-and-thinking-levels/) <sub>Cost per task: Using cheap classifiers to route across Gemini models and thinking levels</sub> · Google
- [AI가 바꾼 Spotify의 개발 방식: 빨라진 속도에서 품질에 대해 배우고 고친 것](https://engineering.atspotify.com/2026/9/ai-changed-how-spotify-builds-what-we-learned-and-fixed-about-quality-at-higher-velocity/) <sub>AI Changed How Spotify Builds. What We Learned (and Fixed) About Quality at Higher Velocity</sub> · Spotify
