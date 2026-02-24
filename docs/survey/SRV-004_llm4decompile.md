---
type: survey
id: SRV-004
title: "LLM4Decompile: Decompiling Binary Code with Large Language Models"
category: rendering
year: 2024
venue: EMNLP 2024
url: https://arxiv.org/abs/2403.05286
github: https://github.com/albertan017/LLM4Decompile
models: ["LLM4Decompile-1.3b", "LLM4Decompile-6.7b", "LLM4Decompile-22b"]
key-metric: "V2: 64.94% re-executability on Decompile benchmark"
reproducible: true
tags:
  - type/survey
  - category/rendering
---

# SRV-004: LLM4Decompile

## 핵심 요약

LLM을 사용한 **바이너리 → C 코드 디컴파일**의 대표 연구. 4B 토큰의 어셈블리-C 쌍으로 학습. 1.3B~33B 크기의 모델 시리즈. GPT-4o보다 100%+ 높은 재실행성.

## 문제 인식

- 전통 디컴파일러(Ghidra, IDA)는 규칙 기반 → 읽기 어려운 코드 생성
- LLM이 "의미를 이해한" 디컴파일을 할 수 있는가?
- 디컴파일된 코드가 원래 동작을 재현할 수 있는가? (re-executability)

## 접근 방법

1. **데이터**: AnghaBench 1M+ C 샘플 → GCC O0~O3로 컴파일 → 4B 토큰의 어셈블리-C 쌍
2. **모델**: DeepSeek-Coder 기반, 1.3B/6.7B/22B/33B
3. **V2 (Sep 2024)**: Decompile-Ghidra-100K 추가 학습, 재실행성 크게 개선

## 주요 결과

| Model | Re-executability | vs GPT-4o |
|-------|-----------------|-----------|
| LLM4Decompile-6B V1 | 21% | +100% 이상 |
| LLM4Decompile V2 | 64.94% | 훨씬 상회 |
| Ghidra (전통) | ~85-95% 기능적 | 가독성 낮음 |

## Binary Alchemy 관련성

- **Phase 1**: 핵심 실습 대상. C → 컴파일 → objdump → LLM4Decompile → C' 파이프라인 체험
- **Phase 2**: Rendering 벤치마크의 주요 비교 대상
- **Phase 3**: Rendering Pipeline의 Layer 1 (디컴파일된 C) 담당
- **핵심 가치**: **라운드트립의 "돌아오는 방향" 핵심 모델**

## 실행 가능성

- [x] 모델 공개 (HuggingFace: 1.3B~33B)
- [x] GitHub 코드 공개 (추론 스크립트 포함)
- [x] 1.3B 모델은 CPU에서도 실행 가능
- [x] Decompile-Eval 벤치마크 공개
- [x] V2 모델 공개 (Ghidra 통합)

## Related

- [[SRV-001_nova]] — 반대 방향 (Generation)
- [[SRV-005_sk2decompile]] — 개선된 디컴파일 접근
- [[SRV-003_llm-compiler]] — IR 수준 디스어셈블리
