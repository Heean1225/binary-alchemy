---
type: survey
id: SRV-010
title: "AI + Formal Verification (Kleppmann 2025)"
category: verification
year: 2025
url: https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html
key-metric: "AI가 형식 검증을 주류화할 것이라는 예측"
reproducible: false
tags:
  - type/survey
  - category/verification
---

# SRV-010: AI + Formal Verification

## 핵심 요약

Martin Kleppmann의 2025년 예측: AI가 Dafny, Lean, Verus 등 형식 검증 언어의 증명을 자동 생성하면서, 형식 검증이 주류로 올라올 것. **AI가 코드를 생성하고, AI가 그 코드의 정확성을 수학적으로 증명**하는 미래.

## 관련 도구

| 도구 | 언어 | 특징 |
|------|------|------|
| Dafny | C#-like | 자동 검증, MS Research |
| Lean 4 | 함수형 | 수학 증명, 커뮤니티 활발 |
| Verus | Rust | Rust 코드의 형식 검증 |

## Binary Alchemy 관련성

- **Phase 5**: Verified Binary Generation — 의도 → 스펙(Dafny) → 증명 → 바이너리
- **핵심 가치**: "AI가 만든 바이너리를 어떻게 신뢰하는가"의 궁극적 해답

## Related

- [[SRV-008_formai]] — 통계적 검증 (이것은 수학적 증명)
- [[SRV-009_metamorphic-testing]] — 경험적 검증 (이것은 형식적 검증)
