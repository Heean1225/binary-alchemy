---
type: survey
id: SRV-003
title: "Meta Large Language Model Compiler"
category: generation
year: 2024
venue: ACM SIGPLAN
url: https://arxiv.org/abs/2407.02524
models: ["llm-compiler-7b", "llm-compiler-13b"]
key-metric: "77% of autotuning potential, 45% disassembly round-trip accuracy"
reproducible: true
huggingface: "facebook/llm-compiler-13b"
tags:
  - type/survey
  - category/generation
---

# SRV-003: Meta LLM Compiler

## 핵심 요약

Meta가 개발한 **컴파일러 최적화 전용 LLM**. 546B 토큰의 LLVM-IR + X86/ARM 어셈블리로 학습. 7B/13B 크기. 컴파일러 플래그 튜닝과 디스어셈블리 라운드트립에서 강력한 성능.

## 문제 인식

- LLM이 자연어와 고수준 코드에서는 뛰어나지만, 컴파일러 IR과 어셈블리에는 특화되지 않음
- 컴파일러 최적화는 전문가 지식 필요 → AI가 자동화할 수 있는가?
- LLVM-IR ↔ 어셈블리 변환을 LLM이 학습할 수 있는가?

## 접근 방법

1. **대규모 학습**: 546B 토큰 (LLVM-IR + X86-64 + ARM 어셈블리)
2. **Code Llama 기반**: Code Llama를 컴파일러 도메인에 추가 학습
3. **Two tasks**: Flag Tuning (최적화 플래그 추천) + Disassembly (바이너리→어셈블리→IR)

## 주요 결과

| Task | Metric | Performance |
|------|--------|-------------|
| Flag Tuning | autotuning 달성률 | 77% |
| Disassembly Round-Trip | 정확도 | 45% |
| Disassembly Exact Match | 완전 일치 | 14% |

## Binary Alchemy 관련성

- **Phase 1**: HuggingFace에서 모델 다운로드 후 LLVM-IR 생성 실험
- **Phase 2**: Generation 파이프라인에서 LLVM-IR 경로의 핵심 모델
- **Phase 3**: `intent → LLVM-IR → assembly → binary` 파이프라인의 중간 단계
- **핵심 가치**: **LLVM-IR을 다루는 유일한 대규모 공개 모델** → Generation Pipeline의 핵심

## 실행 가능성

- [x] 모델 공개 (HuggingFace: `facebook/llm-compiler-7b`, `facebook/llm-compiler-13b`)
- [x] 7B 모델은 GPU 16GB에서 실행 가능
- [x] LLVM-IR + 어셈블리 양방향 지원
- [ ] 13B 모델은 양자화 필요할 수 있음

## Related

- [[SRV-001_nova]] — 어셈블리 생성 (Nova는 C↔Assembly, LLM Compiler는 IR↔Assembly)
- [[SRV-004_llm4decompile]] — 디컴파일 방향 (반대 방향)
