---
type: survey
id: SRV-005
title: "SK²Decompile: LLM-based Two-Phase Binary Decompilation"
category: rendering
year: 2025
url: https://arxiv.org/abs/2509.22114
key-metric: "+21.6% re-executability gain over GPT-5-mini on HumanEval"
reproducible: false
tags:
  - type/survey
  - category/rendering
---

# SRV-005: SK²Decompile

## 핵심 요약

2단계 디컴파일: **골격(Skeleton)** 복원 → **스킨(Skin)** 부여. 구조 복원과 식별자 이름 지정을 분리하여 각각 최적화. RL로 문법 준수 강화.

## 접근 방법

1. **Phase 1 (Skeleton)**: 제어 흐름, 타입, 구조를 복원 (변수명은 placeholder)
2. **Phase 2 (Skin)**: placeholder에 의미 있는 이름을 부여 (RL 기반)
3. **강화학습**: 구문 정확성을 보상으로 사용

## Binary Alchemy 관련성

- **Phase 5**: Progressive Binary Rendering 아이디어의 이론적 근거
- "골격→스킨" 패턴은 다단계 렌더링의 핵심 원리

## Related

- [[SRV-004_llm4decompile]] — 기본 디컴파일 (단일 단계)
