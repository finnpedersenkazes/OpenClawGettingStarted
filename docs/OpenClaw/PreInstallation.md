# OpenClaw Prerequisites

This page covers what you need **before** running the OpenClaw installer. It applies to dedicated Ubuntu, dedicated macOS, and Ubuntu VMs.

You do **not** need Docker or OpenShell for the basic OpenClaw path.

## 1. Install curl

### Ubuntu

```bash
sudo apt update
sudo apt install curl
```

### macOS

curl is pre-installed on macOS.

### Verify

```bash
curl --version
```

Expected: a version number and supported protocols. For example:

```text
curl 8.5.0 (x86_64-pc-linux-gnu) ...
```

## 2. Install Node.js and npm

The easiest cross-platform approach is [nvm](https://github.com/nvm-sh/nvm):

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
```

Reload the shell so `nvm` is available:

```bash
\. "$HOME/.nvm/nvm.sh"
```

Install Node.js (npm is included):

```bash
nvm install 24
```

### Verify

```bash
node -v
npm -v
```

Expected:

```text
v24.14.0
11.9.0
```

## 3. Install Git

You must install Git before Homebrew.

### Ubuntu

```bash
sudo apt update
sudo apt install git
```

### macOS

Option 1 -- Xcode Command Line Tools (recommended, includes Git):

```bash
xcode-select --install
```

Option 2 -- via Homebrew (if you prefer Homebrew-managed Git):

```bash
brew install git
```

### Verify

```bash
git --version
```

Expected: a version number. For example:

```text
git version 2.43.0
```

## 4. Optional: Homebrew

Many skill dependencies are shipped via Homebrew, but it is not required for the initial install.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After install, follow the on-screen instructions to add Homebrew to your PATH.

### Verify

```bash
brew --version
```

Expected: a version number. For example:

```text
Homebrew 4.4.17
```

## 5. Optional: Ollama

Install Ollama only if you want local models instead of a hosted provider.

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

Pull a lightweight model for local heartbeats:

```bash
ollama pull llama3.2:3b
```

### Verify

```bash
ollama --version
```

Expected: a version number. For example:

```text
ollama version 0.6.2
```

## Final check

Before continuing, run all of the following commands. Every one should succeed:

```bash
curl --version
node -v
npm -v
git --version
```

Expected results:

| Command | Expected |
| --- | --- |
| `curl --version` | Version number and protocols |
| `node -v` | `v24.14.0` or later |
| `npm -v` | `11.9.0` or later |
| `git --version` | Version number |

If any command fails, go back to the corresponding step above.

## Troubleshooting

### `openclaw: command not found` after installation

If you manage Node.js with `nvm` or `fnm`, the installer may not update the current shell's PATH immediately. Reload your shell:

```bash
source ~/.bashrc
openclaw --version
```

If `openclaw` is still not found, check if the npm global bin directory is in your PATH:

```bash
npm config get prefix
```

Add the `bin` subdirectory to your PATH. For example:

```bash
export PATH="$(npm config get prefix)/bin:$PATH"
```

### `nvm: command not found`

If `nvm` is not found after installing it, reload your shell:

```bash
source ~/.bashrc
nvm --version
```

### `git: command not found`

On Ubuntu, install with `sudo apt install git`. On macOS, install with `xcode-select --install`. Then verify with `git --version`.

### Homebrew not found after installation

Homebrew prints instructions at the end of its install script telling you how to add it to your PATH. If you missed them, run:

```bash
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```

On macOS Apple Silicon:

```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```

## Next step

Continue to [Install OpenClaw](Installation.md).
