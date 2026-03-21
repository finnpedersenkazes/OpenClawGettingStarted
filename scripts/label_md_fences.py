#!/usr/bin/env python3
"""Add language tags to unlabeled Markdown fenced code blocks in docs/.

Tests: label_md_fences_test.py (run: python -m unittest discover -s scripts -p label_md_fences_test.py -v)
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def classify_fence_body(body: str) -> str:
    s = body.strip("\n")
    if not s:
        return "text"
    lines = [ln for ln in s.splitlines() if ln.strip()]
    first = lines[0] if lines else ""

    if first.strip().startswith("{"):
        return "json"

    if first.strip().startswith("# ") and ("SOUL.md" in s or "USER.md" in s):
        return "md"

    # TUI / transcripts / ASCII UI (anywhere in block) — before shell heuristics
    box_chars = (
        "\u2502",
        "\u251c",
        "\u2514",
        "\u2570",
        "\u250c",
        "\u2500",
        "\u2550",
        "\u2551",
        "\u256d",
        "\u256e",
        "\u256f",
        "\u2570",
        "\u252c",
        "\u2534",
        "\u253c",
    )
    if any(ch in s for ch in box_chars):
        return "text"
    if any(ch in s for ch in ("┌", "├", "└", "│", "◇", "◆")):
        return "text"
    # Dense ASCII / block art (e.g. OpenClaw banner)
    if any(ch in s for ch in ("█", "▄", "▀", "░", "▒", "▓")):
        return "text"

    bullets = ("\u25c7", "\u25c6", "\u25cb", "\u25cf")
    if first.lstrip().startswith(bullets):
        return "text"

    if "\u2713" in s or "[1/3]" in s or "Install plan" in s:
        return "text"

    # Single-line path / file reference (not a shell session)
    if len(lines) == 1 and first.startswith("~") and "/" in first:
        return "text"

    if "openclaw tui" in s or "session agent:" in s or "connected | idle" in s:
        return "text"

    if first.strip() in ("Your name is Alex",):
        return "text"

    # Bot / app messages (not a shell session)
    if "Pairing code:" in s or "Ask the bot owner" in s:
        return "text"

    shellish = (
        "sudo ",
        "apt ",
        "curl ",
        "nvm ",
        "npm ",
        "node ",
        "git ",
        "ollama",
        "export ",
        "bash ",
        "/bin/bash",
        "alex@",
        ":~$",
    )
    # Only treat `openclaw` as shell when it looks like a command invocation
    if "openclaw " in s or s.strip().startswith("openclaw"):
        if not any(ch in s for ch in box_chars + ("│", "◇", "◆", "┌", "├", "└")):
            return "bash"

    if any(k in s for k in shellish):
        return "bash"

    for ln in lines[:5]:
        t = ln.strip()
        if t.startswith(("# ", "$ ", "cd ", "chmod ")):
            return "bash"

    return "text"


def process(text: str) -> str:
    out: list[str] = []
    lines = text.splitlines(keepends=True)
    i = 0
    in_fence = False

    while i < len(lines):
        line = lines[i]
        raw = line.rstrip("\r\n")

        if raw.startswith("```"):
            lang_part = raw[3:].strip()

            if in_fence:
                # Closing fence
                out.append(line)
                in_fence = False
                i += 1
                continue

            # Opening fence
            if lang_part != "":
                out.append(line)
                in_fence = True
                i += 1
                continue

            # Unlabeled opening ``` : read body until closing ```
            j = i + 1
            body_lines: list[str] = []
            while j < len(lines):
                r2 = lines[j].rstrip("\r\n")
                if r2 == "```":
                    break
                body_lines.append(lines[j])
                j += 1

            if j >= len(lines):
                out.append(line)
                i += 1
                continue

            body = "".join(body_lines)
            lang2 = classify_fence_body(body)
            nl = "\r\n" if line.endswith("\r\n") else "\n"
            out.append(f"```{lang2}{nl}")
            out.extend(body_lines)
            out.append(lines[j])
            i = j + 1
            continue

        out.append(line)
        i += 1

    return "".join(out)


def main() -> None:
    for path in sorted(DOCS.glob("*.md")):
        orig = path.read_text(encoding="utf-8")
        new = process(orig)
        if new != orig:
            path.write_text(new, encoding="utf-8")
            print("updated", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
