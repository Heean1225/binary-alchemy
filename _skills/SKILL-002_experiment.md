---
type: skill
id: SKILL-002
description: "Use when designing and running an experiment"
triggers: ["실험 실행", "모델 테스트", "프로토타입 구현"]
used-by: ["AGENT_experimenter"]
tags:
  - type/skill
---

# SKILL-002: Experiment Design & Execution

## When to Use

모델 추론, 파이프라인 단계 테스트, 프로토타입 구현 등 실험을 실행할 때.

## Process

### 1. 환경 확인 (Pre-flight)
```python
# 실행할 것:
import torch
print(f"CUDA: {torch.cuda.is_available()}")
print(f"Device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU'}")
print(f"VRAM: {torch.cuda.get_device_properties(0).total_mem / 1e9:.1f}GB" if torch.cuda.is_available() else "N/A")

# 확인할 것:
# - 필요 패키지 설치 여부
# - 모델 파일 다운로드 여부
# - 디스크 공간 (모델 크기 고려)
# - API 키 설정 여부 (Claude API 사용 시)
```

### 2. 실험 설계 (Design)
```
실험명: EXP-{NNN}_{title}
Phase: {1|2|3}

목적: 한 줄로 "무엇을 확인하려는가"
입력: 구체적인 입력 데이터 정의
기대 출력: 성공 시 어떤 결과가 나오는가
평가 기준: 성공/실패/부분성공 판단 기준

코드 위치: experiments/phase{N}-{name}/{실험명}/
```

### 3. 코드 작성 (Implement)
```
experiments/phase{N}-{name}/{실험명}/
├── run.py          # 메인 실행 스크립트
├── README.md       # 실행 방법 (한 줄 명령어)
├── requirements.txt # 추가 의존성 (있으면)
├── input/          # 입력 데이터
└── output/         # 실행 결과 (gitignore에 따라)
```

### 4. 실행 및 기록 (Execute)
```
- run.py 실행
- stdout/stderr 캡처
- 실행 시간 기록
- 에러 발생 시: 에러 메시지 + 원인 분석 + 시도한 해결책
```

### 5. 문서화 (Document)

EXP 노트 생성:

```yaml
---
type: experiment
id: EXP-{NNN}
title: "{실험명}"
phase: {1|2|3}
date: {YYYY-MM-DD}
status: success | partial | failed
related-survey: ["SRV-{NNN}"]
tags:
  - type/experiment
  - phase/{N}
---
```

본문 구조:
```
# EXP-{NNN}: {실험명}
## 목적
## 환경 (GPU, OS, Python 버전, 모델 크기)
## 입력
## 실행 방법 (복붙 가능한 명령어)
## 결과 (수치, 출력 예시)
## 발견사항 (예상과 다른 점, 배운 것)
## 다음 단계
## Related
```

## Completion Checklist

- [ ] 환경 확인 완료
- [ ] 실험 코드 작성 + README
- [ ] 실행 성공 (또는 실패 원인 기록)
- [ ] EXP 노트 작성
- [ ] 결과 데이터 저장
- [ ] MOC_master.md 실험 테이블에 등록
