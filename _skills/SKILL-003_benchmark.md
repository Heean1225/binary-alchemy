---
type: skill
id: SKILL-003
description: "Use when benchmarking and comparing results"
triggers: ["성능 비교", "메트릭 측정", "모델 평가"]
used-by: ["AGENT_evaluator"]
tags:
  - type/skill
---

# SKILL-003: Benchmark & Evaluation

## When to Use

여러 모델/접근법을 정량적으로 비교하거나, 논문 수치를 재현할 때.

## Process

### 1. 데이터셋 선정
```
소규모 (Phase 1 Quick Test):
  - 자체 작성 C 함수 5~10개 (add, gcd, fibonacci, sort, search)

중규모 (Phase 2 Reproduce):
  - HumanEval C subset (~50 함수)
  - FormAI subset (~100 프로그램)

대규모 (Phase 3+ Full Eval):
  - Decompile-Eval 벤치마크
  - SuperCoder 벤치마크 (8,072 프로그램)
```

### 2. 메트릭 선택

| 메트릭 | 용도 | 계산 방법 |
|--------|------|----------|
| **Pass@1** | 생성 코드 정확도 | 생성 → 어셈블 → 실행 → 테스트 통과율 |
| **Re-exec** | 디컴파일 품질 | 디컴파일 → 재컴파일 → 실행 성공률 |
| **BLEU** | 텍스트 유사도 | sacrebleu 패키지 |
| **Semantic** | 의미 보존도 | CLAP 임베딩 코사인 유사도 |
| **Speedup** | 성능 비교 | execution_time(gcc-O3) / execution_time(AI) |

### 3. 실행
```bash
# tools/eval_metrics.py 사용
python tools/eval_metrics.py \
  --dataset benchmarks/datasets/{name}/ \
  --model {model_name} \
  --metrics pass@1,reexec,bleu \
  --output benchmarks/results/{phase}/{name}.json
```

### 4. 비교표 생성
```markdown
| Model | Pass@1 | Re-exec | BLEU | Semantic |
|-------|--------|---------|------|----------|
| Nova 1.3B | XX% | - | - | - |
| Claude API | XX% | - | - | - |
| LLM4Decompile | - | XX% | XX | XX |
| Ghidra | - | XX% | XX | XX |
```

### 5. 결과 저장
```
benchmarks/results/{phase}/
├── {name}.json       # Raw 결과 데이터
├── {name}_table.md   # 비교표
└── {name}_chart.png  # 시각화 (선택)
```

## Completion Checklist

- [ ] 데이터셋 명시 (크기, 출처)
- [ ] 메트릭 정의
- [ ] 공정 비교 조건 확인 (동일 데이터, 동일 하드웨어)
- [ ] 결과 JSON 저장
- [ ] 비교표 생성
- [ ] 해석/결론 기술
