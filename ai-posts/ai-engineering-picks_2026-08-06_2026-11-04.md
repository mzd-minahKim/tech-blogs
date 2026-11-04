# AI 엔지니어링 실무 글 모음 (2026-08-06 ~ 2026-11-04)

국내외 기술 블로그 86곳에서 3개월 동안 올라온 AI 글 730개 중, 사내 업무를 AI로 바꾸는 일(AX)과 에이전트 개발·운영에 바로 참고할 만한 140개를 주제별로 골랐습니다. ⭐는 먼저 읽어볼 만한 글입니다.

- 전체 목록: [AI 관련 글 모음](2026-08-06_2026-11-04.md)
- Microsoft의 'AX'는 Agent Experience(에이전트가 쓰기 좋은 도구 설계)를 뜻합니다.

## ⭐ 먼저 읽을 글

- [손가락 튕기기로 LLM 비용 줄이기](https://toss.tech/article/snap-llm-cost-reduction) · 토스
- [모델만 바꿨는데 LLM 비용이 3배가 된 이유](https://medium.com/daangn/%EB%AA%A8%EB%8D%B8%EB%A7%8C-%EB%B0%94%EA%BF%A8%EB%8A%94%EB%8D%B0-llm-%EB%B9%84%EC%9A%A9%EC%9D%B4-3%EB%B0%B0%EA%B0%80-%EB%90%9C-%EC%9D%B4%EC%9C%A0-5ae60ab5108b) · 당근마켓
- [Portal by Spotify cut my Claude Code token usage by 90%](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90/) · Spotify
- [Gisting: Compressing LLM Agent context to ↑ throughput and ↓ cost](https://shopify.engineering/gisting) · Shopify
- [개인 AI 활용의 다음 단계는 무엇인가 - LY Corporation에서 AIDD 워크숍을 통해 살펴본 AIDD 조직 도입의 조건](https://techblog.lycorp.co.jp/ko/conditions-for-organizational-aidd-adoption) · LINE (LY Corporation)
- [AI Native 조직은 도메인 지식을 어떻게 공유하는가](https://techblog.musinsa.com/ai-native-%EC%A1%B0%EC%A7%81%EC%9D%80-%EB%8F%84%EB%A9%94%EC%9D%B8-%EC%A7%80%EC%8B%9D%EC%9D%84-%EC%96%B4%EB%96%BB%EA%B2%8C-%EA%B3%B5%EC%9C%A0%ED%95%98%EB%8A%94%EA%B0%80-f2e3de607df3) · 무신사 (29CM 통합)
- [팀이 신뢰할 수 있는 AI 분석 환경 만들기: 추천팀의 컨텍스트 설계](https://tech.kakao.com/posts/844) · 카카오
- [데이터 분석 에이전트를 만들며 배운 컨텍스트 설계](https://tech.kakao.com/posts/838) · 카카오
- [The Thin Orchestrator: How We Made Our AI Agents More Reliable by Giving the Router Less to Do](https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/) · Meta (Facebook)
- [머릿속에 있던 로그 정의 기준을 모두의 AI 스킬로 만들기](https://toss.tech/article/dataops-log-definition-skill) · 토스
- [나는 하네스 깎는 노인이 되었다 시리즈 2: 안녕, 실버불릿](https://meetup.nhncloud.com/posts/426) · NHN Cloud Meetup (구 TOAST Meetup)
- [같은 LLM인데 왜 결과가 다를까? 답은 하네스에 있다.](https://tech.hancom.com/harness-engineering/) · 한글과컴퓨터
- [Flava MCP Hub가 걸어온 길: AI 시대를 위한 배관 공사](https://techblog.lycorp.co.jp/ko/flava-mcp-hub-ai-infrastructure) · LINE (LY Corporation)
- [Designing MCP Gateway: Uber's MCP Management Platform](https://www.uber.com/us/en/blog/designing-mcp-gateway) · Uber
- [How PayPal is governing agent skills at enterprise scale](https://developer.paypal.com/community/blog/agent_skills_at_enterprise_scale) · PayPal
- [How to Evaluate AI Agents From Tool Calls to Task Completion](https://developer.nvidia.com/blog/how-to-evaluate-ai-agents-from-tool-calls-to-task-completion/) · NVIDIA Technical Blog
- [Tracing Agent Harness Behavior with NVIDIA NeMo Relay](https://developer.nvidia.com/blog/tracing-agent-harness-behavior-with-nvidia-nemo-relay/) · NVIDIA Technical Blog
- [Evaluating AI agents: moving past the vibe check](https://developers.googleblog.com/evaluating-ai-agents-moving-past-the-vibe-check/) · Google
- [Hill-Climbing Agent Quality with Agents CLI Evaluation](https://developers.googleblog.com/hill-climbing-agent-quality-with-agents-cli-evaluation/) · Google
- [리더보드 1등 LLM, 토스에서도 1등일까? - Toss Benchmark 구축기](https://toss.tech/article/toss-benchmark) · 토스
- [채널톡이 글로벌 상담 Agent를 GPT-5.6 Luna로 갈아탄 이유](https://tech.channel.io/kr/articles/d1671db1) · 채널톡
- [사내 지식으로 Agentic RAG 만들기 (2/3) : 검색을 얹기, LightRAG와 Navigator](https://techblog.gccompany.co.kr/%EC%82%AC%EB%82%B4-%EC%A7%80%EC%8B%9D%EC%9C%BC%EB%A1%9C-agentic-rag-%EB%A7%8C%EB%93%A4%EA%B8%B0-2-3-%EA%B2%80%EC%83%89%EC%9D%84-%EC%96%B9%EA%B8%B0-lightrag%EC%99%80-navigator-9f3119060242) · 여기어때
- [사내 지식으로 Agentic RAG 만들기 (3/3) : 관측 가능한 RAG, 운영되는 도구로](https://techblog.gccompany.co.kr/%EC%82%AC%EB%82%B4-%EC%A7%80%EC%8B%9D%EC%9C%BC%EB%A1%9C-agentic-rag-%EB%A7%8C%EB%93%A4%EA%B8%B0-3-3-%EA%B4%80%EC%B8%A1-%EA%B0%80%EB%8A%A5%ED%95%9C-rag-%EC%9A%B4%EC%98%81%EB%90%98%EB%8A%94-%EB%8F%84%EA%B5%AC%EB%A1%9C-dbac813832db) · 여기어때
- [How Dynata scaled AI across the development lifecycle with AI-DLC and Kiro IDE](https://aws.amazon.com/blogs/architecture/how-dynata-scaled-ai-across-the-development-lifecycle-with-ai-dlc-and-kiro-ide/) · AWS Architecture

## 1. 토큰·비용 절감 (19개)

LLM 비용, 캐싱, 컨텍스트 압축, 모델 라우팅

- ⭐ [손가락 튕기기로 LLM 비용 줄이기](https://toss.tech/article/snap-llm-cost-reduction) · 토스 · 10-27
- ⭐ [모델만 바꿨는데 LLM 비용이 3배가 된 이유](https://medium.com/daangn/%EB%AA%A8%EB%8D%B8%EB%A7%8C-%EB%B0%94%EA%BF%A8%EB%8A%94%EB%8D%B0-llm-%EB%B9%84%EC%9A%A9%EC%9D%B4-3%EB%B0%B0%EA%B0%80-%EB%90%9C-%EC%9D%B4%EC%9C%A0-5ae60ab5108b) · 당근마켓 · 10-21
- ⭐ [Portal by Spotify cut my Claude Code token usage by 90%](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90/) · Spotify · 09-04
- ⭐ [Gisting: Compressing LLM Agent context to ↑ throughput and ↓ cost](https://shopify.engineering/gisting) · Shopify · 08-19
- [How Coinbase used Code Connect to guide agents and shrink token costs](https://www.figma.com/blog/how-coinbase-used-code-connect-to-shrink-token-costs/) · Figma · 09-03
- [Lessons from scaling teams of coding agents: reach the frontier at 30% of the cost Oct 14, 2026 17 min read](https://cohere.com/blog/lessons-from-scaling-teams-of-frontier-coding-agents) · Cohere · 10-15
- [Cost per task: Using cheap classifiers to route across Gemini models and thinking levels](https://developers.googleblog.com/cost-per-task-using-cheap-classifiers-to-route-across-gemini-models-and-thinking-levels/) · Google · 11-03
- [How Tailscale built a customer-facing model router on AI Gateway](https://vercel.com/blog/how-tailscale-built-a-customer-facing-model-router-on-ai-gateway) · Vercel · 09-11
- [사내 LLM 요청을 한곳으로 모은 AI Gateway 구축기](https://tech.inflab.com/20260825-ai-gateway/) · 인프랩 (인프런) · 09-09
- [Better prompt caching for GPT-6](https://openai.com/index/better-prompt-caching-for-gpt-6) · OpenAI · 09-23
- [Asana cuts model costs 76x in browser tests with GPT-6.1 Sol](https://openai.com/index/asana-browser-agent) · OpenAI · 10-09
- [LegalOn halves Codex costs while maintaining development speed](https://openai.com/index/legalon-halves-codex-costs) · OpenAI · 10-08
- [V7 cuts costs 78% while boosting accuracy with GPT-5.6 Luna](https://openai.com/index/v7) · OpenAI · 09-21
- [Managing Amazon Bedrock costs end to end: A playbook for FinOps and platform teams](https://aws.amazon.com/blogs/machine-learning/managing-amazon-bedrock-costs-end-to-end-a-playbook-for-finops-and-platform-teams/) · AWS Machine Learning · 10-31
- [Cutting our inference bill by 68% by being obsessive about optimization](https://blog.cloudflare.com/obsessive-inference-optimization/) · Cloudflare · 10-20
- [How Specializing the Vocabulary of SLMs Can Cut Inference Cost by 77% in Real Applications](https://huggingface.co/blog/Dharma-AI/vocabx-vocabulary-specialization) · Hugging Face · 10-22
- [Thinking of ACE? We Can Do It with Fewer Tokens](https://huggingface.co/blog/ibm-research/altk-evolve-sldd) · Hugging Face · 08-11
- [Self-Compacting Language Model Agents](https://machinelearning.apple.com/research/self-compacting-language-agents) · Apple Machine Learning Research · 10-12
- [How Much Memory Does Your Agent Actually Need?](https://huggingface.co/blog/ibm-research/altk-evolve-hmm) · Hugging Face · 08-19

## 2. AX: 조직의 AI 전환과 AI-Native하게 일하기 (22개)

도입 조건, 일하는 방식, 효과 측정, 플랫폼화

- ⭐ [개인 AI 활용의 다음 단계는 무엇인가 - LY Corporation에서 AIDD 워크숍을 통해 살펴본 AIDD 조직 도입의 조건](https://techblog.lycorp.co.jp/ko/conditions-for-organizational-aidd-adoption) · LINE (LY Corporation) · 08-07
- ⭐ [AI Native 조직은 도메인 지식을 어떻게 공유하는가](https://techblog.musinsa.com/ai-native-%EC%A1%B0%EC%A7%81%EC%9D%80-%EB%8F%84%EB%A9%94%EC%9D%B8-%EC%A7%80%EC%8B%9D%EC%9D%84-%EC%96%B4%EB%96%BB%EA%B2%8C-%EA%B3%B5%EC%9C%A0%ED%95%98%EB%8A%94%EA%B0%80-f2e3de607df3) · 무신사 (29CM 통합) · 08-25
- [대AI시대에 일하는 방식의 변화에 대한 고찰](https://techblog.musinsa.com/%EB%8C%80ai%EC%8B%9C%EB%8C%80%EC%97%90-%EC%9D%BC%ED%95%98%EB%8A%94-%EB%B0%A9%EC%8B%9D%EC%9D%98-%EB%B3%80%ED%99%94%EC%97%90-%EB%8C%80%ED%95%9C-%EA%B3%A0%EC%B0%B0-6d11e0b1fead) · 무신사 (29CM 통합) · 10-27
- [AI 전환, 우리가 도운 건 돕는 사람이었습니다](https://techblog.woowahan.com/27640/) · 우아한형제들 · 09-14
- [AI 시대 당신의 팀은 안녕하신가요](https://techblog.gccompany.co.kr/ai-%EC%8B%9C%EB%8C%80-%EB%8B%B9%EC%8B%A0%EC%9D%98-%ED%8C%80-%EC%A1%B0%EC%A7%81%EC%9D%80-%EC%95%88%EB%85%95%ED%95%98%EC%8B%A0%EA%B0%80%EC%9A%94-c59f982d5add) · 여기어때 · 10-10
- [더 중요한 고민에 집중하는 올리브영 PM이 AI로 일하는 방식](https://oliveyoung.tech/2026-10-29/%EC%98%AC%EB%A6%AC%EB%B8%8C%EC%98%81-pm%EC%9D%B4-ai%EC%99%80-%ED%95%A8%EA%BB%98-%EC%9D%BC%ED%95%98%EB%8A%94-%EB%B0%A9%EC%8B%9D/) · 올리브영 · 10-29
- [프롬프트를 쓰는 PM과 AI를 이해시키려는 개발자](https://oliveyoung.tech/2026-08-28/search-mcp/) · 올리브영 · 08-28
- [서비스 개발에 집중할 수 있는 AI 플랫폼 만들기](https://toss.tech/article/ai-platform-foundation) · 토스 · 10-13
- [AI로 만든 앱, 실제 서비스가 되려면? - 오늘의집 AI 개발 플랫폼 구축 오디세이 AI시대 ‘진짜’ 병목을 해결하는, AI 개발 플랫폼 ‘올리고’ 개발 기록 AI frontier](https://www.bucketplace.com/post/2026-10-16-ai로-만든-앱-실제-서비스가-되려면-오늘의집-ai-개발-플랫폼-구축-오디세이) · 오늘의집 (버킷플레이스)
- [Data Playground - 오늘의집 바이브 코딩 플랫폼 한 사람이 하나의 앱을, 데이터부터 배포까지 스스로 AI frontier](https://www.bucketplace.com/post/2026-08-30-data-playground-오늘의집-바이브-코딩-플랫폼) · 오늘의집 (버킷플레이스)
- [Becoming an AI Team](https://medium.com/pinterest-engineering/becoming-an-ai-team-866d6b567803) · Pinterest · 09-02
- [Dropbox CTO Ali Dasdan on moving from AI adoption to transformation](https://dropbox.tech/culture/learnings-from-deploying-ai-at-company-scale) · Dropbox · 09-23
- [AI Changed How Spotify Builds. What We Learned (and Fixed) About Quality at Higher Velocity](https://engineering.atspotify.com/2026/9/ai-changed-how-spotify-builds-what-we-learned-and-fixed-about-quality-at-higher-velocity/) · Spotify · 09-17
- [4 team rituals that drive AI adoption](https://www.figma.com/blog/4-team-rituals-that-drive-ai-adoption/) · Figma · 10-10
- [How do you actually measure the impact of AI on design?](https://www.figma.com/blog/measuring-the-impact-of-ai/) · Figma · 08-29
- [How to connect AI usage to business value](https://openai.com/index/how-to-connect-ai-usage-to-business-value) · OpenAI · 09-16
- [AI ROI: How enterprises can measure the return on AI investments Oct 15, 2026 6 min read](https://cohere.com/blog/ai-roi) · Cohere · 10-15
- [How AI-native companies turn workflows into operating capability](https://openai.com/index/ai-native-company-workflows) · OpenAI · 09-02
- [From assistance to execution: How enterprises put AI to work](https://openai.com/index/how-enterprises-put-ai-to-work) · OpenAI · 08-12
- [How RingCentral builds AI-native work from engineering to ops](https://openai.com/index/ringcentral) · OpenAI · 08-12
- [What is Agent Experience (AX)?](https://devblogs.microsoft.com/blog/what-is-agent-experience-ax/) · Microsoft · 10-06
- [Introducing the Agent Experience (AX) Practitioner Playbook](https://devblogs.microsoft.com/blog/introducing-the-agent-experience-ax-practitioner-playbook/) · Microsoft · 10-09

## 3. 사내 업무를 에이전트 워크플로로 옮긴 사례 (26개)

분석·QA·운영·보안 업무 자동화

- ⭐ [팀이 신뢰할 수 있는 AI 분석 환경 만들기: 추천팀의 컨텍스트 설계](https://tech.kakao.com/posts/844) · 카카오 · 10-28
- ⭐ [데이터 분석 에이전트를 만들며 배운 컨텍스트 설계](https://tech.kakao.com/posts/838) · 카카오 · 10-02
- [LLM에게 어디까지 맡길 것인가: AI 에이전트 기반 광고 분석 리포트 자동화](https://techblog.lycorp.co.jp/ko/ai-agent-ad-report-automation) · LINE (LY Corporation) · 09-18
- [LLM이 만든 SQL을 믿고 실행하기까지: A2A 기반의 대화형 BI 애플리케이션 개발기](https://techblog.lycorp.co.jp/ko/a2a-conversational-bi-app) · LINE (LY Corporation) · 10-02
- [보안 업무를 위한 AI 에이전트 플랫폼 「SAGE」 개발기 1편: 판단은 사람에게 남기는 설계](https://techblog.lycorp.co.jp/ko/ai-agent-platform-sage-dev-log-part-1) · LINE (LY Corporation) · 08-18
- [오늘의집 Self-Service Data Analytics 구축기 AI가 데이터를 읽고, 오늘의집의 기준으로 답하기까지 AI frontier](https://www.bucketplace.com/post/2026-10-29-오늘의집-self-service-data-analytics-구축기) · 오늘의집 (버킷플레이스)
- [DB 업무, 어디까지 자동화할까 - DBRE의 두 가지 답 DB 변경은 Git PR로, 반복적인 운영 업무는 셀프서비스로 AI frontier](https://www.bucketplace.com/post/2026-10-07-db-업무-어디까지-자동화할까-dbre의-두-가지-답) · 오늘의집 (버킷플레이스)
- [기획서 하나로 결함 등록까지, QA AI Hub를 만들며 배운 것](https://helloworld.kurly.com/blog/ai-qa-from-spec-to-defect/) · 마켓컬리 · 11-03
- [QA 티켓 280건, AI와 함께 처리한 기록](https://techblog.gccompany.co.kr/qa-%ED%8B%B0%EC%BC%93-280%EA%B1%B4-ai%EC%99%80-%ED%95%A8%EA%BB%98-%EC%B2%98%EB%A6%AC%ED%95%9C-%EA%B8%B0%EB%A1%9D-447b8b8b0f99) · 여기어때 · 09-17
- [버그 티켓, AI에게 맡겨봤습니다 — QUBA 개발기](https://techtopic.skplanet.com/quba/) · SK플래닛 · 10-19
- [AI로 E2E 회귀 테스트 자동화하기: ‘딸깍’을 파이프라인으로 바꾸기까지](https://techblog.lycorp.co.jp/ko/ai-e2e-test-automation) · LINE (LY Corporation) · 10-16
- [AI를 활용한 테스트 자동화 도전기 1편](https://medium.com/ssgtech/ai-%ED%8E%98%EC%96%B4-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%99%80-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%9E%90%EB%8F%99%ED%99%94-%EB%8F%84%EC%A0%84%EA%B8%B0-33dab17571e6) · SSG · 09-01
- [연 300시간을 아낀 AI 상담 서비스](https://toss.tech/article/AI_chatbot) · 토스 · 09-23
- [How Ultrafast cut incident investigation from hours to minutes at OpenAI](https://openai.com/index/openai-cut-incident-investigation) · OpenAI · 10-26
- [How Circle K accelerated DevOps incident triage to under 15 minutes with Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/how-circle-k-accelerated-devops-incident-triage-to-under-15-minutes-with-amazon-bedrock/) · AWS Machine Learning · 11-03
- [Making Failure Diagnosis Reliable with Pensive AI](https://netflixtechblog.com/making-failure-diagnosis-reliable-with-pensive-ai-6b0811a1c015) · Netflix · 10-27
- [Quality Assurance Agent: Reimagining Software Quality with AI-Driven Autonomous ...](https://www.linkedin.com/blog/engineering/ai/qa-agent-reimagining-software-quality-with-ai-driven-autonomous-testing) · LinkedIn
- [High-Signal AI Code Review That Adapts to Your Codebase at Scale](https://www.linkedin.com/blog/engineering/ai/high-signal-ai-code-review-that-adapts-to-your-codebase-at-scale) · LinkedIn
- [Scaling AI in Legal: Building Uber’s Redlining Agent](https://www.uber.com/us/en/blog/building-ubers-redlining-agent) · Uber
- [Metrics Board: Building an Agent-ready Metrics Layer](https://medium.com/pinterest-engineering/metrics-board-building-an-agent-ready-metrics-layer-2c8fefe68756) · Pinterest · 10-07
- [Building Reliable Data Analytics Agents: Lessons from the KDD Cup](https://developer.nvidia.com/blog/building-reliable-data-analytics-agents-lessons-from-the-kdd-cup/) · NVIDIA Technical Blog · 10-09
- ⭐ [The Thin Orchestrator: How We Made Our AI Agents More Reliable by Giving the Router Less to Do](https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/) · Meta (Facebook) · 10-20
- [Stripe’s Payment Method Factory: Orchestrating agents for repeated, custom integrations](https://stripe.dev/blog/stripes-payment-method-factory-orchestrating-agents-for-repeated-custom-integrations) · Stripe · 09-30
- [Harbor: Stripe’s AI-assisted prototyping tool](https://stripe.dev/blog/harbor-stripes-ai-assisted-prototyping-tool) · Stripe · 09-14
- [AI didn't write our SDK. It changed how we built it.](https://stripe.dev/blog/ai-didnt-write-our-sdk-it-changed-how-we-built-it) · Stripe · 08-28
- [Building a software factory for AI SDK](https://vercel.com/blog/building-a-software-factory-for-ai-sdk) · Vercel · 08-12

## 4. 재사용 컴포넌트: 스킬·커맨드·하네스·MCP·지식베이스 (23개)

팀이 두고두고 쓰는 에이전트 인프라

- ⭐ [머릿속에 있던 로그 정의 기준을 모두의 AI 스킬로 만들기](https://toss.tech/article/dataops-log-definition-skill) · 토스 · 10-23
- ⭐ [나는 하네스 깎는 노인이 되었다 시리즈 2: 안녕, 실버불릿](https://meetup.nhncloud.com/posts/426) · NHN Cloud Meetup (구 TOAST Meetup) · 10-20
- [나는 하네스 깎는 노인이 되었다 시리즈 1: 은총알은 없다](https://meetup.nhncloud.com/posts/423) · NHN Cloud Meetup (구 TOAST Meetup) · 09-28
- ⭐ [같은 LLM인데 왜 결과가 다를까? 답은 하네스에 있다.](https://tech.hancom.com/harness-engineering/) · 한글과컴퓨터 · 08-21
- [AI Agent, 넌 누구냐 2 - 네이티브 개발자를 위한 FE 하네스를 만들고, 레거시가 되기까지 네이티브 개발자의 FE 개발을 돕기 위해 컨벤션과 개발 방식을 담은 AI Agent 하네스를 만들](https://tech.kakaopay.com/post/ai-agent-2) · 카카오페이
- [에이전트, 개념부터 같이 정리해봐요 - 워크플로우 · 하네스 · Context/Memory · MCP/A2A](https://d2.naver.com/helloworld/8118359) · Naver D2 · 10-01
- [코딩 에이전트가 Spring을 못 짠다면, component scan부터 걷어내 보세요](https://flex.team/blog/2026/10/13/backend46) · 플렉스 (flex) · 10-13
- [시킬 때마다 다른 결과를 내는 AI에게 도구를 쥐여 주었습니다 — AI가 쓰는 ERD 도구 제작기](https://techblog.gccompany.co.kr/%EC%8B%9C%ED%82%AC-%EB%95%8C%EB%A7%88%EB%8B%A4-%EB%8B%A4%EB%A5%B8-%EA%B2%B0%EA%B3%BC%EB%A5%BC-%EB%82%B4%EB%8A%94-ai%EC%97%90%EA%B2%8C-%EB%8F%84%EA%B5%AC%EB%A5%BC-%EC%A5%90%EC%97%AC-%EC%A3%BC%EC%97%88%EC%8A%B5%EB%8B%88%EB%8B%A4-ai%EA%B0%80-%EC%93%B0%EB%8A%94-erd-%EB%8F%84%EA%B5%AC-%EC%A0%9C%EC%9E%91%EA%B8%B0-f97eefa26354) · 여기어때 · 10-10
- ⭐ [Flava MCP Hub가 걸어온 길: AI 시대를 위한 배관 공사](https://techblog.lycorp.co.jp/ko/flava-mcp-hub-ai-infrastructure) · LINE (LY Corporation) · 10-26
- ⭐ [Designing MCP Gateway: Uber's MCP Management Platform](https://www.uber.com/us/en/blog/designing-mcp-gateway) · Uber
- [What We Learned Building PayPal's MCP Gateway](https://developer.paypal.com/community/blog/PayPal_MCP_Gateway) · PayPal
- [Jira’s depth, on demand: designing an MCP server around jobs, not endpoints](https://www.atlassian.com/blog/how-we-build/jira-depth-on-demand) · Atlassian · 10-29
- [블로그 발행 MCP를 직접 만들며 확인한 AI 에이전트 실무 원칙 - 구성요소부터 사람 승인까지](http://devocean.sk.com/blog/techBoardDetail.do?id=168583&boardType=techBlog&isShared=Y) · SK텔레콤 DEVOCEAN · 10-29
- [국내 최초 광고 MCP를 출시하며, 개발자의 역할은 어디까지 넓어졌을까?](https://medium.com/daangn/%EA%B5%AD%EB%82%B4-%EC%B5%9C%EC%B4%88-%EA%B4%91%EA%B3%A0-mcp%EB%A5%BC-%EC%B6%9C%EC%8B%9C%ED%95%98%EB%A9%B0-%EA%B0%9C%EB%B0%9C%EC%9E%90%EC%9D%98-%EC%97%AD%ED%95%A0%EC%9D%80-%EC%96%B4%EB%94%94%EA%B9%8C%EC%A7%80-%EB%84%93%EC%96%B4%EC%A1%8C%EC%9D%84%EA%B9%8C-8dea7fe41c07) · 당근마켓 · 11-03
- ⭐ [How PayPal is governing agent skills at enterprise scale](https://developer.paypal.com/community/blog/agent_skills_at_enterprise_scale) · PayPal
- [State of agent skills](https://vercel.com/blog/state-of-agent-skills) · Vercel · 09-25
- [Enabling Consistent AI-Assisted Engineering with GitHub Copilot Plugins](https://devblogs.microsoft.com/blog/enabling-consistent-ai-assisted-engineering-with-github-copilot-plugins/) · Microsoft · 09-30
- [How our agents build on-brand pages with design.md](https://vercel.com/blog/how-our-agents-build-on-brand-pages-with-design-md) · Vercel · 08-31
- [LLM Wiki: 코드 기준으로 자동 최신화되는 도메인 지식 SSOT 만들기](https://techblog.lycorp.co.jp/ko/llm-wiki-code-driven-knowledge-ssot) · LINE (LY Corporation) · 08-28
- [Give Your Coding Agents a Memory You Own](https://huggingface.co/blog/funes) · Hugging Face · 09-03
- [Getting the Source Right, Not Just the Fact: Source-Aware Verification for MCP Agents](https://huggingface.co/blog/MultiverseComputingCAI/getting-the-source-right-not-just-the-fact-source) · Hugging Face · 09-29
- [Plan or Retrieve First? A Scale Study of Tool Discovery Architectures](https://machinelearning.apple.com/research/plan-retrieve-tool-discovery) · Apple Machine Learning Research · 10-15
- [Stop Giving AI More Documentation. Give It an API.](https://developer.paypal.com/community/blog/stopgivingaimoredocumentation) · PayPal

## 5. 평가(Eval)·트레이스·가드레일·거버넌스 (25개)

Eval-driven 개발, 실행 트레이스 진단, 런타임 통제

- [Jev로 AI 글 냄새 잡기 - 판정 모델을 교정 파이프라인 세 곳에 붙인 기록](http://devocean.sk.com/blog/techBoardDetail.do?id=168525&boardType=techBlog&isShared=Y) · SK텔레콤 DEVOCEAN · 09-29
- ⭐ [How to Evaluate AI Agents From Tool Calls to Task Completion](https://developer.nvidia.com/blog/how-to-evaluate-ai-agents-from-tool-calls-to-task-completion/) · NVIDIA Technical Blog · 09-22
- ⭐ [Tracing Agent Harness Behavior with NVIDIA NeMo Relay](https://developer.nvidia.com/blog/tracing-agent-harness-behavior-with-nvidia-nemo-relay/) · NVIDIA Technical Blog · 10-01
- ⭐ [Evaluating AI agents: moving past the vibe check](https://developers.googleblog.com/evaluating-ai-agents-moving-past-the-vibe-check/) · Google · 10-15
- ⭐ [Hill-Climbing Agent Quality with Agents CLI Evaluation](https://developers.googleblog.com/hill-climbing-agent-quality-with-agents-cli-evaluation/) · Google · 10-28
- [Does ‘eval’ in the workspace path change what your agent does?](https://devblogs.microsoft.com/blog/does-eval-in-the-workspace-path-change-what-your-agent-does/) · Microsoft · 10-30
- [Can a local git remote replace GitHub in your agent eval?](https://devblogs.microsoft.com/blog/can-a-local-git-remote-replace-github-in-your-agent-eval/) · Microsoft · 10-20
- [Introducing Run SDK: secure eval for your agents](https://vercel.com/blog/introducing-run) · Vercel · 08-25
- [How Ora benchmarks every major AI agent on Vercel](https://vercel.com/blog/how-ora-benchmarks-every-major-ai-agent-on-vercel) · Vercel · 08-22
- [Your Agent Aced the Task. Will It Do It Again?](https://huggingface.co/blog/ibm-research/altk-evolve-consistency) · Hugging Face · 09-16
- [The Agent Said It Was Done. The Database Disagreed.](https://huggingface.co/blog/microsoft/thinkingbox) · Hugging Face · 10-04
- [Grab Bench: Evaluating AI on Grab-shaped production work](https://engineering.grab.com/grab-bench-evaluating-ai) · Grab · 08-12
- [ShopGym: Realistic, reproducible sandboxes for shopping agents](https://shopify.engineering/shopgym) · Shopify · 10-02
- [Agents, Randomness, and Receipts: Notes from trivago's QA Meetup](https://tech.trivago.com/post/2026-08-12-agents-randomness-and-receipts-notes-from-trivagos-qa-meetup/) · Trivago · 08-12
- [From synthetic enterprise data evaluations to real Microsoft Copilot AI confidence](https://www.microsoft.com/en-us/research/blog/from-synthetic-enterprise-data-evaluations-to-real-microsoft-copilot-ai-confidence/) · Microsoft Research · 10-30
- [Investigating unintended model actions in our evaluations and internal use](https://www.anthropic.com/research/investigating-unintended-model-actions) · Anthropic Research · 10-09
- [Add Runtime Controls to AI Agents with NVIDIA OpenShell](https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/) · NVIDIA Technical Blog · 09-28
- [Inside NVIDIA Sentry: Secure AI Agents at Runtime](https://developer.nvidia.com/blog/inside-nvidia-sentry-secure-ai-agents-at-runtime/) · NVIDIA Technical Blog · 10-21
- [How NVIDIA OpenShell Reference Architecture Secures and Governs AI Agent Workloads at Scale](https://developer.nvidia.com/blog/how-nvidia-openshell-reference-architecture-secures-and-governs-ai-agent-workloads-at-scale/) · NVIDIA Technical Blog · 10-21
- [How Vercel Agent accesses production safely](https://vercel.com/blog/how-vercel-agent-accesses-production-safely) · Vercel · 10-24
- [The end of credential sprawl for agents](https://vercel.com/blog/the-end-of-credential-sprawl-for-agents) · Vercel · 08-25
- [Your AI agent can move money in Stripe - here's how to stay in control](https://stripe.dev/blog/your-ai-agent-can-move-money-in-stripe) · Stripe · 10-21
- [Agent sprawl: How to manage agent proliferation in the enterprise Oct 15, 2026 5 min read](https://cohere.com/blog/agent-sprawl) · Cohere · 10-16
- [Architecting Governed, Self-Evolving AI Agents on Google Cloud](https://developers.googleblog.com/architecting-governed-self-evolving-ai-agents-on-gemini-agent-platform/) · Google · 10-22
- [Automating agentic AI Well-Architected reviews with the AWS Agentic AI Lens](https://aws.amazon.com/blogs/architecture/automating-agentic-ai-well-architected-reviews-with-the-aws-agentic-ai-lens/) · AWS Architecture · 10-29

## 6. 모델 냉정하게 평가하기와 '언제 AI를 쓰지 말지' (10개)

자체 벤치마크, 모델 교체 판단, 한계 분석

- ⭐ [리더보드 1등 LLM, 토스에서도 1등일까? - Toss Benchmark 구축기](https://toss.tech/article/toss-benchmark) · 토스 · 09-16
- ⭐ [채널톡이 글로벌 상담 Agent를 GPT-5.6 Luna로 갈아탄 이유](https://tech.channel.io/kr/articles/d1671db1) · 채널톡 · 08-24
- [[신청 마감] ​AI 제품을 만들 때, 자체 모델과 검색엔진은 언제 필요할까요?](https://tech.channel.io/kr/articles/2e5b1191) · 채널톡 · 09-28
- [A model guide for the GPT-6 family](https://openai.com/index/practical-guide-building-gpt-6) · OpenAI · 10-03
- [Beyond the model: Engineering AI infra with scientific judgement](https://medium.com/airbnb-engineering/beyond-the-model-engineering-ai-infra-with-scientific-judgement-371316d43261) · Airbnb · 09-16
- [What AI gets wrong and what failure teaches us](https://www.microsoft.com/en-us/research/podcast/what-ai-gets-wrong-and-what-failure-teaches-us/) · Microsoft Research · 10-07
- [How AI agents shape experts’ judgment calls](https://www.anthropic.com/research/agents-judgment-calls) · Anthropic Research · 10-27
- [BenchMIRT: What are LLM benchmarks actually measuring?](https://huggingface.co/blog/allenai/benchmirt) · Hugging Face · 09-02
- [State of Open Models: Summer 2026 Observations](https://huggingface.co/blog/state-of-open-models-summer-2026) · Hugging Face · 08-14
- [배달의민족 전자계약서 화면 개편기: AI에게 맡긴 것과 사람이 챙긴 것](https://techblog.woowahan.com/27604/) · 우아한형제들 · 09-18

## 7. RAG·파인튜닝·스펙 기반 개발·에이전틱 코딩 실무 (15개)

실제 제품·개발에 적용한 사례

- ⭐ [사내 지식으로 Agentic RAG 만들기 (2/3) : 검색을 얹기, LightRAG와 Navigator](https://techblog.gccompany.co.kr/%EC%82%AC%EB%82%B4-%EC%A7%80%EC%8B%9D%EC%9C%BC%EB%A1%9C-agentic-rag-%EB%A7%8C%EB%93%A4%EA%B8%B0-2-3-%EA%B2%80%EC%83%89%EC%9D%84-%EC%96%B9%EA%B8%B0-lightrag%EC%99%80-navigator-9f3119060242) · 여기어때 · 10-10
- ⭐ [사내 지식으로 Agentic RAG 만들기 (3/3) : 관측 가능한 RAG, 운영되는 도구로](https://techblog.gccompany.co.kr/%EC%82%AC%EB%82%B4-%EC%A7%80%EC%8B%9D%EC%9C%BC%EB%A1%9C-agentic-rag-%EB%A7%8C%EB%93%A4%EA%B8%B0-3-3-%EA%B4%80%EC%B8%A1-%EA%B0%80%EB%8A%A5%ED%95%9C-rag-%EC%9A%B4%EC%98%81%EB%90%98%EB%8A%94-%EB%8F%84%EA%B5%AC%EB%A1%9C-dbac813832db) · 여기어때 · 10-10
- [Prepare web content for Amazon Bedrock Knowledge Bases with Crawl4AI](https://aws.amazon.com/blogs/machine-learning/prepare-web-content-for-amazon-bedrock-knowledge-bases-with-crawl4ai/) · AWS Machine Learning · 11-03
- [측정할 수 없으면 개선할 수 없다 - AI Pick 추천 카드를 위한 sLLM 정렬 학습기](https://oliveyoung.tech/2026-09-18/oy_sllm_alignment/) · 올리브영 · 09-18
- [Fine-tuning LLMs for risk assessment](https://stripe.dev/blog/training-llms-for-risk-assessment) · Stripe · 10-09
- [Fine-tuning a 350M Model for Better Structured Outputs in 100 GRPO Steps](https://huggingface.co/blog/grpo-with-trl-ifstruct) · Hugging Face · 09-03
- [Async GRPO with LoRA across HF Jobs: a bucket, a proxy, and no NCCL](https://huggingface.co/blog/asyncgrpo-lora-hfjobs) · Hugging Face · 09-10
- ⭐ [How Dynata scaled AI across the development lifecycle with AI-DLC and Kiro IDE](https://aws.amazon.com/blogs/architecture/how-dynata-scaled-ai-across-the-development-lifecycle-with-ai-dlc-and-kiro-ide/) · AWS Architecture · 10-16
- [OpenAI에서 직접 알려주는 Codex 사용법](https://tech.channel.io/kr/articles/361daeef) · 채널톡 · 09-02
- [AI 코딩 시대, DDD가 더 필요해진 이유](https://blog.banksalad.com/tech/banksalad-ddd-in-ai-era/) · 뱅크샐러드 · 10-15
- [Unity를 모르는 프론트엔드 개발자가 AI로 Unity 서비스를 React로 옮긴 방법](https://tech.hancom.com/migrated-unity-to-react-with-ai/) · 한글과컴퓨터 · 08-26
- [Asana completed a years-long code migration in 2 weeks with Codex](https://openai.com/index/asana) · OpenAI · 08-18
- [Build a repeatable PHP-to-Java migration engine with Kiro](https://aws.amazon.com/blogs/machine-learning/build-a-repeatable-php-to-java-migration-engine-with-kiro/) · AWS Machine Learning · 10-30
- [Modernizing complex legacy code with AI agents.](https://mistral.ai/news/legacy-code-modernization/) · Mistral AI · 09-09
- [We gave AI agents a mobile dev environment](https://shopify.engineering/remote-dev) · Shopify · 10-22
