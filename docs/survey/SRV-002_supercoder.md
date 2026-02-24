---
type: survey
id: SRV-002
title: "SuperCoder: Assembly Program Superoptimization with LLMs"
category: generation
year: 2025
url: https://arxiv.org/abs/2505.11480
models: ["Qwen2.5-Coder-7B (finetuned)"]
key-metric: "95% correctness, 1.46x average speedup vs gcc -O3"
reproducible: true
tags:
  - type/survey
  - category/generation
---

# SRV-002: SuperCoder — Assembly Program Superoptimization with LLMs

## 핵심 요약

LLM을 사용한 **어셈블리 수준 슈퍼최적화**. gcc -O3보다 더 빠른 어셈블리를 AI가 생성할 수 있음을 최초로 대규모 벤치마크로 검증.

## 문제 인식

- 컴파일러 최적화(gcc -O3)는 범용적이라 특정 함수에 대한 극한 최적화를 놓침
- 기존 슈퍼최적화(stochastic search)는 너무 느리고 작은 코드에만 적용 가능
- LLM이 컴파일러를 능가하는 최적화를 생성할 수 있는가?

## 접근 방법

1. **벤치마크 구축**: 8,072개 어셈블리 프로그램 (최초의 대규모 슈퍼최적화 벤치마크)
2. **Fine-tuning**: Qwen2.5-Coder-7B를 어셈블리 최적화 데이터로 파인튜닝
3. **RL (RLVR)**: 실행 결과를 보상으로 사용하는 강화학습

## 주요 결과

| Model | Correctness | Avg Speedup vs gcc -O3 |
|-------|-------------|----------------------|
| Qwen2.5-Coder-7B (finetuned) | 95% | 1.46x |
| Claude Opus 4 (baseline) | 51.5% | 1.43x |
| GPT-4 (baseline) | - | ~1.2x |

## Binary Alchemy 관련성

- **Phase 2**: 어셈블리 생성 품질 평가 시 "AI가 컴파일러보다 나을 수 있다"는 증거
- **Phase 5**: 최적화 방향의 독창적 기여 가능성 (특정 도메인 최적화)
- **핵심 통찰**: AI 어셈블리 생성이 "그냥 되는 수준"이 아니라 "컴파일러를 이기는 수준"까지 도달

## 실행 가능성

- [x] 논문 공개
- [ ] 모델 가중치 공개 여부 확인 필요
- [x] 벤치마크 공개 (8,072 프로그램)
- [ ] RLVR 학습 코드 공개 여부 확인 필요

## Related

- [[SRV-001_nova]] — 어셈블리 생성 (생성 자체에 초점)
- [[SRV-003_llm-compiler]] — LLVM-IR 최적화 (IR 수준)
