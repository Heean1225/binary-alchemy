---
type: skill
id: SKILL-004
description: "Use when testing the full generation→rendering round-trip"
triggers: ["라운드트립 테스트", "양방향 검증", "파이프라인 전체 테스트"]
used-by: ["AGENT_experimenter", "AGENT_evaluator"]
tags:
  - type/skill
---

# SKILL-004: Round-Trip Test

## When to Use

자연어 의도 → 바이너리 생성 → 렌더링 → 의미 비교의 전체 루프를 테스트할 때.
Binary Alchemy의 **핵심 실험 절차**.

## Process

### Full Round-Trip Pipeline

```
Step 1: Intent (Level 5)
  입력: "두 정수의 최대공약수를 반환하는 함수"
          ↓
Step 2: Generate (Level 5 → Level 1)
  방법 A: Claude API → 어셈블리 직접 생성
  방법 B: Claude API → C → gcc → objdump → 어셈블리
  방법 C: Nova 모델 → 어셈블리
  방법 D: LLM Compiler → LLVM-IR → llc → 어셈블리
          ↓
Step 3: Assemble (Level 1 → Level 0)
  as gcd.s -o gcd.o && ld gcd.o -o gcd.elf
  (또는 NASM: nasm -f elf64 gcd.asm -o gcd.o)
          ↓
Step 4: Verify (Level 0)
  - 실행 테스트: ./gcd 12 8 → 4 (expected)
  - 여러 입력으로 fuzz test
          ↓
Step 5: Render (Level 0 → Level 1~5)
  Layer 1: objdump -d gcd.elf → 어셈블리 (기계적)
  Layer 2: LLM4Decompile → C 코드 (AI)
  Layer 3: Claude API → 함수 설명 (AI)
  Layer 4: CLAP → 임베딩 (AI)
          ↓
Step 6: Compare (Level 5 vs Level 5')
  원래 의도: "두 정수의 최대공약수를 반환하는 함수"
  렌더링 설명: "This function computes the GCD of two integers..."
  → Semantic Score = cosine_similarity(embed(intent), embed(description))
```

### Metrics

| 메트릭 | 측정 대상 | 계산 |
|--------|----------|------|
| **Functional Score** | 바이너리가 올바르게 동작하는가 | 테스트 통과율 |
| **Semantic Score** | 원래 의도가 보존되었는가 | CLAP 임베딩 유사도 |
| **Readability Score** | 렌더링 결과가 읽기 쉬운가 | 변수명 의미 복원율 |
| **Round-Trip Score** | 종합 | 위 3개의 가중 평균 |

### Shortcut Variants

전체 파이프라인이 안 될 때 부분 테스트:

```
Half-Trip (Generation only):
  Intent → Generate → Assemble → Verify
  → "AI가 만든 바이너리가 동작하는가?"

Half-Trip (Rendering only):
  기존 바이너리 → Render → Compare with known source
  → "AI가 바이너리를 얼마나 잘 설명하는가?"

Compiler Baseline:
  Intent → C (human) → gcc → binary → Render → Compare
  → "전통적 경로 대비 AI 경로의 품질은?"
```

## Output

```
{experiment_dir}/
├── intent.txt           # 원래 자연어 의도
├── generated.s          # 생성된 어셈블리 (또는 .c, .ll)
├── binary.elf           # 어셈블된 바이너리
├── verify_results.json  # 기능 테스트 결과
├── rendered/
│   ├── layer1_asm.txt   # objdump 결과
│   ├── layer2_c.txt     # 디컴파일된 C
│   ├── layer3_desc.txt  # 자연어 설명
│   └── layer4_embed.json # CLAP 임베딩
├── scores.json          # 메트릭 결과
└── roundtrip_report.md  # 종합 보고서
```

## Completion Checklist

- [ ] 의도(intent) 명확히 정의
- [ ] 생성 경로(A/B/C/D) 명시
- [ ] 바이너리 실행 테스트 통과
- [ ] 최소 2개 렌더링 레이어 생성
- [ ] Semantic Score 계산
- [ ] 보고서 작성
