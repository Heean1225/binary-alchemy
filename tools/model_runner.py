"""
model_runner.py - 다양한 모델의 추론을 통합하는 래퍼.

Usage:
    python tools/model_runner.py --model nova --input "int gcd(int a, int b)" --task decompile
    python tools/model_runner.py --model claude --input "gcd function" --task generate-asm
"""

import argparse
import json
import sys
from pathlib import Path


def run_huggingface(model_name: str, input_text: str, task: str, **kwargs) -> str:
    """HuggingFace 모델 추론 (Nova, LLM4Decompile, CLAP 등)."""
    try:
        from transformers import AutoModelForCausalLM, AutoTokenizer
        import torch
    except ImportError:
        return "ERROR: transformers/torch not installed. Run: pip install torch transformers"

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[model_runner] Loading {model_name} on {device}...")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    ).to(device)

    inputs = tokenizer(input_text, return_tensors="pt").to(device)
    max_new_tokens = kwargs.get("max_new_tokens", 512)

    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result


def run_claude(input_text: str, task: str, **kwargs) -> str:
    """Claude API를 통한 추론."""
    try:
        import anthropic
    except ImportError:
        return "ERROR: anthropic not installed. Run: pip install anthropic"

    client = anthropic.Anthropic()

    prompts = {
        "generate-asm": (
            f"Generate x86-64 assembly code for the following intent. "
            f"Output ONLY the assembly code, no explanation.\n\n{input_text}"
        ),
        "generate-c": (
            f"Generate C code for the following intent. "
            f"Output ONLY the C code, no explanation.\n\n{input_text}"
        ),
        "explain-asm": (
            f"Explain what the following assembly code does in plain language.\n\n{input_text}"
        ),
        "decompile": (
            f"Decompile the following assembly code to readable C code.\n\n{input_text}"
        ),
    }

    prompt = prompts.get(task, f"{task}\n\n{input_text}")

    message = client.messages.create(
        model=kwargs.get("claude_model", "claude-sonnet-4-20250514"),
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )

    return message.content[0].text


# 모델 이름 → HuggingFace ID 매핑
MODEL_REGISTRY = {
    "nova": "lt-asset/nova-1.3b",
    "llm4decompile": "LLM4Binary/llm4decompile-1.3b-v2",
    "llm-compiler": "facebook/llm-compiler-7b",
    "clap-asm": "Hustcw/clap-asm",
}


def main():
    parser = argparse.ArgumentParser(description="Binary Alchemy Model Runner")
    parser.add_argument("--model", required=True, help="Model name (nova, llm4decompile, claude, ...)")
    parser.add_argument("--input", required=True, help="Input text or file path")
    parser.add_argument("--task", required=True, help="Task (generate-asm, decompile, explain-asm, generate-c)")
    parser.add_argument("--output", help="Output file path (default: stdout)")
    parser.add_argument("--max-tokens", type=int, default=512)
    args = parser.parse_args()

    # 파일이면 읽기
    input_text = args.input
    if Path(input_text).exists():
        input_text = Path(input_text).read_text()

    # 실행
    if args.model == "claude":
        result = run_claude(input_text, args.task)
    elif args.model in MODEL_REGISTRY:
        result = run_huggingface(MODEL_REGISTRY[args.model], input_text, args.task, max_new_tokens=args.max_tokens)
    else:
        # 직접 HuggingFace ID로 시도
        result = run_huggingface(args.model, input_text, args.task, max_new_tokens=args.max_tokens)

    # 출력
    if args.output:
        Path(args.output).write_text(result)
        print(f"[model_runner] Output saved to {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
