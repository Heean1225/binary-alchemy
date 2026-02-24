---
type: survey
id: SRV-011
title: "AI Bill of Materials (AI-BOM)"
category: verification
year: 2025
url: https://owasp.org/www-project-aibom/
key-metric: "OWASP 공식 프로젝트, AI 투명성 표준"
reproducible: false
tags:
  - type/survey
  - category/verification
---

# SRV-011: AI-BOM (AI Bill of Materials)

## 핵심 요약

SBOM(Software Bill of Materials)을 AI 시대에 확장한 **AI-BOM**. AI가 생성한 코드/바이너리의 출처, 학습 데이터, 모델 버전, 설정을 추적하는 표준. OWASP 공식 프로젝트.

## 핵심 필드

- 어떤 모델이 생성했는가 (모델 ID, 버전)
- 어떤 프롬프트로 생성했는가
- 학습 데이터 출처
- 검증 결과

## Binary Alchemy 관련성

- **Phase 3**: 생성된 바이너리에 AI-BOM 메타데이터 첨부 (실험적)
- **Phase 5**: Intent-Aligned Assembly에서 .provenance 섹션과 연결
- **핵심 가치**: "이 바이너리를 누가(어떤 AI가) 왜 만들었는가"의 추적 가능성

## Related

- [[SRV-008_formai]] — AI 코드 보안 (AI-BOM은 투명성)
- [[SRV-010_formal-verification]] — 정확성 증명 (AI-BOM은 출처 추적)
