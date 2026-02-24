# Binary Alchemy

**From Intent to Metal, Rendered for Humans**

AI가 소스코드 없이 바이너리를 직접 생성하고, 사람은 바이너리를 렌더링된 형태로 보는 양방향 파이프라인 연구 프로젝트.

## Vision

```
현재:  사람 → 소스코드 작성 → 컴파일러 → 바이너리 → CPU 실행
미래:  사람 → 자연어 의도 → AI → 바이너리 → CPU 실행
                                      ↓
                              AI 렌더링 → 사람이 검토
```

프로그래밍 언어는 "사람이 기계에게 말하는 언어"였다.
렌더링은 "기계가 사람에게 말하는 언어"가 된다.

## Research Areas

### 1. Generation (자연어 → 바이너리)
- LLM이 어셈블리/LLVM-IR을 직접 생성
- 소스코드 단계를 건너뛴 바이너리 생성

### 2. Rendering (바이너리 → 사람이 읽는 표현)
- AI 디컴파일 (바이너리 → C 코드)
- 다단계 렌더링 (바이트 → 어셈블리 → 의사코드 → 자연어 → 의도)

### 3. Verification (AI 생성 바이너리 검증)
- 라운드트립 의미 보존도 측정
- Metamorphic testing
- 형식 검증 (Formal Verification)

## Tech Stack

- **실험**: Python + PyTorch + HuggingFace Transformers
- **코어**: Rust (Cargo workspace)
- **모델**: Nova, LLM4Decompile, CLAP, Meta LLM Compiler, Claude API
- **도구**: Ghidra, GCC/Clang/LLVM, NASM
- **문서**: Obsidian (`docs/`)

## Project Status

> Phase 0: Survey & Landscape (진행 중)

## License

MIT
