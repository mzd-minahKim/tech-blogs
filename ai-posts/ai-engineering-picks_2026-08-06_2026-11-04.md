# AI 엔지니어링 실무 글 모음 (2026-08-06 ~ 2026-11-04)

국내외 기술 블로그 86곳에서 3개월 동안 올라온 AI 글 730개 중, 사내 업무를 AI로 바꾸는 일(AX)과 에이전트 개발·운영에 바로 참고할 만한 140개를 주제별로 골랐습니다. ⭐는 먼저 읽어볼 만한 글입니다.

- 전체 목록: [AI 관련 글 모음](2026-08-06_2026-11-04.md)
- Microsoft의 'AX'는 Agent Experience(에이전트가 쓰기 좋은 도구 설계)를 뜻합니다.

## ⭐ 먼저 읽을 글

- [손가락 튕기기로 LLM 비용 줄이기](https://toss.tech/article/snap-llm-cost-reduction) · 토스
- [모델만 바꿨는데 LLM 비용이 3배가 된 이유](https://medium.com/daangn/%EB%AA%A8%EB%8D%B8%EB%A7%8C-%EB%B0%94%EA%BF%A8%EB%8A%94%EB%8D%B0-llm-%EB%B9%84%EC%9A%A9%EC%9D%B4-3%EB%B0%B0%EA%B0%80-%EB%90%9C-%EC%9D%B4%EC%9C%A0-5ae60ab5108b) · 당근마켓
- [Spotify의 Portal로 Claude Code 토큰 사용량 90% 줄이기](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90/) <sub>Portal by Spotify cut my Claude Code token usage by 90%</sub> · Spotify
- [Gisting: LLM 에이전트 컨텍스트를 압축해 처리량은 높이고 비용은 낮추기](https://shopify.engineering/gisting) <sub>Gisting: Compressing LLM Agent context to ↑ throughput and ↓ cost</sub> · Shopify
- [개인 AI 활용의 다음 단계는 무엇인가 - LY Corporation에서 AIDD 워크숍을 통해 살펴본 AIDD 조직 도입의 조건](https://techblog.lycorp.co.jp/ko/conditions-for-organizational-aidd-adoption) · LINE (LY Corporation)
- [AI Native 조직은 도메인 지식을 어떻게 공유하는가](https://techblog.musinsa.com/ai-native-%EC%A1%B0%EC%A7%81%EC%9D%80-%EB%8F%84%EB%A9%94%EC%9D%B8-%EC%A7%80%EC%8B%9D%EC%9D%84-%EC%96%B4%EB%96%BB%EA%B2%8C-%EA%B3%B5%EC%9C%A0%ED%95%98%EB%8A%94%EA%B0%80-f2e3de607df3) · 무신사 (29CM 통합)
- [팀이 신뢰할 수 있는 AI 분석 환경 만들기: 추천팀의 컨텍스트 설계](https://tech.kakao.com/posts/844) · 카카오
- [데이터 분석 에이전트를 만들며 배운 컨텍스트 설계](https://tech.kakao.com/posts/838) · 카카오
- [Thin Orchestrator: 라우터 일을 줄여 AI 에이전트를 더 안정적으로 만든 방법](https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/) <sub>The Thin Orchestrator: How We Made Our AI Agents More Reliable by Giving the Router Less to Do</sub> · Meta (Facebook)
- [머릿속에 있던 로그 정의 기준을 모두의 AI 스킬로 만들기](https://toss.tech/article/dataops-log-definition-skill) · 토스
- [나는 하네스 깎는 노인이 되었다 시리즈 2: 안녕, 실버불릿](https://meetup.nhncloud.com/posts/426) · NHN Cloud Meetup (구 TOAST Meetup)
- [같은 LLM인데 왜 결과가 다를까? 답은 하네스에 있다.](https://tech.hancom.com/harness-engineering/) · 한글과컴퓨터
- [Flava MCP Hub가 걸어온 길: AI 시대를 위한 배관 공사](https://techblog.lycorp.co.jp/ko/flava-mcp-hub-ai-infrastructure) · LINE (LY Corporation)
- [MCP Gateway 설계: Uber의 MCP 관리 플랫폼](https://www.uber.com/us/en/blog/designing-mcp-gateway) <sub>Designing MCP Gateway: Uber's MCP Management Platform</sub> · Uber
- [PayPal이 전사 규모로 에이전트 스킬을 관리하는 방법](https://developer.paypal.com/community/blog/agent_skills_at_enterprise_scale) <sub>How PayPal is governing agent skills at enterprise scale</sub> · PayPal
- [도구 호출부터 작업 완료까지, AI 에이전트 평가하는 법](https://developer.nvidia.com/blog/how-to-evaluate-ai-agents-from-tool-calls-to-task-completion/) <sub>How to Evaluate AI Agents From Tool Calls to Task Completion</sub> · NVIDIA Technical Blog
- [NVIDIA NeMo Relay로 에이전트 하네스 동작 추적하기](https://developer.nvidia.com/blog/tracing-agent-harness-behavior-with-nvidia-nemo-relay/) <sub>Tracing Agent Harness Behavior with NVIDIA NeMo Relay</sub> · NVIDIA Technical Blog
- [AI 에이전트 평가: 감으로 보는 단계에서 벗어나기](https://developers.googleblog.com/evaluating-ai-agents-moving-past-the-vibe-check/) <sub>Evaluating AI agents: moving past the vibe check</sub> · Google
- [Agents CLI 평가로 에이전트 품질을 점진적으로 끌어올리기](https://developers.googleblog.com/hill-climbing-agent-quality-with-agents-cli-evaluation/) <sub>Hill-Climbing Agent Quality with Agents CLI Evaluation</sub> · Google
- [리더보드 1등 LLM, 토스에서도 1등일까? - Toss Benchmark 구축기](https://toss.tech/article/toss-benchmark) · 토스
- [채널톡이 글로벌 상담 Agent를 GPT-5.6 Luna로 갈아탄 이유](https://tech.channel.io/kr/articles/d1671db1) · 채널톡
- [사내 지식으로 Agentic RAG 만들기 (2/3) : 검색을 얹기, LightRAG와 Navigator](https://techblog.gccompany.co.kr/%EC%82%AC%EB%82%B4-%EC%A7%80%EC%8B%9D%EC%9C%BC%EB%A1%9C-agentic-rag-%EB%A7%8C%EB%93%A4%EA%B8%B0-2-3-%EA%B2%80%EC%83%89%EC%9D%84-%EC%96%B9%EA%B8%B0-lightrag%EC%99%80-navigator-9f3119060242) · 여기어때
- [사내 지식으로 Agentic RAG 만들기 (3/3) : 관측 가능한 RAG, 운영되는 도구로](https://techblog.gccompany.co.kr/%EC%82%AC%EB%82%B4-%EC%A7%80%EC%8B%9D%EC%9C%BC%EB%A1%9C-agentic-rag-%EB%A7%8C%EB%93%A4%EA%B8%B0-3-3-%EA%B4%80%EC%B8%A1-%EA%B0%80%EB%8A%A5%ED%95%9C-rag-%EC%9A%B4%EC%98%81%EB%90%98%EB%8A%94-%EB%8F%84%EA%B5%AC%EB%A1%9C-dbac813832db) · 여기어때
- [Dynata가 AI-DLC와 Kiro IDE로 개발 전 과정에 AI를 확장한 방법](https://aws.amazon.com/blogs/architecture/how-dynata-scaled-ai-across-the-development-lifecycle-with-ai-dlc-and-kiro-ide/) <sub>How Dynata scaled AI across the development lifecycle with AI-DLC and Kiro IDE</sub> · AWS Architecture

## 1. 토큰·비용 절감 (19개)

LLM 비용, 캐싱, 컨텍스트 압축, 모델 라우팅

- ⭐ [손가락 튕기기로 LLM 비용 줄이기](https://toss.tech/article/snap-llm-cost-reduction) · 토스 · 10-27
- ⭐ [모델만 바꿨는데 LLM 비용이 3배가 된 이유](https://medium.com/daangn/%EB%AA%A8%EB%8D%B8%EB%A7%8C-%EB%B0%94%EA%BF%A8%EB%8A%94%EB%8D%B0-llm-%EB%B9%84%EC%9A%A9%EC%9D%B4-3%EB%B0%B0%EA%B0%80-%EB%90%9C-%EC%9D%B4%EC%9C%A0-5ae60ab5108b) · 당근마켓 · 10-21
- ⭐ [Spotify의 Portal로 Claude Code 토큰 사용량 90% 줄이기](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90/) <sub>Portal by Spotify cut my Claude Code token usage by 90%</sub> · Spotify · 09-04
- ⭐ [Gisting: LLM 에이전트 컨텍스트를 압축해 처리량은 높이고 비용은 낮추기](https://shopify.engineering/gisting) <sub>Gisting: Compressing LLM Agent context to ↑ throughput and ↓ cost</sub> · Shopify · 08-19
- [Coinbase가 Code Connect로 에이전트를 안내하고 토큰 비용을 줄인 방법](https://www.figma.com/blog/how-coinbase-used-code-connect-to-shrink-token-costs/) <sub>How Coinbase used Code Connect to guide agents and shrink token costs</sub> · Figma · 09-03
- [코딩 에이전트 팀을 키우며 배운 것: 비용 30%로 최상위 성능 내기](https://cohere.com/blog/lessons-from-scaling-teams-of-frontier-coding-agents) <sub>Lessons from scaling teams of coding agents: reach the frontier at 30% of the cost</sub> · Cohere · 10-15
- [작업당 비용: 저렴한 분류기로 Gemini 모델과 사고 수준 라우팅하기](https://developers.googleblog.com/cost-per-task-using-cheap-classifiers-to-route-across-gemini-models-and-thinking-levels/) <sub>Cost per task: Using cheap classifiers to route across Gemini models and thinking levels</sub> · Google · 11-03
- [Tailscale이 AI Gateway 위에 고객용 모델 라우터를 만든 방법](https://vercel.com/blog/how-tailscale-built-a-customer-facing-model-router-on-ai-gateway) <sub>How Tailscale built a customer-facing model router on AI Gateway</sub> · Vercel · 09-11
- [사내 LLM 요청을 한곳으로 모은 AI Gateway 구축기](https://tech.inflab.com/20260825-ai-gateway/) · 인프랩 (인프런) · 09-09
- [GPT-6의 개선된 프롬프트 캐싱](https://openai.com/index/better-prompt-caching-for-gpt-6) <sub>Better prompt caching for GPT-6</sub> · OpenAI · 09-23
- [Asana, GPT-6.1 Sol로 브라우저 테스트 모델 비용 76배 절감](https://openai.com/index/asana-browser-agent) <sub>Asana cuts model costs 76x in browser tests with GPT-6.1 Sol</sub> · OpenAI · 10-09
- [LegalOn, 개발 속도는 유지하며 Codex 비용 절반으로](https://openai.com/index/legalon-halves-codex-costs) <sub>LegalOn halves Codex costs while maintaining development speed</sub> · OpenAI · 10-08
- [V7, GPT-5.6 Luna로 비용 78% 줄이고 정확도는 높여](https://openai.com/index/v7) <sub>V7 cuts costs 78% while boosting accuracy with GPT-5.6 Luna</sub> · OpenAI · 09-21
- [Amazon Bedrock 비용 끝까지 관리하기: FinOps·플랫폼 팀을 위한 플레이북](https://aws.amazon.com/blogs/machine-learning/managing-amazon-bedrock-costs-end-to-end-a-playbook-for-finops-and-platform-teams/) <sub>Managing Amazon Bedrock costs end to end: A playbook for FinOps and platform teams</sub> · AWS Machine Learning · 10-31
- [집요한 최적화로 추론 비용 68% 줄이기](https://blog.cloudflare.com/obsessive-inference-optimization/) <sub>Cutting our inference bill by 68% by being obsessive about optimization</sub> · Cloudflare · 10-20
- [SLM 어휘를 특화해 실제 서비스 추론 비용 77% 줄이기](https://huggingface.co/blog/Dharma-AI/vocabx-vocabulary-specialization) <sub>How Specializing the Vocabulary of SLMs Can Cut Inference Cost by 77% in Real Applications</sub> · Hugging Face · 10-22
- [ACE를 생각 중이라면? 더 적은 토큰으로 할 수 있습니다](https://huggingface.co/blog/ibm-research/altk-evolve-sldd) <sub>Thinking of ACE? We Can Do It with Fewer Tokens</sub> · Hugging Face · 08-11
- [스스로 컨텍스트를 압축하는 언어 모델 에이전트](https://machinelearning.apple.com/research/self-compacting-language-agents) <sub>Self-Compacting Language Model Agents</sub> · Apple Machine Learning Research · 10-12
- [에이전트에 메모리가 실제로 얼마나 필요할까?](https://huggingface.co/blog/ibm-research/altk-evolve-hmm) <sub>How Much Memory Does Your Agent Actually Need?</sub> · Hugging Face · 08-19

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
- [AI 팀이 되어 가기](https://medium.com/pinterest-engineering/becoming-an-ai-team-866d6b567803) <sub>Becoming an AI Team</sub> · Pinterest · 09-02
- [Dropbox CTO가 말하는 AI 도입에서 전환으로 넘어가기](https://dropbox.tech/culture/learnings-from-deploying-ai-at-company-scale) <sub>Dropbox CTO Ali Dasdan on moving from AI adoption to transformation</sub> · Dropbox · 09-23
- [AI가 바꾼 Spotify의 개발 방식: 빨라진 속도에서 품질에 대해 배우고 고친 것](https://engineering.atspotify.com/2026/9/ai-changed-how-spotify-builds-what-we-learned-and-fixed-about-quality-at-higher-velocity/) <sub>AI Changed How Spotify Builds. What We Learned (and Fixed) About Quality at Higher Velocity</sub> · Spotify · 09-17
- [AI 도입을 이끄는 팀 습관 4가지](https://www.figma.com/blog/4-team-rituals-that-drive-ai-adoption/) <sub>4 team rituals that drive AI adoption</sub> · Figma · 10-10
- [디자인에 AI가 준 영향, 실제로 어떻게 측정할까?](https://www.figma.com/blog/measuring-the-impact-of-ai/) <sub>How do you actually measure the impact of AI on design?</sub> · Figma · 08-29
- [AI 사용량을 비즈니스 가치와 연결하는 법](https://openai.com/index/how-to-connect-ai-usage-to-business-value) <sub>How to connect AI usage to business value</sub> · OpenAI · 09-16
- [AI ROI: 기업이 AI 투자 수익을 측정하는 법](https://cohere.com/blog/ai-roi) <sub>AI ROI: How enterprises can measure the return on AI investments</sub> · Cohere · 10-15
- [AI 네이티브 기업은 워크플로를 어떻게 운영 역량으로 바꾸나](https://openai.com/index/ai-native-company-workflows) <sub>How AI-native companies turn workflows into operating capability</sub> · OpenAI · 09-02
- [보조에서 실행으로: 기업이 AI를 실무에 투입하는 방식](https://openai.com/index/how-enterprises-put-ai-to-work) <sub>From assistance to execution: How enterprises put AI to work</sub> · OpenAI · 08-12
- [RingCentral이 개발부터 운영까지 AI 네이티브로 일하는 방법](https://openai.com/index/ringcentral) <sub>How RingCentral builds AI-native work from engineering to ops</sub> · OpenAI · 08-12
- [에이전트 경험(AX)이란?](https://devblogs.microsoft.com/blog/what-is-agent-experience-ax/) <sub>What is Agent Experience (AX)?</sub> · Microsoft · 10-06
- [에이전트 경험(AX) 실무자 플레이북 공개](https://devblogs.microsoft.com/blog/introducing-the-agent-experience-ax-practitioner-playbook/) <sub>Introducing the Agent Experience (AX) Practitioner Playbook</sub> · Microsoft · 10-09

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
- [OpenAI가 Ultrafast로 장애 조사 시간을 몇 시간에서 몇 분으로 줄인 방법](https://openai.com/index/openai-cut-incident-investigation) <sub>How Ultrafast cut incident investigation from hours to minutes at OpenAI</sub> · OpenAI · 10-26
- [Circle K가 Amazon Bedrock으로 DevOps 장애 분류를 15분 이내로 단축한 방법](https://aws.amazon.com/blogs/machine-learning/how-circle-k-accelerated-devops-incident-triage-to-under-15-minutes-with-amazon-bedrock/) <sub>How Circle K accelerated DevOps incident triage to under 15 minutes with Amazon Bedrock</sub> · AWS Machine Learning · 11-03
- [Pensive AI로 장애 진단을 믿을 수 있게 만들기](https://netflixtechblog.com/making-failure-diagnosis-reliable-with-pensive-ai-6b0811a1c015) <sub>Making Failure Diagnosis Reliable with Pensive AI</sub> · Netflix · 10-27
- [QA 에이전트: AI 기반 자율 테스트로 소프트웨어 품질 다시 설계하기](https://www.linkedin.com/blog/engineering/ai/qa-agent-reimagining-software-quality-with-ai-driven-autonomous-testing) <sub>Quality Assurance Agent: Reimagining Software Quality with AI-Driven Autonomous ...</sub> · LinkedIn
- [코드베이스에 맞춰 적응하는, 신호 높은 대규모 AI 코드 리뷰](https://www.linkedin.com/blog/engineering/ai/high-signal-ai-code-review-that-adapts-to-your-codebase-at-scale) <sub>High-Signal AI Code Review That Adapts to Your Codebase at Scale</sub> · LinkedIn
- [법무에 AI 확장하기: Uber의 계약서 수정(레드라이닝) 에이전트 만들기](https://www.uber.com/us/en/blog/building-ubers-redlining-agent) <sub>Scaling AI in Legal: Building Uber’s Redlining Agent</sub> · Uber
- [Metrics Board: 에이전트가 쓸 수 있는 지표 레이어 만들기](https://medium.com/pinterest-engineering/metrics-board-building-an-agent-ready-metrics-layer-2c8fefe68756) <sub>Metrics Board: Building an Agent-ready Metrics Layer</sub> · Pinterest · 10-07
- [믿을 수 있는 데이터 분석 에이전트 만들기: KDD Cup에서 배운 것](https://developer.nvidia.com/blog/building-reliable-data-analytics-agents-lessons-from-the-kdd-cup/) <sub>Building Reliable Data Analytics Agents: Lessons from the KDD Cup</sub> · NVIDIA Technical Blog · 10-09
- ⭐ [Thin Orchestrator: 라우터 일을 줄여 AI 에이전트를 더 안정적으로 만든 방법](https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/) <sub>The Thin Orchestrator: How We Made Our AI Agents More Reliable by Giving the Router Less to Do</sub> · Meta (Facebook) · 10-20
- [Stripe의 Payment Method Factory: 반복되는 맞춤 연동을 에이전트로 처리하기](https://stripe.dev/blog/stripes-payment-method-factory-orchestrating-agents-for-repeated-custom-integrations) <sub>Stripe’s Payment Method Factory: Orchestrating agents for repeated, custom integrations</sub> · Stripe · 09-30
- [Harbor: Stripe의 AI 기반 프로토타이핑 도구](https://stripe.dev/blog/harbor-stripes-ai-assisted-prototyping-tool) <sub>Harbor: Stripe’s AI-assisted prototyping tool</sub> · Stripe · 09-14
- [AI가 SDK를 짠 건 아니다. 만드는 방식을 바꿨을 뿐](https://stripe.dev/blog/ai-didnt-write-our-sdk-it-changed-how-we-built-it) <sub>AI didn't write our SDK. It changed how we built it.</sub> · Stripe · 08-28
- [AI SDK를 위한 소프트웨어 공장 만들기](https://vercel.com/blog/building-a-software-factory-for-ai-sdk) <sub>Building a software factory for AI SDK</sub> · Vercel · 08-12

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
- ⭐ [MCP Gateway 설계: Uber의 MCP 관리 플랫폼](https://www.uber.com/us/en/blog/designing-mcp-gateway) <sub>Designing MCP Gateway: Uber's MCP Management Platform</sub> · Uber
- [PayPal MCP Gateway를 만들며 배운 것](https://developer.paypal.com/community/blog/PayPal_MCP_Gateway) <sub>What We Learned Building PayPal's MCP Gateway</sub> · PayPal
- [Jira 기능을 필요할 때 깊이 있게: 엔드포인트가 아닌 작업 중심으로 MCP 서버 설계하기](https://www.atlassian.com/blog/how-we-build/jira-depth-on-demand) <sub>Jira’s depth, on demand: designing an MCP server around jobs, not endpoints</sub> · Atlassian · 10-29
- [블로그 발행 MCP를 직접 만들며 확인한 AI 에이전트 실무 원칙 - 구성요소부터 사람 승인까지](http://devocean.sk.com/blog/techBoardDetail.do?id=168583&boardType=techBlog&isShared=Y) · SK텔레콤 DEVOCEAN · 10-29
- [국내 최초 광고 MCP를 출시하며, 개발자의 역할은 어디까지 넓어졌을까?](https://medium.com/daangn/%EA%B5%AD%EB%82%B4-%EC%B5%9C%EC%B4%88-%EA%B4%91%EA%B3%A0-mcp%EB%A5%BC-%EC%B6%9C%EC%8B%9C%ED%95%98%EB%A9%B0-%EA%B0%9C%EB%B0%9C%EC%9E%90%EC%9D%98-%EC%97%AD%ED%95%A0%EC%9D%80-%EC%96%B4%EB%94%94%EA%B9%8C%EC%A7%80-%EB%84%93%EC%96%B4%EC%A1%8C%EC%9D%84%EA%B9%8C-8dea7fe41c07) · 당근마켓 · 11-03
- ⭐ [PayPal이 전사 규모로 에이전트 스킬을 관리하는 방법](https://developer.paypal.com/community/blog/agent_skills_at_enterprise_scale) <sub>How PayPal is governing agent skills at enterprise scale</sub> · PayPal
- [에이전트 스킬 현황](https://vercel.com/blog/state-of-agent-skills) <sub>State of agent skills</sub> · Vercel · 09-25
- [GitHub Copilot 플러그인으로 일관된 AI 지원 개발 환경 만들기](https://devblogs.microsoft.com/blog/enabling-consistent-ai-assisted-engineering-with-github-copilot-plugins/) <sub>Enabling Consistent AI-Assisted Engineering with GitHub Copilot Plugins</sub> · Microsoft · 09-30
- [design.md로 에이전트가 브랜드에 맞는 페이지를 만드는 방법](https://vercel.com/blog/how-our-agents-build-on-brand-pages-with-design-md) <sub>How our agents build on-brand pages with design.md</sub> · Vercel · 08-31
- [LLM Wiki: 코드 기준으로 자동 최신화되는 도메인 지식 SSOT 만들기](https://techblog.lycorp.co.jp/ko/llm-wiki-code-driven-knowledge-ssot) · LINE (LY Corporation) · 08-28
- [코딩 에이전트에게 직접 소유하는 메모리 주기](https://huggingface.co/blog/funes) <sub>Give Your Coding Agents a Memory You Own</sub> · Hugging Face · 09-03
- [사실만이 아니라 출처까지 맞히기: MCP 에이전트를 위한 출처 기반 검증](https://huggingface.co/blog/MultiverseComputingCAI/getting-the-source-right-not-just-the-fact-source) <sub>Getting the Source Right, Not Just the Fact: Source-Aware Verification for MCP Agents</sub> · Hugging Face · 09-29
- [계획이 먼저냐 검색이 먼저냐? 도구 탐색 구조의 대규모 비교 연구](https://machinelearning.apple.com/research/plan-retrieve-tool-discovery) <sub>Plan or Retrieve First? A Scale Study of Tool Discovery Architectures</sub> · Apple Machine Learning Research · 10-15
- [AI에게 문서를 더 주지 말고 API를 주세요](https://developer.paypal.com/community/blog/stopgivingaimoredocumentation) <sub>Stop Giving AI More Documentation. Give It an API.</sub> · PayPal

## 5. 평가(Eval)·트레이스·가드레일·거버넌스 (25개)

Eval-driven 개발, 실행 트레이스 진단, 런타임 통제

- [Jev로 AI 글 냄새 잡기 - 판정 모델을 교정 파이프라인 세 곳에 붙인 기록](http://devocean.sk.com/blog/techBoardDetail.do?id=168525&boardType=techBlog&isShared=Y) · SK텔레콤 DEVOCEAN · 09-29
- ⭐ [도구 호출부터 작업 완료까지, AI 에이전트 평가하는 법](https://developer.nvidia.com/blog/how-to-evaluate-ai-agents-from-tool-calls-to-task-completion/) <sub>How to Evaluate AI Agents From Tool Calls to Task Completion</sub> · NVIDIA Technical Blog · 09-22
- ⭐ [NVIDIA NeMo Relay로 에이전트 하네스 동작 추적하기](https://developer.nvidia.com/blog/tracing-agent-harness-behavior-with-nvidia-nemo-relay/) <sub>Tracing Agent Harness Behavior with NVIDIA NeMo Relay</sub> · NVIDIA Technical Blog · 10-01
- ⭐ [AI 에이전트 평가: 감으로 보는 단계에서 벗어나기](https://developers.googleblog.com/evaluating-ai-agents-moving-past-the-vibe-check/) <sub>Evaluating AI agents: moving past the vibe check</sub> · Google · 10-15
- ⭐ [Agents CLI 평가로 에이전트 품질을 점진적으로 끌어올리기](https://developers.googleblog.com/hill-climbing-agent-quality-with-agents-cli-evaluation/) <sub>Hill-Climbing Agent Quality with Agents CLI Evaluation</sub> · Google · 10-28
- [작업 경로에 'eval'이 있으면 에이전트 행동이 달라질까?](https://devblogs.microsoft.com/blog/does-eval-in-the-workspace-path-change-what-your-agent-does/) <sub>Does ‘eval’ in the workspace path change what your agent does?</sub> · Microsoft · 10-30
- [에이전트 eval에서 로컬 git 원격이 GitHub를 대신할 수 있을까?](https://devblogs.microsoft.com/blog/can-a-local-git-remote-replace-github-in-your-agent-eval/) <sub>Can a local git remote replace GitHub in your agent eval?</sub> · Microsoft · 10-20
- [Run SDK 공개: 에이전트를 위한 안전한 eval 환경](https://vercel.com/blog/introducing-run) <sub>Introducing Run SDK: secure eval for your agents</sub> · Vercel · 08-25
- [Ora가 Vercel에서 주요 AI 에이전트를 모두 벤치마크하는 방법](https://vercel.com/blog/how-ora-benchmarks-every-major-ai-agent-on-vercel) <sub>How Ora benchmarks every major AI agent on Vercel</sub> · Vercel · 08-22
- [에이전트가 작업을 해냈다. 다음에도 해낼까?](https://huggingface.co/blog/ibm-research/altk-evolve-consistency) <sub>Your Agent Aced the Task. Will It Do It Again?</sub> · Hugging Face · 09-16
- [에이전트는 끝났다고 했다. 데이터베이스는 아니라고 했다.](https://huggingface.co/blog/microsoft/thinkingbox) <sub>The Agent Said It Was Done. The Database Disagreed.</sub> · Hugging Face · 10-04
- [Grab Bench: Grab의 실제 업무로 AI 평가하기](https://engineering.grab.com/grab-bench-evaluating-ai) <sub>Grab Bench: Evaluating AI on Grab-shaped production work</sub> · Grab · 08-12
- [ShopGym: 쇼핑 에이전트를 위한 현실적이고 재현 가능한 샌드박스](https://shopify.engineering/shopgym) <sub>ShopGym: Realistic, reproducible sandboxes for shopping agents</sub> · Shopify · 10-02
- [에이전트, 무작위성, 그리고 증거: trivago QA 밋업 정리](https://tech.trivago.com/post/2026-08-12-agents-randomness-and-receipts-notes-from-trivagos-qa-meetup/) <sub>Agents, Randomness, and Receipts: Notes from trivago's QA Meetup</sub> · Trivago · 08-12
- [합성 기업 데이터 평가에서 실제 Microsoft Copilot에 대한 신뢰까지](https://www.microsoft.com/en-us/research/blog/from-synthetic-enterprise-data-evaluations-to-real-microsoft-copilot-ai-confidence/) <sub>From synthetic enterprise data evaluations to real Microsoft Copilot AI confidence</sub> · Microsoft Research · 10-30
- [평가와 사내 사용에서 나온 모델의 의도치 않은 행동 조사](https://www.anthropic.com/research/investigating-unintended-model-actions) <sub>Investigating unintended model actions in our evaluations and internal use</sub> · Anthropic Research · 10-09
- [NVIDIA OpenShell로 AI 에이전트에 런타임 통제 추가하기](https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/) <sub>Add Runtime Controls to AI Agents with NVIDIA OpenShell</sub> · NVIDIA Technical Blog · 09-28
- [NVIDIA Sentry 들여다보기: 실행 중인 AI 에이전트 보호하기](https://developer.nvidia.com/blog/inside-nvidia-sentry-secure-ai-agents-at-runtime/) <sub>Inside NVIDIA Sentry: Secure AI Agents at Runtime</sub> · NVIDIA Technical Blog · 10-21
- [NVIDIA OpenShell 참조 아키텍처로 대규모 AI 에이전트 작업 보호·관리하기](https://developer.nvidia.com/blog/how-nvidia-openshell-reference-architecture-secures-and-governs-ai-agent-workloads-at-scale/) <sub>How NVIDIA OpenShell Reference Architecture Secures and Governs AI Agent Workloads at Scale</sub> · NVIDIA Technical Blog · 10-21
- [Vercel Agent가 운영 환경에 안전하게 접근하는 방법](https://vercel.com/blog/how-vercel-agent-accesses-production-safely) <sub>How Vercel Agent accesses production safely</sub> · Vercel · 10-24
- [에이전트용 자격 증명이 여기저기 흩어지는 문제의 끝](https://vercel.com/blog/the-end-of-credential-sprawl-for-agents) <sub>The end of credential sprawl for agents</sub> · Vercel · 08-25
- [AI 에이전트가 Stripe에서 돈을 움직일 수 있다면, 통제권을 지키는 법](https://stripe.dev/blog/your-ai-agent-can-move-money-in-stripe) <sub>Your AI agent can move money in Stripe - here's how to stay in control</sub> · Stripe · 10-21
- [에이전트 난립: 기업에서 늘어나는 에이전트 관리하기](https://cohere.com/blog/agent-sprawl) <sub>Agent sprawl: How to manage agent proliferation in the enterprise</sub> · Cohere · 10-16
- [Google Cloud에서 통제 가능하고 스스로 발전하는 AI 에이전트 설계하기](https://developers.googleblog.com/architecting-governed-self-evolving-ai-agents-on-gemini-agent-platform/) <sub>Architecting Governed, Self-Evolving AI Agents on Google Cloud</sub> · Google · 10-22
- [AWS Agentic AI Lens로 에이전틱 AI Well-Architected 리뷰 자동화하기](https://aws.amazon.com/blogs/architecture/automating-agentic-ai-well-architected-reviews-with-the-aws-agentic-ai-lens/) <sub>Automating agentic AI Well-Architected reviews with the AWS Agentic AI Lens</sub> · AWS Architecture · 10-29

## 6. 모델 냉정하게 평가하기와 '언제 AI를 쓰지 말지' (10개)

자체 벤치마크, 모델 교체 판단, 한계 분석

- ⭐ [리더보드 1등 LLM, 토스에서도 1등일까? - Toss Benchmark 구축기](https://toss.tech/article/toss-benchmark) · 토스 · 09-16
- ⭐ [채널톡이 글로벌 상담 Agent를 GPT-5.6 Luna로 갈아탄 이유](https://tech.channel.io/kr/articles/d1671db1) · 채널톡 · 08-24
- [[신청 마감] ​AI 제품을 만들 때, 자체 모델과 검색엔진은 언제 필요할까요?](https://tech.channel.io/kr/articles/2e5b1191) · 채널톡 · 09-28
- [GPT-6 모델군 선택 가이드](https://openai.com/index/practical-guide-building-gpt-6) <sub>A model guide for the GPT-6 family</sub> · OpenAI · 10-03
- [모델 너머: 과학적 판단으로 AI 인프라 설계하기](https://medium.com/airbnb-engineering/beyond-the-model-engineering-ai-infra-with-scientific-judgement-371316d43261) <sub>Beyond the model: Engineering AI infra with scientific judgement</sub> · Airbnb · 09-16
- [AI가 틀리는 것들, 그리고 실패가 알려주는 것](https://www.microsoft.com/en-us/research/podcast/what-ai-gets-wrong-and-what-failure-teaches-us/) <sub>What AI gets wrong and what failure teaches us</sub> · Microsoft Research · 10-07
- [AI 에이전트가 전문가의 판단에 미치는 영향](https://www.anthropic.com/research/agents-judgment-calls) <sub>How AI agents shape experts’ judgment calls</sub> · Anthropic Research · 10-27
- [BenchMIRT: LLM 벤치마크는 실제로 무엇을 측정하나?](https://huggingface.co/blog/allenai/benchmirt) <sub>BenchMIRT: What are LLM benchmarks actually measuring?</sub> · Hugging Face · 09-02
- [오픈 모델 현황: 2026년 여름 관찰](https://huggingface.co/blog/state-of-open-models-summer-2026) <sub>State of Open Models: Summer 2026 Observations</sub> · Hugging Face · 08-14
- [배달의민족 전자계약서 화면 개편기: AI에게 맡긴 것과 사람이 챙긴 것](https://techblog.woowahan.com/27604/) · 우아한형제들 · 09-18

## 7. RAG·파인튜닝·스펙 기반 개발·에이전틱 코딩 실무 (15개)

실제 제품·개발에 적용한 사례

- ⭐ [사내 지식으로 Agentic RAG 만들기 (2/3) : 검색을 얹기, LightRAG와 Navigator](https://techblog.gccompany.co.kr/%EC%82%AC%EB%82%B4-%EC%A7%80%EC%8B%9D%EC%9C%BC%EB%A1%9C-agentic-rag-%EB%A7%8C%EB%93%A4%EA%B8%B0-2-3-%EA%B2%80%EC%83%89%EC%9D%84-%EC%96%B9%EA%B8%B0-lightrag%EC%99%80-navigator-9f3119060242) · 여기어때 · 10-10
- ⭐ [사내 지식으로 Agentic RAG 만들기 (3/3) : 관측 가능한 RAG, 운영되는 도구로](https://techblog.gccompany.co.kr/%EC%82%AC%EB%82%B4-%EC%A7%80%EC%8B%9D%EC%9C%BC%EB%A1%9C-agentic-rag-%EB%A7%8C%EB%93%A4%EA%B8%B0-3-3-%EA%B4%80%EC%B8%A1-%EA%B0%80%EB%8A%A5%ED%95%9C-rag-%EC%9A%B4%EC%98%81%EB%90%98%EB%8A%94-%EB%8F%84%EA%B5%AC%EB%A1%9C-dbac813832db) · 여기어때 · 10-10
- [Crawl4AI로 Amazon Bedrock Knowledge Bases용 웹 콘텐츠 준비하기](https://aws.amazon.com/blogs/machine-learning/prepare-web-content-for-amazon-bedrock-knowledge-bases-with-crawl4ai/) <sub>Prepare web content for Amazon Bedrock Knowledge Bases with Crawl4AI</sub> · AWS Machine Learning · 11-03
- [측정할 수 없으면 개선할 수 없다 - AI Pick 추천 카드를 위한 sLLM 정렬 학습기](https://oliveyoung.tech/2026-09-18/oy_sllm_alignment/) · 올리브영 · 09-18
- [리스크 평가를 위한 LLM 파인튜닝](https://stripe.dev/blog/training-llms-for-risk-assessment) <sub>Fine-tuning LLMs for risk assessment</sub> · Stripe · 10-09
- [GRPO 100스텝으로 350M 모델의 구조화 출력 개선하기](https://huggingface.co/blog/grpo-with-trl-ifstruct) <sub>Fine-tuning a 350M Model for Better Structured Outputs in 100 GRPO Steps</sub> · Hugging Face · 09-03
- [HF Jobs에서 LoRA로 비동기 GRPO 돌리기: 버킷 하나, 프록시 하나, NCCL 없이](https://huggingface.co/blog/asyncgrpo-lora-hfjobs) <sub>Async GRPO with LoRA across HF Jobs: a bucket, a proxy, and no NCCL</sub> · Hugging Face · 09-10
- ⭐ [Dynata가 AI-DLC와 Kiro IDE로 개발 전 과정에 AI를 확장한 방법](https://aws.amazon.com/blogs/architecture/how-dynata-scaled-ai-across-the-development-lifecycle-with-ai-dlc-and-kiro-ide/) <sub>How Dynata scaled AI across the development lifecycle with AI-DLC and Kiro IDE</sub> · AWS Architecture · 10-16
- [OpenAI에서 직접 알려주는 Codex 사용법](https://tech.channel.io/kr/articles/361daeef) · 채널톡 · 09-02
- [AI 코딩 시대, DDD가 더 필요해진 이유](https://blog.banksalad.com/tech/banksalad-ddd-in-ai-era/) · 뱅크샐러드 · 10-15
- [Unity를 모르는 프론트엔드 개발자가 AI로 Unity 서비스를 React로 옮긴 방법](https://tech.hancom.com/migrated-unity-to-react-with-ai/) · 한글과컴퓨터 · 08-26
- [Asana, Codex로 몇 년 걸릴 코드 이전을 2주 만에 끝내다](https://openai.com/index/asana) <sub>Asana completed a years-long code migration in 2 weeks with Codex</sub> · OpenAI · 08-18
- [Kiro로 반복 가능한 PHP→Java 이전 엔진 만들기](https://aws.amazon.com/blogs/machine-learning/build-a-repeatable-php-to-java-migration-engine-with-kiro/) <sub>Build a repeatable PHP-to-Java migration engine with Kiro</sub> · AWS Machine Learning · 10-30
- [AI 에이전트로 복잡한 레거시 코드 현대화하기](https://mistral.ai/news/legacy-code-modernization/) <sub>Modernizing complex legacy code with AI agents.</sub> · Mistral AI · 09-09
- [AI 에이전트에게 모바일 개발 환경을 줘봤다](https://shopify.engineering/remote-dev) <sub>We gave AI agents a mobile dev environment</sub> · Shopify · 10-22
