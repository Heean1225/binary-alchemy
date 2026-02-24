---
type: survey
id: SRV-007
title: "GhidrAssist + DAILA: AI-Powered Reverse Engineering Plugins"
category: tools
year: 2024
github-ghidrassist: https://github.com/jtang613/GhidrAssist
github-daila: https://github.com/mahaloz/DAILA
key-metric: "Claude/GPT 연동, 함수 요약/변수 이름 추론"
reproducible: true
tags:
  - type/survey
  - category/tools
---

# SRV-007: GhidrAssist + DAILA

## 핵심 요약

Ghidra(오픈소스 역공학 도구)에 LLM을 연결하는 플러그인들. 바이너리를 로드하면 AI가 함수 요약, 변수 이름 추론, 취약점 탐지를 수행. **"바이너리를 사람이 읽을 수 있게 렌더링"하는 현재 상태의 실체**.

## 도구 비교

| 도구 | 백엔드 | 특징 |
|------|--------|------|
| GhidrAssist | OpenAI, Anthropic, Ollama | 범용 LLM 연동 |
| DAILA | GPT-4, Claude, VarBERT | 변수 이름 추론 특화 |
| Binary Ninja Sidekick | 자체 | 상용, 완전 통합 |

## Binary Alchemy 관련성

- **Phase 1**: Ghidra + GhidrAssist 설치 후 바이너리 분석 체험
- **Phase 3**: Rendering Pipeline의 Layer 4 (제어흐름 그래프) 소스
- **핵심 가치**: "현재 사람이 바이너리를 어떻게 읽는가"의 baseline 경험

## Related

- [[SRV-004_llm4decompile]] — 자동 디컴파일 (Ghidra는 수동 분석 + AI 보조)
- [[SRV-006_clap]] — 임베딩 기반 이해 (Ghidra는 대화형 이해)
