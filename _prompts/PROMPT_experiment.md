---
type: prompt
command: /experiment
invokes: AGENT_experimenter
required-skills: ["SKILL-002_experiment"]
---

# /experiment {name}

## Purpose

새 실험을 설계하고 실행 환경을 세팅한다.

## Input

- `{name}`: 실험 이름 (예: "nova-inference", "llm4decompile-gcd")

## Steps

1. AGENT_experimenter 활성화
2. 환경 확인 (GPU, 패키지, 모델)
3. 실험 디렉토리 + 코드 스캐폴드 생성
4. SKILL-002_experiment 프로세스 실행
5. EXP 노트 생성

## Output

- `experiments/phase{N}-{name}/` 실험 코드
- `docs/experiments/EXP-{NNN}_{title}.md` 실험 기록
