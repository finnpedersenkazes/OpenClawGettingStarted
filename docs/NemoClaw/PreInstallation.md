# NemoClaw Prerequisites

This page covers what you need **before** running the NemoClaw installer on Ubuntu.

NemoClaw is currently **alpha software**, so it is normal for the docs and runtime behavior to change quickly.

## 1. Install curl

```bash
sudo apt update
sudo apt install curl
```

### Verify

```bash
curl --version
```

Expected: a version number and supported protocols. For example:

```text
curl 8.5.0 (x86_64-pc-linux-gnu) ...
```

## 2. Install Docker Engine

Do these steps in order. OpenShell expects Docker to work for your normal user account, not only with `sudo`.

Install Docker with Docker's [Linux install script](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script) from [get.docker.com](https://get.docker.com/):

```bash
curl -fsSL https://get.docker.com | sudo sh
```

`sudo` is required so the script can install packages. (You can [read the script on GitHub](https://github.com/docker/docker-install) before you run it.)

Confirm the service is running:

```bash
sudo systemctl status docker --no-pager
```

You want **`Active: active (running)`**.

Add your user to the `docker` group:

```bash
sudo usermod -aG docker $USER
```

Start a **new login session** so your user picks up the `docker` group. The session where you ran `usermod` cannot use Docker without `sudo` until you do this.

- **Physical PC or VM with a desktop:** log out completely, then log back in. Or reboot: `sudo reboot`.
- **SSH only:** disconnect all SSH sessions, then connect again. If it still fails, reboot: `sudo reboot`.
- **VM (VMware, etc.):** rebooting the guest is often the simplest approach.

Opening a new terminal tab in the same session is **not** enough on many systems.

In the new session, confirm the group:

```bash
groups
```

The output should include `docker`. If it does not, you are still in an old session -- log out and log back in again.

### Verify

```bash
docker version
docker run hello-world
```

Expected: `docker version` shows both **Client** and **Server**, and `hello-world` prints `Hello from Docker!`

```text
Client: Docker Engine - Community
 Version:           ...
Server: Docker Engine - Community
 Version:           ...

Hello from Docker!
```

## 3. Install OpenShell

Install OpenShell only **after** Docker works for your normal user account (step 2).

```bash
curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh
```

### Verify

```bash
openshell --version
```

Expected: a version number. For example:

```text
openshell 0.0.20
```

## 4. Install Node.js and npm

The easiest approach is [nvm](https://github.com/nvm-sh/nvm):

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

## 5. Install Git

```bash
sudo apt update
sudo apt install git
```

### Verify

```bash
git --version
```

Expected: a version number. For example:

```text
git version 2.43.0
```

## 6. Optional: Homebrew

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

## 7. Optional: Ollama

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
docker version
docker run hello-world
openshell --version
node -v
npm -v
git --version
```

Expected results:

| Command | Expected |
| --- | --- |
| `curl --version` | Version number and protocols |
| `docker version` | Shows both Client and Server |
| `docker run hello-world` | Prints `Hello from Docker!` |
| `openshell --version` | Version number |
| `node -v` | `v24.14.0` or later |
| `npm -v` | `11.9.0` or later |
| `git --version` | Version number |

If any command fails, go back to the corresponding step above.

## Troubleshooting

### `nemoclaw: command not found` after installation

If you manage Node.js with `nvm` or `fnm`, the installer may not update the current shell's PATH immediately. Reload your shell:

```bash
source ~/.bashrc
nemoclaw --help
```

### Docker permission denied

If Docker fails with `permission denied ... /var/run/docker.sock`, your user is not yet active in the `docker` group. Check with `groups` and repeat step 2 (usermod + new login session).

### Stale Docker credentials

If Docker fails with a missing credential helper (e.g. `docker-credential-desktop`), inspect `~/.docker/config.json` and remove the `credsStore` line, then retry `docker run hello-world`.

### `nvm: command not found`

If `nvm` is not found after installing it, reload your shell:

```bash
source ~/.bashrc
nvm --version
```

### `git: command not found`

On Ubuntu, install with `sudo apt install git`. Then verify with `git --version`.

## Next step

Continue to [Install NemoClaw](Installation.md).
