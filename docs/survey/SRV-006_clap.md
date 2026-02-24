---
type: survey
id: SRV-006
title: "CLAP: Learning Transferable Binary Code Representations"
category: rendering
year: 2024
venue: ISSTA 2024
url: https://arxiv.org/abs/2402.16928
github: https://github.com/Hustcw/CLAP
models: ["clap-asm", "clap-text"]
key-metric: "49.6% recall@1 improvement over jTrans in zero-shot"
reproducible: true
huggingface: "Hustcw/clap-asm"
tags:
  - type/survey
  - category/rendering
---

# SRV-006: CLAP — Contrastive Language-Assembly Pre-training

## 핵심 요약

어셈블리 코드와 자연어 설명을 **같은 임베딩 공간**에 매핑하는 대조 학습 모델. 195M 어셈블리-설명 쌍으로 학습. "이 어셈블리가 뭘 하는지"를 벡터로 표현.

## 접근 방법

1. **데이터 생성**: 자동으로 어셈블리 함수에 대한 자연어 설명 생성 (195M 쌍)
2. **대조 학습**: CLIP과 유사한 방식으로 어셈블리↔텍스트 임베딩 정렬
3. **Zero-shot 전이**: 학습하지 않은 태스크에도 임베딩으로 적용 가능

## Binary Alchemy 관련성

- **Phase 1**: 어셈블리 코드의 "의미"를 임베딩으로 추출하는 실험
- **Phase 2**: Semantic Round-Trip Score 계산 시 임베딩 유사도 활용
- **Phase 3**: Rendering Pipeline의 Layer 2 (함수별 자연어 요약) 활용 가능
- **핵심 가치**: 바이너리의 "의미"를 정량화할 수 있는 도구

## 실행 가능성

- [x] 모델 공개 (HuggingFace)
- [x] GitHub 코드 공개
- [x] 작은 모델이라 로컬 실행 용이

## Related

- [[SRV-001_nova]] — 어셈블리 생성 (CLAP은 이해)
- [[SRV-004_llm4decompile]] — 코드로 렌더링 (CLAP은 임베딩으로 이해)
