# Binary Alchemy

> Version: 0.2 | Created: 2026-02-24 | Updated: 2026-02-25

## Purpose

AI가 소스코드 없이 바이너리를 직접 생성하고, 사람은 바이너리를 렌더링된 형태로 보는
**양방향 파이프라인**을 연구하고 프로토타입하는 프로젝트.

```
자연어 의도 → [AI Generation] → 바이너리 → [AI Rendering] → 사람이 읽는 표현
```

## Abstraction Levels

> 이 프로젝트가 다루는 추상화 계층. 각 레벨 간 변환이 연구 대상.

```
Level 5: 자연어 의도     "두 정수의 최대공약수를 구하는 함수"
Level 4: 의사 코드       result = gcd(a, b)
Level 3: 소스코드 (C)    int gcd(int a, int b) { ... }
Level 2: LLVM-IR         define i32 @gcd(i32 %a, i32 %b) { ... }
Level 1: 어셈블리        mov eax, edi; cmp eax, 0; ...
Level 0: 기계어/바이너리  48 89 D8 B8 01 00 00 00 ...
```

- **생성 방향**: Level 5 → Level 0 (아래로)
- **렌더링 방향**: Level 0 → Level 5 (위로)
- 어셈블리(L1) → 기계어(L0)는 1:1 기계적 변환 (어셈블러가 처리)
- 핵심 연구: Level 5 ↔ Level 1~2 변환의 AI 활용

## Tech Stack

| 계층 | 도구 | 용도 |
|------|------|------|
| 실험 | Python 3.11+, PyTorch, transformers | 모델 추론, 프로토타이핑 |
| 코어 엔진 | Rust, Cargo workspace | 성능 핵심 모듈 (Phase 4+) |
| LLM API | Claude API (Anthropic) | 코드 생성, 설명 생성 |
| ML 모델 | Nova, LLM4Decompile, CLAP, Meta LLM Compiler | 로컬 모델 추론 |
| 역공학 | Ghidra, GhidrAssist | 바이너리 분석 |
| 컴파일러 | GCC, Clang/LLVM, NASM | 컴파일, 어셈블, 링크 |
| 문서 | Obsidian | 지식 관리 (docs/) |

## Rules

| # | Rule | 이유 |
|---|------|------|
| 1 | **실험 기록 필수**: 모든 실험은 docs/experiments/EXP-NNN에 기록 | 재현 가능성 보장 |
| 2 | **서베이 우선**: 구현 전 관련 논문/도구를 먼저 조사 | 바퀴 재발명 방지 |
| 3 | **벤치마크 동반**: 성능 주장은 benchmarks/에 수치로 뒷받침 | 증거 기반 |
| 4 | **점진적 빌드**: Phase 순서를 건너뛰지 않음 | 기초 없는 구현 방지 |
| 5 | **Quick Win 우선**: 기존 도구 활용 → 커스텀 구현 순서 | 빠른 학습 루프 |

## Agents

| Agent | Role | Triggers |
|-------|------|----------|
| AGENT_researcher | 논문/도구 서베이, 최신 연구 추적 | 새 주제 탐색, /survey |
| AGENT_experimenter | 실험 설계/실행/기록 | 모델 추론, /experiment, /roundtrip |
| AGENT_evaluator | 벤치마크, 비교, 메트릭 | 결과 평가, /benchmark |

> Agent 정의: `_agents/` 디렉토리

## Skills

| ID | Skill | Trigger |
|----|-------|---------|
| SKILL-001 | survey | 새 논문/도구/데이터셋 조사 시 |
| SKILL-002 | experiment | 실험 설계/실행 시 |
| SKILL-003 | benchmark | 성능 측정/비교 시 |
| SKILL-004 | round-trip | 전체 생성→렌더링 루프 테스트 시 |

> Skill 정의: `_skills/` 디렉토리

## Slash Commands

| Command | Purpose | Prompt |
|---------|---------|--------|
| /survey {topic} | 논문/도구 서베이 → SRV 노트 생성 | _prompts/PROMPT_survey.md |
| /experiment {name} | 실험 설계 + 코드 스캐폴드 + EXP 노트 | _prompts/PROMPT_experiment.md |
| /benchmark {target} | 벤치마크 실행 + 비교표 생성 | _prompts/PROMPT_benchmark.md |
| /roundtrip {intent} | 전체 라운드트립 테스트 | _prompts/PROMPT_roundtrip.md |

