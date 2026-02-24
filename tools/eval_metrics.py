"""
eval_metrics.py - Binary Alchemy 평가 메트릭 계산.

Usage:
    python tools/eval_metrics.py pass1 --generated out.s --test test_gcd.py
    python tools/eval_metrics.py reexec --original src.c --decompiled decompiled.c
    python tools/eval_metrics.py semantic --text1 "gcd function" --text2 "computes greatest common divisor"
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path


def pass_at_1(generated_asm: Path, test_script: Path) -> dict:
    """Pass@1: 생성된 어셈블리를 어셈블+실행하여 테스트 통과 여부 확인."""
    binary = generated_asm.with_suffix(".elf")

    # 어셈블
    obj = generated_asm.with_suffix(".o")
    r1 = subprocess.run(["as", "-o", str(obj), str(generated_asm)], capture_output=True)
    if r1.returncode != 0:
        return {"metric": "pass@1", "passed": False, "error": "assembly_failed", "detail": r1.stderr.decode()}

    r2 = subprocess.run(["ld", "-o", str(binary), str(obj)], capture_output=True)
    obj.unlink(missing_ok=True)
    if r2.returncode != 0:
        return {"metric": "pass@1", "passed": False, "error": "link_failed", "detail": r2.stderr.decode()}

    # 테스트 실행
    r3 = subprocess.run(["python", str(test_script), str(binary)], capture_output=True, text=True, timeout=30)
    binary.unlink(missing_ok=True)

    return {
        "metric": "pass@1",
        "passed": r3.returncode == 0,
        "stdout": r3.stdout[:500],
        "stderr": r3.stderr[:500] if r3.returncode != 0 else "",
    }


def re_executability(original_c: Path, decompiled_c: Path) -> dict:
    """Re-executability: 디컴파일된 C를 재컴파일+실행 가능 여부."""
    binary = decompiled_c.with_suffix(".reexec")

    # 재컴파일
    r = subprocess.run(
        ["gcc", "-o", str(binary), str(decompiled_c), "-lm"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        return {
            "metric": "re-executability",
            "compilable": False,
            "executable": False,
            "error": r.stderr[:500],
        }

    # 실행 가능 여부
    r2 = subprocess.run([str(binary)], capture_output=True, timeout=10)
    binary.unlink(missing_ok=True)

    return {
        "metric": "re-executability",
        "compilable": True,
        "executable": r2.returncode == 0 or r2.returncode != -11,  # not segfault
    }


def bleu_score(reference: str, hypothesis: str) -> dict:
    """BLEU score between reference and hypothesis text."""
    try:
        import sacrebleu
        result = sacrebleu.sentence_bleu(hypothesis, [reference])
        return {"metric": "bleu", "score": result.score, "bp": result.bp}
    except ImportError:
        return {"metric": "bleu", "error": "sacrebleu not installed"}


def semantic_similarity(text1: str, text2: str) -> dict:
    """CLAP 기반 또는 간단한 임베딩 코사인 유사도."""
    try:
        from sentence_transformers import SentenceTransformer, util
        model = SentenceTransformer("all-MiniLM-L6-v2")
        emb1 = model.encode(text1, convert_to_tensor=True)
        emb2 = model.encode(text2, convert_to_tensor=True)
        score = util.cos_sim(emb1, emb2).item()
        return {"metric": "semantic_similarity", "score": score, "model": "all-MiniLM-L6-v2"}
    except ImportError:
        return {"metric": "semantic_similarity", "error": "sentence-transformers not installed"}


def main():
    parser = argparse.ArgumentParser(description="Binary Alchemy Evaluation Metrics")
    subparsers = parser.add_subparsers(dest="command")

    # pass@1
    p1 = subparsers.add_parser("pass1", help="Test if generated assembly passes tests")
    p1.add_argument("--generated", required=True, help="Generated assembly file")
    p1.add_argument("--test", required=True, help="Test script")

    # re-executability
    p2 = subparsers.add_parser("reexec", help="Test if decompiled code is re-executable")
    p2.add_argument("--original", required=True, help="Original C file")
    p2.add_argument("--decompiled", required=True, help="Decompiled C file")

    # BLEU
    p3 = subparsers.add_parser("bleu", help="BLEU score between two texts")
    p3.add_argument("--reference", required=True)
    p3.add_argument("--hypothesis", required=True)

    # Semantic similarity
    p4 = subparsers.add_parser("semantic", help="Semantic similarity between two texts")
    p4.add_argument("--text1", required=True)
    p4.add_argument("--text2", required=True)

    args = parser.parse_args()

    if args.command == "pass1":
        result = pass_at_1(Path(args.generated), Path(args.test))
    elif args.command == "reexec":
        result = re_executability(Path(args.original), Path(args.decompiled))
    elif args.command == "bleu":
        ref = Path(args.reference).read_text() if Path(args.reference).exists() else args.reference
        hyp = Path(args.hypothesis).read_text() if Path(args.hypothesis).exists() else args.hypothesis
        result = bleu_score(ref, hyp)
    elif args.command == "semantic":
        result = semantic_similarity(args.text1, args.text2)
    else:
        parser.print_help()
        sys.exit(1)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
