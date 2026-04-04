## Before installing NVIDIA NemoClaw

The goal of this section is simple: make sure your computer is ready **before** you run the NemoClaw installer.

For **Ubuntu**, use **Docker Engine**, not Docker Desktop. NVIDIA's current NemoClaw Quickstart lists **Docker** as the primary supported container runtime on Linux, while Docker Desktop is listed for macOS Apple Silicon and Windows WSL.

For first-time success on a fresh Ubuntu machine, make sure the following are in place before you continue:

- **Docker Engine** installed and running
- **OpenShell** installed
- **Node.js** 22.16 or later
- **npm** 10 or later

NVIDIA also notes that NemoClaw is currently **alpha software**, so it is normal for the docs and runtime behavior to change quickly.

### Docker Engine on Ubuntu

Install Docker Engine using Docker's Ubuntu packages.

```bash
sudo apt update
sudo apt install docker-ce
```

After installation, verify that the Docker service exists and is running:

```bash
sudo systemctl status docker --no-pager
```

Expected result:

- `Loaded: loaded`
- `Active: active (running)`

Then add your user to the `docker` group so you can run Docker without `sudo`:

```bash
sudo usermod -aG docker $USER
```

After running that command, **log out and back in** before continuing. Docker's Linux post-install documentation notes that group membership changes may require a new login session before they take effect.

When you are back in a fresh session, verify Docker:

```bash
docker version
```

Expected result:

- a **Client** section
- a **Server** section
- no permission error

Then run a real container test:

```bash
docker run hello-world
```

Expected result:

- Docker downloads the image if needed
- the output includes `Hello from Docker!`

### If you previously installed Docker Desktop on Linux

If you already tried Docker Desktop on Ubuntu before switching to Docker Engine, remove Docker Desktop completely before continuing. Docker's uninstall documentation warns that Docker Desktop can leave configuration behind, including credential helper and context settings.

Remove Docker Desktop:

```bash
sudo apt remove docker-desktop
```

After that, check for leftover Docker Desktop configuration in your shell files:

```bash
grep -n 'DOCKER_HOST\|desktop-linux\|docker/desktop/docker.sock' ~/.bashrc ~/.profile ~/.zshrc 2>/dev/null
```

If you find an old `DOCKER_HOST` export pointing to Docker Desktop, remove it.

Also inspect Docker's client configuration:

```bash
cat ~/.docker/config.json
```

If you see this:

```json
{
  "auths": {},
  "credsStore": "desktop",
  "currentContext": "default"
}
```

remove the `credsStore` entry, because it points to `docker-credential-desktop`, which is removed together with Docker Desktop. Docker documents that Docker Desktop uninstall on Linux may require manual cleanup of `credsStore` and `currentContext` in `~/.docker/config.json`.

A minimal cleaned-up file can look like this:

```json
{
  "auths": {},
  "currentContext": "default"
}
```

After cleanup, verify again:

```bash
docker version
docker run hello-world
```

### OpenShell

Install OpenShell after Docker Engine is working:

```bash
curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh
```

Verify that OpenShell is available:

```bash
openshell --version
```

Expected result:

- a version number is shown
- no `command not found` error

### Final verification before installing NemoClaw

Before moving to the NemoClaw installer, all of the following should work:

```bash
docker version
docker run hello-world
openshell --version
node -v
npm -v
```

If all five commands work, your Ubuntu machine is ready for the next step: installing NemoClaw.

### Note about `nemoclaw` not being found after installation

If you manage Node.js with `nvm` or `fnm`, NVIDIA notes that the installer may not update the current shell's `PATH` immediately. If `nemoclaw` is not found after installation, reload your shell configuration or open a new terminal:

```bash
source ~/.bashrc
nemoclaw --help
```

That is the easiest fix before assuming the installation failed.
