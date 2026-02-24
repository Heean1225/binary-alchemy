---
type: prompt
command: /survey
invokes: AGENT_researcher
required-skills: ["SKILL-001_survey"]
---

# /survey {topic}

## Purpose

주어진 주제에 대한 논문/도구/데이터셋을 검색하고 SRV 노트를 생성한다.

## Input

- `{topic}`: 검색할 주제 (예: "assembly optimization RL", "neural decompiler 2025")

## Steps

1. AGENT_researcher 활성화
2. SKILL-001_survey 프로세스 실행:
   - 웹 검색 (arxiv, GitHub, HuggingFace)
   - 관련성 필터링
   - SRV 노트 작성
   - MOC_master.md 등록
3. 결과 요약 출력

## Output

- `docs/survey/SRV-{NNN}_{title}.md` (1건 이상)
- MOC_master.md 업데이트
