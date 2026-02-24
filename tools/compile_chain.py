"""
compile_chain.py - C→gcc→binary→objdump 자동화 체인.

Usage:
    python tools/compile_chain.py --input test.c --output test.elf --dump
    python tools/compile_chain.py --asm test.s --output test.elf
"""

import argparse
import subprocess
import sys
from pathlib import Path


def compile_c(c_file: Path, output: Path, opt_level: str = "-O2") -> bool:
    """C 파일을 컴파일하여 ELF 바이너리 생성."""
    cmd = ["gcc", opt_level, "-o", str(output), str(c_file)]
    print(f"[compile_chain] {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[compile_chain] ERROR: {result.stderr}", file=sys.stderr)
        return False
    print(f"[compile_chain] Compiled: {output} ({output.stat().st_size} bytes)")
    return True


def assemble(asm_file: Path, output: Path) -> bool:
    """어셈블리 파일을 어셈블+링크하여 ELF 바이너리 생성."""
    obj_file = output.with_suffix(".o")

    # 어셈블
    cmd_as = ["as", "-o", str(obj_file), str(asm_file)]
    print(f"[compile_chain] {' '.join(cmd_as)}")
    result = subprocess.run(cmd_as, capture_output=True, text=True)
    if result.returncode != 0:
        # NASM 시도
        cmd_nasm = ["nasm", "-f", "elf64", "-o", str(obj_file), str(asm_file)]
        print(f"[compile_chain] as failed, trying NASM: {' '.join(cmd_nasm)}")
        result = subprocess.run(cmd_nasm, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"[compile_chain] ERROR: {result.stderr}", file=sys.stderr)
            return False

    # 링크
    cmd_ld = ["ld", "-o", str(output), str(obj_file)]
    print(f"[compile_chain] {' '.join(cmd_ld)}")
    result = subprocess.run(cmd_ld, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[compile_chain] ERROR: {result.stderr}", file=sys.stderr)
        return False

    print(f"[compile_chain] Assembled: {output} ({output.stat().st_size} bytes)")
    obj_file.unlink(missing_ok=True)
    return True


def objdump(binary: Path, output: Path | None = None) -> str:
    """바이너리를 디스어셈블."""
    cmd = ["objdump", "-d", str(binary)]
    print(f"[compile_chain] {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[compile_chain] ERROR: {result.stderr}", file=sys.stderr)
        return ""

    if output:
        output.write_text(result.stdout)
        print(f"[compile_chain] Disassembly saved to {output}")
    return result.stdout


def hexdump(binary: Path, limit: int = 256) -> str:
    """바이너리의 hex dump."""
    data = binary.read_bytes()[:limit]
    lines = []
    for i in range(0, len(data), 16):
        hex_part = " ".join(f"{b:02X}" for b in data[i : i + 16])
        ascii_part = "".join(chr(b) if 32 <= b < 127 else "." for b in data[i : i + 16])
        lines.append(f"{i:08X}  {hex_part:<48}  {ascii_part}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Binary Alchemy Compile Chain")
    parser.add_argument("--input", help="C source file")
    parser.add_argument("--asm", help="Assembly source file")
    parser.add_argument("--output", required=True, help="Output binary path")
    parser.add_argument("--opt", default="-O2", help="Optimization level (default: -O2)")
    parser.add_argument("--dump", action="store_true", help="Also run objdump")
    parser.add_argument("--hex", action="store_true", help="Also show hex dump")
    args = parser.parse_args()

    output = Path(args.output)

    if args.input:
        success = compile_c(Path(args.input), output, args.opt)
    elif args.asm:
        success = assemble(Path(args.asm), output)
    else:
        print("ERROR: --input (C file) or --asm (assembly file) required")
        sys.exit(1)

    if not success:
        sys.exit(1)

    if args.dump:
        disasm = objdump(output, output.with_suffix(".dump"))
        print("\n--- Disassembly ---")
        print(disasm[:2000])

    if args.hex:
        hd = hexdump(output)
        print("\n--- Hex Dump ---")
        print(hd)


if __name__ == "__main__":
    main()
