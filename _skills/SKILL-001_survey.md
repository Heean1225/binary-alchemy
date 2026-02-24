---
type: skill
id: SKILL-001
description: "Use when surveying a new paper, tool, or dataset"
triggers: ["새 논문 발견", "도구 조사", "데이터셋 탐색"]
used-by: ["AGENT_researcher"]
tags:
  - type/skill
---

# SKILL-001: Paper/Tool Survey

## When to Use

새로운 논문, 도구, 데이터셋, 모델을 발견했을 때.

## Process

### 1. 검색 (Search)
```
- arxiv: "{keyword} assembly|binary|decompile|LLM"
- GitHub: 관련 레포지토리
- HuggingFace: 공개 모델/데이터셋
- Google Scholar: 인용 관계 추적
```

### 2. 읽기 (Read)
```
- Abstract + Introduction: 뭘 하는 건지
- Method: 어떻게 하는 건지
- Results: 얼마나 잘 되는지 (핵심 수치)
- Conclusion: 한계가 뭔지
```

### 3. 판단 (Evaluate)
```
Binary Alchemy 파이프라인 매핑:
  □ Generation (L5→L0): 자연어→어셈블리/바이너리 생성에 해당?
  □ Rendering (L0→L5): 바이너리→사람 표현 변환에 해당?
  □ Verification: 검증/안전에 해당?
  □ Infrastructure: 도구/데이터셋/프레임워크?

실행 가능성:
  □ 모델 공개 (HuggingFace 등)?
  □ 코드 공개 (GitHub)?
  □ 데이터셋 공개?
  □ 내 하드웨어로 실행 가능?
```

### 4. 문서화 (Document)

SRV 노트 생성:

```yaml
---
type: survey
id: SRV-{NNN}
title: "{논문/도구명}"
category: generation | rendering | verification | infrastructure
year: {YYYY}
url: {URL}
models: [{모델명}]
key-metric: "{핵심 수치 한 줄}"
reproducible: true/false
tags:
  - type/survey
  - category/{category}
---
```

본문 구조:
```
# SRV-{NNN}: {제목}
## 핵심 요약 (3줄 이내)
## 접근 방법
## 주요 결과 (표)
## Binary Alchemy 관련성 (어느 Phase에서 활용?)
## 실행 가능성 (체크리스트)
## Related ([[wikilink]])
```

### 5. 등록 (Register)
```
- docs/MOC_master.md 해당 테이블에 행 추가
- 관련 SRV 노트의 Related 섹션에 [[wikilink]] 추가
```

## Completion Checklist

- [ ] SRV 노트 작성 완료
- [ ] frontmatter 필수 필드 모두 채움
- [ ] category 정확히 분류
- [ ] reproducible 여부 확인
- [ ] MOC_master.md에 등록
- [ ] 관련 노트에 cross-link
