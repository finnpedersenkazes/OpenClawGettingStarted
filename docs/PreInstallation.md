# Before installing OpenClaw

On a brand new computer or clean VM.

## Install Curl (Client URL)

```bash
sudo apt update
sudo apt install curl
```

## Install Node.js

https://nodejs.org/en/download

Copy paste the following into the terminal.

```bash
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash

# in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"

# Download and install Node.js:
nvm install 24

# Verify the Node.js version:
node -v # Should print "v24.14.0".

# Verify npm version:
npm -v # Should print "11.9.0".
```

## Homebrew

Many skill dependencies are shipped via Homebrew.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Install Git

```bash
sudo apt update
sudo apt install git
```

## Install Ollama

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

Then pull a lightweight model for local heartbeats:

```bash
ollama pull llama3.2:3b
```

If you want to verify it's working:

```bash
ollama serve
ollama run llama3.2:3b "respond with OK"
```

## Install OpenClaw

[Next up: Install OpenClaw](Installation.md)
