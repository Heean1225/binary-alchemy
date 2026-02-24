---
type: prompt
command: /benchmark
invokes: AGENT_evaluator
required-skills: ["SKILL-003_benchmark"]
---

# /benchmark {target}

## Purpose

대상 모델/접근법의 성능을 정량적으로 측정하고 비교한다.

## Input

- `{target}`: 벤치마크 대상 (예: "nova vs claude assembly-gen", "decompile quality")

## Steps

1. AGENT_evaluator 활성화
2. 데이터셋 확인/준비
3. SKILL-003_benchmark 프로세스 실행
4. 결과 JSON + 비교표 생성

## Output

- `benchmarks/results/{phase}/{name}.json`
- `benchmarks/results/{phase}/{name}_table.md`
