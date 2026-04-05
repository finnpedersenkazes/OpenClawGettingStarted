# Install NemoClaw

This page assumes you already completed the [NemoClaw Prerequisites](PreInstallation.md) and verified that all of the following work:

```bash
curl --version
docker version
docker run hello-world
openshell --version
node -v
npm -v
git --version
```

If any of those commands fail, go back to the [prerequisites page](PreInstallation.md) first.

## 1. Install NemoClaw

Run the official NVIDIA installer:

```bash
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

Expected result:

- Node.js is detected or installed
- the NemoClaw CLI is installed
- the command `nemoclaw --help` becomes available

If you use `nvm` or `fnm` and `nemoclaw` is not found immediately after installation, reload your shell:

```bash
source ~/.bashrc
nemoclaw --help
```

Reference: [NemoClaw Quick Start](https://docs.nvidia.com/nemoclaw/latest/get-started/quickstart.html)

## 2. Start onboarding

```bash
nemoclaw onboard
```

During onboarding, NemoClaw will typically:

1. Run preflight checks
2. Start the OpenShell gateway
3. Ask you to choose an inference provider
4. Create your first sandboxed OpenClaw assistant
5. Show you how to connect to that sandbox

On Ubuntu with Docker Engine, the preflight checks should report Docker as running and reachable.

## 3. What successful onboarding looks like

The exact wording may change over time, but a successful onboarding run should look roughly like this:

```text
NemoClaw Onboarding
===================

[1/7] Preflight checks
✓ Docker is running
✓ Container runtime: docker
✓ openshell CLI: openshell ...
✓ Port 8080 available (OpenShell gateway)
✓ Port 18789 available (NemoClaw dashboard)

[2/7] Starting OpenShell gateway
✓ Checking Docker
✓ Downloading gateway
✓ Initializing environment
✓ Starting gateway
✓ Gateway ready

[3/7] Choose an inference provider
...

[4/7] Creating your first sandbox
✓ Sandbox created

[5/7] Final verification
✓ Gateway healthy
✓ Sandbox reachable
```

## 4. Verify the gateway

```bash
openshell status
```

Expected:

```text
Server Status

  Gateway: nemoclaw
  Server: https://127.0.0.1:8080
  Status: Connected
  Version: ...
```

## 5. List your sandboxes

```bash
nemoclaw list
```

Expected:

```text
Sandboxes:
  my-assistant *
    model: claude-haiku-4-5  provider: anthropic-prod  CPU  policies: discord, docker, npm, pypi, telegram
```

`*` means the default sandbox.

## 6. Connect to your sandbox

```bash
nemoclaw my-assistant connect
```

Replace `my-assistant` with the actual sandbox name shown by `nemoclaw list`.

When connected, your prompt changes:

```bash
sandbox@my-assistant:~$
```

This is no longer your Ubuntu host. You are now inside the sandbox.

## Host vs sandbox

This distinction is important.

### On the host

Your prompt looks like this:

```bash
randall@your-computer:~$
```

Use the host for commands like `docker version`, `openshell status`, `nemoclaw list`, `nemoclaw onboard`.

### Inside the sandbox

Your prompt looks like this:

```bash
sandbox@my-assistant:~$
```

Use the sandbox for commands like `openclaw --version`, `openclaw update`.

Do not confuse the two environments when troubleshooting.

## Optional: update OpenClaw inside the sandbox

```bash
npm config set prefix ~/.local
export PATH="$HOME/.local/bin:$PATH"
npm i -g openclaw@latest
```

To make the path persistent:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## Troubleshooting

### `nemoclaw: command not found`

```bash
source ~/.bashrc
nemoclaw --help
```

### Permission denied on Docker socket

Your user is probably not yet active in the `docker` group.

```bash
groups
```

If `docker` is missing:

```bash
sudo usermod -aG docker $USER
```

Then log out and log back in before retrying.

### Stale Docker credential configuration

If Docker fails with a missing credential helper, check `~/.docker/config.json`. If it contains `"credsStore": "desktop"`, remove that line and retry:

```bash
docker run hello-world
```

### Sandbox listed locally but not present in the gateway

Check the live gateway, then list sandboxes again:

```bash
openshell status
nemoclaw list
```

If necessary, rerun onboarding:

```bash
nemoclaw onboard
```

## When you are ready

If all of the following work, your NemoClaw installation is successful:

```bash
openshell status
nemoclaw list
nemoclaw my-assistant connect
```

You are now ready to configure providers, connect channels, and continue with the next steps.
