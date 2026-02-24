---
type: survey
id: SRV-001
title: "NOVA: Generative Language Models for Assembly Code"
category: generation
year: 2025
venue: ICLR 2025
url: https://arxiv.org/abs/2311.13721
models: ["nova-1.3b"]
key-metric: "14.84-21.58% higher Pass@1 vs LLM4Decompile; GPT-4o 수준 at 1.3B"
reproducible: true
huggingface: "lt-asset/nova-1.3b"
tags:
  - type/survey
  - category/generation
---

# SRV-001: NOVA — Generative Language Models for Assembly Code

## 핵심 요약

어셈블리 코드에 특화된 생성형 언어 모델. **계층적 어텐션(hierarchical attention)**과 **대조 학습(contrastive learning)**으로 어셈블리 코드의 저정보 밀도(low information density) 문제를 해결.

## 문제 인식

- 어셈블리 코드는 고수준 언어보다 **정보 밀도가 낮음** (같은 로직이 훨씬 많은 줄)
- 일반적인 Transformer의 flat attention으로는 어셈블리의 구조를 효과적으로 포착 못함
- 기존 바이너리 분석 모델(BinBERT 등)은 이해(understanding)에만 집중, 생성(generation) 부족

## 접근 방법

1. **Hierarchical Attention**: 명령어 내부(intra-instruction) + 명령어 간(inter-instruction) 2단계 어텐션
2. **Contrastive Learning**: 의미적으로 유사한 어셈블리 함수를 가깝게, 다른 함수를 멀리
3. **학습 데이터**: ~4.3M 어셈블리 함수 (C 프로그램에서 X86-64로 컴파일)

## 주요 결과

| Task | Metric | Nova 1.3B | vs GPT-4o |
|------|--------|-----------|-----------|
| Binary Decompilation | Pass@1 | +14.84~21.58% vs LLM4Decompile | 동등 수준 |
| Binary Code Similarity | Recall@1 | +6.17% | - |
| Assembly Summarization | - | 개선 | - |

## Binary Alchemy 관련성

- **Phase 1**: HuggingFace에서 모델 다운로드 후 어셈블리 생성 실험
- **Phase 2**: 어셈블리 생성 품질 벤치마크에 포함
- **핵심 가치**: 1.3B라는 작은 크기로 GPT-4o 수준 → 로컬 실행 가능, 실험 비용 낮음

## 실행 가능성

- [x] 모델 공개 (HuggingFace: `lt-asset/nova-1.3b`)
- [x] 코드 공개
- [x] GPU 16GB면 추론 가능 (1.3B)
- [ ] 학습 데이터 공개 여부 확인 필요

## Related

- [[SRV-004_llm4decompile]] — Nova가 LLM4Decompile 대비 비교
- [[SRV-003_llm-compiler]] — 또 다른 어셈블리 생성 모델
- [[SRV-006_clap]] — 어셈블리 임베딩 (이해 측면)
