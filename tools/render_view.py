"""
render_view.py - 바이너리의 다단계 렌더링 뷰 생성.

Usage:
    python tools/render_view.py --binary gcd.elf --output view.html
    python tools/render_view.py --binary gcd.elf --layers asm,decompile,explain
"""

import argparse
import html
import json
import subprocess
import sys
from pathlib import Path


def render_hex(binary: Path, limit: int = 512) -> str:
    """Layer 0: Hex dump."""
    data = binary.read_bytes()[:limit]
    lines = []
    for i in range(0, len(data), 16):
        hex_part = " ".join(f"{b:02X}" for b in data[i : i + 16])
        ascii_part = "".join(chr(b) if 32 <= b < 127 else "." for b in data[i : i + 16])
        lines.append(f"{i:08X}  {hex_part:<48}  {ascii_part}")
    return "\n".join(lines)


def render_asm(binary: Path) -> str:
    """Layer 1: Disassembly (objdump)."""
    r = subprocess.run(["objdump", "-d", str(binary)], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else f"objdump failed: {r.stderr}"


def render_decompile_stub(binary: Path) -> str:
    """Layer 2: Decompiled C (stub - 실제로는 LLM4Decompile 호출 필요)."""
    return (
        "// [Layer 2: Decompiled C]\n"
        "// TODO: LLM4Decompile 또는 Ghidra로 디컴파일 결과 채우기\n"
        "// python tools/model_runner.py --model llm4decompile --input <asm> --task decompile\n"
    )


def render_explain_stub(binary: Path) -> str:
    """Layer 3: Natural language explanation (stub - Claude API 호출 필요)."""
    return (
        "[Layer 3: Natural Language Explanation]\n"
        "TODO: Claude API로 어셈블리 설명 생성\n"
        "python tools/model_runner.py --model claude --input <asm> --task explain-asm\n"
    )


def generate_html(layers: dict, binary_name: str) -> str:
    """다단계 렌더링을 HTML로 통합."""
    tab_buttons = ""
    tab_contents = ""

    for i, (name, content) in enumerate(layers.items()):
        active_class = "active" if i == 0 else ""
        display = "block" if i == 0 else "none"
        escaped = html.escape(content)

        tab_buttons += f'<button class="tab-btn {active_class}" onclick="showTab(\'{name}\')">{name}</button>\n'
        tab_contents += f'<pre id="tab-{name}" class="tab-content" style="display:{display}">{escaped}</pre>\n'

    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Binary Alchemy - {binary_name}</title>
    <style>
        body {{ font-family: monospace; background: #1e1e1e; color: #d4d4d4; margin: 20px; }}
        h1 {{ color: #569cd6; }}
        .tab-bar {{ display: flex; gap: 4px; margin-bottom: 10px; }}
        .tab-btn {{
            padding: 8px 16px; border: 1px solid #555; background: #2d2d2d;
            color: #d4d4d4; cursor: pointer; border-radius: 4px 4px 0 0;
        }}
        .tab-btn.active {{ background: #1e1e1e; border-bottom: 2px solid #569cd6; color: #569cd6; }}
        .tab-content {{
            background: #1e1e1e; border: 1px solid #555; padding: 16px;
            overflow-x: auto; max-height: 600px; overflow-y: auto;
            line-height: 1.5;
        }}
        .info {{ color: #6a9955; margin-bottom: 10px; }}
    </style>
</head>
<body>
    <h1>Binary Alchemy Rendering View</h1>
    <div class="info">Binary: {binary_name}</div>
    <div class="tab-bar">
        {tab_buttons}
    </div>
    {tab_contents}
    <script>
        function showTab(name) {{
            document.querySelectorAll('.tab-content').forEach(el => el.style.display = 'none');
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
            document.getElementById('tab-' + name).style.display = 'block';
            event.target.classList.add('active');
        }}
    </script>
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="Binary Alchemy Render View")
    parser.add_argument("--binary", required=True, help="Binary file to render")
    parser.add_argument("--output", default="view.html", help="Output HTML file")
    parser.add_argument("--layers", default="hex,asm,decompile,explain",
                        help="Comma-separated layers to render")
    args = parser.parse_args()

    binary = Path(args.binary)
    if not binary.exists():
        print(f"ERROR: {binary} not found")
        sys.exit(1)

    available_layers = {
        "hex": render_hex,
        "asm": render_asm,
        "decompile": render_decompile_stub,
        "explain": render_explain_stub,
    }

    layers = {}
    for layer_name in args.layers.split(","):
        layer_name = layer_name.strip()
        if layer_name in available_layers:
            print(f"[render_view] Rendering layer: {layer_name}")
            layers[layer_name] = available_layers[layer_name](binary)
        else:
            print(f"[render_view] Unknown layer: {layer_name}, skipping")

    html_content = generate_html(layers, binary.name)
    Path(args.output).write_text(html_content)
    print(f"[render_view] View saved to {args.output}")


if __name__ == "__main__":
    main()
