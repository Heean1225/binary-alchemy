---
type: prompt
command: /roundtrip
invokes: AGENT_experimenter
required-skills: ["SKILL-004_round-trip"]
---

# /roundtrip {intent}

## Purpose

자연어 의도에서 바이너리 생성 → 렌더링 → 의미 비교의 전체 루프를 실행한다.

## Input

- `{intent}`: 자연어 의도 (예: "두 정수의 최대공약수를 구하는 함수")

## Steps

1. AGENT_experimenter 활성화
2. SKILL-004_round-trip 프로세스 실행:
   - Step 1: 의도 기록
   - Step 2: 어셈블리/IR 생성 (사용 가능한 모델로)
   - Step 3: 어셈블 → 바이너리
   - Step 4: 기능 테스트
   - Step 5: 다단계 렌더링
   - Step 6: 의미 비교 (Semantic Score)
3. 종합 보고서 생성

## Output

- 바이너리 파일
- 렌더링 결과 (다단계)
- scores.json
- roundtrip_report.md
