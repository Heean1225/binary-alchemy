---
type: survey
id: SRV-009
title: "Metamorphic Prompt Testing for LLM-Generated Programs"
category: verification
year: 2024
url: https://arxiv.org/abs/2406.06864
key-metric: "75% error detection rate, 8.6% false positive rate"
reproducible: true
tags:
  - type/survey
  - category/verification
---

# SRV-009: Metamorphic Prompt Testing

## 핵심 요약

프롬프트를 변형(paraphrase)하여 같은 의도에 대해 여러 번 코드를 생성하고, **일관성을 검사**하여 오류를 탐지. "올바른 코드 간에는 일관성이 있지만, 결함 있는 코드는 변형 시 불일치"라는 원리.

## 접근 방법

1. 프롬프트 A로 코드 생성 → 프롬프트 A' (의미 동일, 표현 다름)로 코드 생성
2. 두 코드의 동작이 동일한지 비교 (metamorphic relation)
3. 불일치하면 오류 가능성 높음

## Binary Alchemy 관련성

- **Phase 2**: 검증 파이프라인 실험
- **Phase 3**: 라운드트립 검증의 핵심 기법
- **핵심 가치**: 테스트 오라클 없이 AI 생성 코드를 검증하는 방법

## Related

- [[SRV-008_formai]] — 데이터셋 기반 검증 (이것은 기법 기반)
- [[SRV-010_formal-verification]] — 수학적 증명 기반 (이것은 통계적)
