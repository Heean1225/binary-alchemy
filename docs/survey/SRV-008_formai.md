---
type: survey
id: SRV-008
title: "FormAI Dataset: AI-Generated Code Security Evaluation"
category: verification
year: 2023
url: https://arxiv.org/abs/2307.02192
key-metric: "112K AI 생성 C 프로그램, 취약점 분류 완비"
reproducible: true
tags:
  - type/survey
  - category/verification
---

# SRV-008: FormAI Dataset

## 핵심 요약

112,000개의 AI 생성 C 프로그램에 대한 **취약점 분류 데이터셋**. ESBMC(형식 검증 도구)로 자동 분류. AI가 생성한 코드의 보안 문제를 대규모로 분석한 최초의 데이터셋.

## Binary Alchemy 관련성

- **Phase 2**: 검증 파이프라인 실험의 데이터셋
- **Phase 3**: 자동 검증 시 참조 데이터
- **핵심 가치**: "AI가 만든 코드가 얼마나 안전한가"의 정량적 근거

## Related

- [[SRV-009_metamorphic-testing]] — 또 다른 검증 접근
- [[SRV-010_formal-verification]] — 형식 검증 (FormAI가 ESBMC 사용)
