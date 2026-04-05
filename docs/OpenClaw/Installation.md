# Install OpenClaw

This page assumes you already completed the [OpenClaw Prerequisites](PreInstallation.md) and verified that all of the following work:

```bash
curl --version
node -v
npm -v
git --version
```

If any of those commands fail, go back to the [prerequisites page](PreInstallation.md) first.

## 1. Run the installer

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

## Installer output

```text
I'll butter your workflow like a lobster roll: messy, delicious, effective.

✓ Detected: linux

Install plan
OS: linux
Install method: npm
Requested version: latest

[1/3] Preparing environment
✓ Node.js v24.14.0 found
· Active Node.js: v24.14.0 (/home/alex/.nvm/versions/node/v24.14.0/bin/node)
· Active npm: 11.9.0 (/home/alex/.nvm/versions/node/v24.14.0/bin/npm)

[2/3] Installing OpenClaw
✓ Git already installed
· Installing OpenClaw v2026.3.13
✓ OpenClaw npm package installed
✓ OpenClaw installed

[3/3] Finalizing setup

! PATH missing npm global bin dir: /home/alex/.npm-global/bin
  This can make openclaw show as "command not found" in new terminals.
  Fix (zsh: ~/.zshrc, bash: ~/.bashrc):
    export PATH="/home/alex/.npm-global/bin:$PATH"

🦞 OpenClaw installed successfully (OpenClaw 2026.3.13 (61d171a))!
cracks claws Alright, what are we building?
```

## Security notice

```text
┌  OpenClaw onboarding
│
◇  Security ─────────────────────────────────────────────────────────╮
│                                                                    │
│  Security warning — please read.                                   │
│                                                                    │
│  OpenClaw is a hobby project and still in beta. Expect sharp       │
│  edges. By default, OpenClaw is a personal agent: one trusted      │
│  operator boundary. This bot can read files and run actions if     │
│  tools are enabled. A bad prompt can trick it into doing unsafe    │
│  things.                                                           │
│                                                                    │
│  Must read: https://docs.openclaw.ai/gateway/security              │
│                                                                    │
├────────────────────────────────────────────────────────────────────╯
│
◆  I understand this is personal-by-default and shared/multi-user
│  use requires lock-down. Continue?
│  ○ Yes / ● No
└
```

## Next step

Continue to [Onboarding](../Onboarding.md).