## Tools

| Tool | 용도 | 사용법 |
|------|------|--------|
| `tools/model_runner.py` | 모델 통합 추론 래퍼 | `--model nova --input "..." --task generate-asm` |
| `tools/compile_chain.py` | C/ASM→바이너리 자동화 | `--input test.c --output test.elf --dump` |
| `tools/eval_metrics.py` | 평가 메트릭 계산 | `pass1 --generated out.s --test test.py` |
| `tools/render_view.py` | 다단계 렌더링 HTML | `--binary gcd.elf --output view.html` |

## Roadmap

```
Phase 0: Survey & Landscape     ✅ 완료
Phase 1: Playground (기존 도구 체험)  ← 다음
Phase 2: Reproduce & Evaluate (논문 재현)
Phase 3: Pipeline Integration (Python 프로토타입)
Phase 4: Rust Core Engine (선택)
Phase 5: Novel Contributions (독창적 기여)
Phase 6: Integration & Publication
```

## Directory Structure

```
binary-alchemy/
├── CLAUDE.md              # 이 파일 (규칙, Agent, Skill, Tool 정의)
├── README.md
├── _agents/               # Agent 정의
│   ├── AGENT_researcher.md
│   ├── AGENT_experimenter.md
│   └── AGENT_evaluator.md
├── _skills/               # Skill 정의
│   ├── SKILL-001_survey.md
│   ├── SKILL-002_experiment.md
│   ├── SKILL-003_benchmark.md
│   └── SKILL-004_round-trip.md
├── _prompts/              # Slash Command Prompts
│   ├── PROMPT_survey.md
│   ├── PROMPT_experiment.md
│   ├── PROMPT_benchmark.md
│   └── PROMPT_roundtrip.md
├── docs/                  # Obsidian vault
│   ├── MOC_master.md      # 최상위 허브
│   ├── survey/            # SRV-NNN 서베이 노트
│   ├── design/            # 아키텍처 설계
│   ├── experiments/       # EXP-NNN 실험 기록
│   └── journal/           # 진행 일지
├── experiments/           # 실험 코드
│   ├── phase1-playground/ # 기존 도구 체험
│   ├── phase2-reproduce/  # 논문 재현
│   └── phase3-pipeline/   # 파이프라인 통합
├── core/                  # Rust 코어 (Phase 4+)
├── benchmarks/            # 벤치마크
├── tools/                 # Python 유틸리티
│   ├── model_runner.py    # 모델 통합 추론 래퍼
│   ├── compile_chain.py   # C/ASM→바이너리 체인
│   ├── eval_metrics.py    # 평가 메트릭
│   └── render_view.py     # 다단계 렌더링 뷰
├── pyproject.toml
└── .gitignore
```

## Naming Convention

| 유형 | 접두어 | 형식 | 예시 |
|------|--------|------|------|
| 서베이 | SRV | `SRV-{NNN}_{title}.md` | `SRV-001_nova.md` |
| 실험 | EXP | `EXP-{NNN}_{title}.md` | `EXP-001_nova-inference.md` |
| 설계 | - | `{title}.md` | `architecture.md` |

## Key Research References

### Generation (AI → Binary)
- NOVA (ICLR 2025): 계층적 어텐션, 어셈블리 코드 생성
- SuperCoder (2025): 어셈블리 최적화, gcc-O3 대비 1.46x
- Meta LLM Compiler: LLVM-IR + 어셈블리, 546B 토큰 학습

### Rendering (Binary → Human)
- LLM4Decompile: 바이너리→C 디컴파일, 64.94% 재실행성
- SK²Decompile: 골격→스킨 2단계 디컴파일
- CLAP: 195M 어셈블리-설명 쌍, 대조 학습

### Verification
- FormAI: 112K AI 생성 C 프로그램 취약점 분류
- Metamorphic Testing: 75% 오류 탐지
- AI-BOM (OWASP): AI 투명성 표준
