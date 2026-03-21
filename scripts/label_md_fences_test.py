#!/usr/bin/env python3
"""Tests for label_md_fences.py (run: python -m unittest scripts.label_md_fences_test -v)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

# Allow `import label_md_fences` when running from repo root or from scripts/
_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

import label_md_fences as lmf  # noqa: E402


class TestClassifyFenceBody(unittest.TestCase):
    def test_empty_body_is_text(self) -> None:
        self.assertEqual(lmf.classify_fence_body(""), "text")
        self.assertEqual(lmf.classify_fence_body("\n\n"), "text")

    def test_json_is_json(self) -> None:
        self.assertEqual(
            lmf.classify_fence_body('{\n  "a": 1\n}'),
            "json",
        )

    def test_sudo_apt_is_bash(self) -> None:
        self.assertEqual(
            lmf.classify_fence_body("sudo apt update\nsudo apt install curl"),
            "bash",
        )

    def test_shell_comment_is_bash(self) -> None:
        self.assertEqual(
            lmf.classify_fence_body("# Download nvm:\ncurl -o- https://example.com/install.sh | bash"),
            "bash",
        )

    def test_single_line_path_is_text(self) -> None:
        self.assertEqual(lmf.classify_fence_body("~/.openclaw/openclaw.json"), "text")

    def test_ui_with_box_drawing_is_text(self) -> None:
        body = "◇  Onboarding\n│  Yes\n└"
        self.assertEqual(lmf.classify_fence_body(body), "text")

    def test_block_art_is_text(self) -> None:
        self.assertEqual(lmf.classify_fence_body("██ OPENCLAW ██\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀"), "text")

    def test_installer_log_is_text(self) -> None:
        body = "[1/3] Preparing environment\n✓ Node.js found"
        self.assertEqual(lmf.classify_fence_body(body), "text")

    def test_pairing_message_is_text(self) -> None:
        body = "Pairing code: abc123\n\nAsk the bot owner to approve with:\nopenclaw pairing approve x"
        self.assertEqual(lmf.classify_fence_body(body), "text")

    def test_openclaw_command_is_bash(self) -> None:
        self.assertEqual(lmf.classify_fence_body("openclaw security audit --deep"), "bash")

    def test_tui_transcript_is_text(self) -> None:
        self.assertEqual(
            lmf.classify_fence_body("openclaw tui - ws://127.0.0.1:18789"),
            "text",
        )

    def test_soul_md_template_is_md(self) -> None:
        body = "# SOUL.md\n\n## Core Principles\n\n[YOUR AGENT PRINCIPLES HERE]\n"
        self.assertEqual(lmf.classify_fence_body(body), "md")


class TestProcess(unittest.TestCase):
    def test_unlabeled_fence_gets_bash(self) -> None:
        src = """# Title

```
sudo apt update
sudo apt install curl
```
"""
        out = lmf.process(src)
        self.assertIn("```bash", out)
        self.assertIn("sudo apt update", out)
        self.assertNotIn("\n```\nsudo", out)

    def test_unlabeled_fence_gets_text_for_ui(self) -> None:
        src = """# Title

```
◇  Continue?
│  Yes
└
```
"""
        out = lmf.process(src)
        self.assertIn("```text", out)

    def test_labeled_bash_preserved(self) -> None:
        src = """```bash
echo hello
```
"""
        self.assertEqual(lmf.process(src), src)

    def test_mixed_labeled_and_unlabeled(self) -> None:
        src = """```bash
echo one
```
```
sudo apt update
```
"""
        out = lmf.process(src)
        self.assertIn("```bash\necho one", out)
        self.assertIn("sudo apt update", out)
        # Second block should be labeled
        self.assertIn("```bash", out)
        self.assertEqual(out.count("```bash"), 2)

    def test_preserves_lf_newlines(self) -> None:
        src = "# x\n\n```\ncurl https://x\n```\n"
        out = lmf.process(src)
        self.assertTrue(out.endswith("\n"))


if __name__ == "__main__":
    unittest.main()
