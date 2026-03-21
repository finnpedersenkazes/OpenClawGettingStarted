# Skills

An agent needs to have some skills to be able to act.

```text
◇  Skills status ─────────────╮
│                             │
│  Eligible: 4                │
│  Missing requirements: 41   │
│  Unsupported on this OS: 7  │
│  Blocked by allowlist: 0    │
│                             │
├─────────────────────────────╯
│
◆  Configure skills now? (recommended)
│  ● Yes / ○ No
└
```

You can choose to install some skills now or wait till later.

```text
◇  Configure skills now? (recommended)
│  Yes
│
◆  Install missing skill dependencies
│  ◻ Skip for now
│  ◼ 🔐 1password (Set up and use 1Password CLI (op). Use when installing the CLI, enabling desktop
│  app inte…)
│  ◻ 📰 blogwatcher
│  ◻ 🫐 blucli
│  ◻ 📸 camsnap
│  ◼ 🧩 clawhub (Use the ClawHub CLI to search, install, update, and publish agent skills from
│  clawhub.com…)
│  ◻ 🛌 eightctl
│  ◻ ✨ gemini
│  ◻ 🧲 gifgrep
│  ◼ 🐙 github (GitHub operations via `gh` CLI: issues, PRs, CI runs, code review, API queries. Use
│  when:…)
│  ◻ 🎮 gog
│  ◻ 📍 goplaces
│  ◻ 📧 himalaya
│  ◻ 📦 mcporter
│  ◻ 🍌 nano-banana-pro
│  ◻ 📄 nano-pdf
│  ◻ 💎 obsidian (Work with Obsidian vaults (plain Markdown notes) and automate via obsidian-cli. —
│  Install…)
│  ◻ 🎤 openai-whisper
│  ◻ 💡 openhue
│  ◻ 🧿 oracle
│  ◻ 🛵 ordercli
│  ◻ 🔊 sag
│  ◻ 🌊 songsee
│  ◻ 🔊 sonoscli
│  ◻ 🧾 summarize
│  ◻ 🎬 video-frames
│  ◻ 📱 wacli
│  ◻ 🐦 xurl
└
```

```text
◇  Install missing skill dependencies
│  🔐 1password, 🧩 clawhub, 🐙 github
│
```

## GitHub

We will use GitHub so it can back itself up.

## ClawHub

This is the place to find new skills.

## 1password

Is optional, but could prove useful.

## Homebrew

```text
◇  Homebrew recommended ──────────────────────────────────────────────────────────╮
│                                                                                 │
│  Many skill dependencies are shipped via Homebrew.                              │
│  Without brew, you'll need to build from source or download releases manually.  │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────╯
│
◆  Show Homebrew install command?
│  ● Yes / ○ No
└
```

> Normally you should have installed Homebrew during the [pre-installation](PreInstallation.md) phase.

If not do it now.

```text
◇  Homebrew install ─────────────────────────────────────────────────────╮
│                                                                        │
│  Run:                                                                  │
│  /bin/bash -c "$(curl -fsSL                                            │
│  https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"  │
│                                                                        │
├────────────────────────────────────────────────────────────────────────╯
│
```

### STOP - Run this command before continuing.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Preferred node manager

```text
◇  Preferred node manager for skill installs
│  npm
│
```

```text
◇  Set GOOGLE_PLACES_API_KEY for goplaces?
│  No
│
◇  Set GEMINI_API_KEY for nano-banana-pro?
│  No
│
◇  Set NOTION_API_KEY for notion?
│  No
│
◇  Set OPENAI_API_KEY for openai-image-gen?
│  No
│
◇  Set OPENAI_API_KEY for openai-whisper-api?
│  No
│
◇  Set ELEVENLABS_API_KEY for sag?
│  No
│
```

## Hooks

```text
◇  Hooks ──────────────────────────────────────────────────────────────────╮
│                                                                          │
│  Hooks let you automate actions when agent commands are issued.          │
│  Example: Save session context to memory when you issue /new or /reset.  │
│                                                                          │
│  Learn more: https://docs.openclaw.ai/automation/hooks                   │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────╯
│
◆  Enable hooks?
│  ◼ Skip for now
│  ◻ 🚀 boot-md
│  ◻ 📎 bootstrap-extra-files
│  ◻ 📝 command-logger
│  ◻ 💾 session-memory
└
```

## Finalizing

```text
◇  Systemd ────────────────────────────────────────────────────────────────────────────────╮
│                                                                                          │
│  Linux installs use a systemd user service by default. Without lingering, systemd stops  │
│  the user session on logout/idle and kills the Gateway.                                  │
│  Enabling lingering now (may require sudo; writes /var/lib/systemd/linger).              │
│                                                                                          │
├──────────────────────────────────────────────────────────────────────────────────────────╯
│
◇  Systemd ─────────────────────────────╮
│                                       │
│  Enabled systemd lingering for alex.  │
│                                       │
├───────────────────────────────────────╯
│
◇  Gateway service runtime ────────────────────────────────────────────╮
│                                                                      │
│  QuickStart uses Node for the Gateway service (stable + supported).  │
│                                                                      │
├──────────────────────────────────────────────────────────────────────╯
│
◓  Installing Gateway service…
Installed systemd service: /home/alex/.config/systemd/user/openclaw-gateway.service
◇  Gateway service installed.
│
◇
Telegram: ok (@bc_hacker_bot) (2803ms)
Agents: main (default)
Heartbeat interval: 30m (main)
Session store (main): /home/alex/.openclaw/agents/main/sessions/sessions.json (0 entries)
│
◇  Optional apps ────────────────────────╮
│                                        │
│  Add nodes for extra features:         │
│  - macOS app (system + notifications)  │
│  - iOS app (camera/canvas)             │
│  - Android app (camera/canvas)         │
│                                        │
├────────────────────────────────────────╯
│
◇  Control UI ─────────────────────────────────────────────────────────────────────╮
│                                                                                  │
│  Web UI: http://127.0.0.1:18789/                                                 │
│  Web UI (with token):                                                            │
│  http://127.0.0.1:18789/#token=14dabbefc1ea007c1491d179315b13c58c1200f515d5f2b3  │
│  Gateway WS: ws://127.0.0.1:18789                                                │
│  Gateway: reachable                                                              │
│  Docs: https://docs.openclaw.ai/web/control-ui                                   │
│                                                                                  │
├──────────────────────────────────────────────────────────────────────────────────╯
│
◇  Start TUI (best option!) ─────────────────────────────────╮
│                                                            │
│  This is the defining action that makes your agent you.    │
│  Please take your time.                                    │
│  The more you tell it, the better the experience will be.  │
│  We will send: "Wake up, my friend!"                       │
│                                                            │
├────────────────────────────────────────────────────────────╯
│
◇  Token ────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                            │
│  Gateway token: shared auth for the Gateway + Control UI.                                  │
│  Stored in: ~/.openclaw/openclaw.json (gateway.auth.token) or OPENCLAW_GATEWAY_TOKEN.      │
│  View token: openclaw config get gateway.auth.token                                        │
│  Generate token: openclaw doctor --generate-gateway-token                                  │
│  Web UI keeps dashboard URL tokens in memory for the current tab and strips them from the  │
│  URL after load.                                                                           │
│  Open the dashboard anytime: openclaw dashboard --no-open                                  │
│  If prompted: paste the token into Control UI settings (or use the tokenized dashboard     │
│  URL).                                                                                     │
│                                                                                            │
├────────────────────────────────────────────────────────────────────────────────────────────╯
│
◆  How do you want to hatch your bot?
│  ● Hatch in TUI (recommended)
│  ○ Open the Web UI
│  ○ Do this later
└
```

## TUI

```text
 openclaw tui - ws://127.0.0.1:18789 - agent main - session main

 session agent:main:main


 Wake up, my friend!


 Hey! I'm awake — and it looks like this is a fresh start. No memory files yet, no prior context. Clean slate.

 I noticed BOOTSTRAP.md is in the workspace, which means we haven't done the introductions yet. So — who are
 you? And what should I call you?
 connected | idle
 agent main | session main (openclaw-tui) | anthropic/claude-sonnet-4-6 | think adaptive | tokens ?/1.0m
───────────────────────────────────────────────────────────────────────────────────────────────────────────────
My name is Finn
```

```text
Your name is Alex
```

## Tools

[Next up: Tooling](Tools.md)
