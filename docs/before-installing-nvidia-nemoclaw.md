## Before installing NVIDIA NemoClaw

The goal of this section is simple: make sure your computer is ready **before** you run the NemoClaw installer.

For **Ubuntu**, install **Docker Engine** with Docker’s own [install script](https://get.docker.com/). NVIDIA’s NemoClaw Quickstart expects **Docker** on Linux.

For first-time success on a fresh Ubuntu machine, make sure the following are in place before you continue:

- **Docker Engine** installed and running
- **OpenShell** installed
- **Node.js** 22.16 or later
- **npm** 10 or later

NVIDIA also notes that NemoClaw is currently **alpha software**, so it is normal for the docs and runtime behavior to change quickly.

### Docker Engine on Ubuntu

Do these steps **in this order**. After `usermod`, you must get a **new session** (log out, reconnect, or reboot) before `groups` will show `docker` and before `docker` works without `sudo`. OpenShell expects Docker to work for your normal user account.

1. **Install Docker** with Docker’s [Linux install script](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script) from [get.docker.com](https://get.docker.com/). It adds Docker’s package source and installs the current Docker Engine for your Ubuntu version.

   ```bash
   curl -fsSL https://get.docker.com | sudo sh
   ```

   `sudo` is required so the script can install packages. (You can [read the script on GitHub](https://github.com/docker/docker-install) before you run it.)

2. **Confirm the service is running** (still fine to use `sudo` here):

   ```bash
   sudo systemctl status docker --no-pager
   ```

   You want **`Active: active (running)`**.

3. **Let your user account use Docker without `sudo`** by adding it to the `docker` group. Run this once, right after Docker is installed:

   ```bash
   sudo usermod -aG docker $USER
   ```

4. **Start a new login session** so your user picks up the `docker` group. The session where you ran `usermod` **cannot** use Docker without `sudo` until you do this.

   - **Physical PC or VM with a desktop:** log out completely, then log back in. Or reboot: `sudo reboot`.
   - **SSH only:** disconnect all SSH sessions, then connect again. If it still fails, reboot the machine: `sudo reboot`.
   - **VM (VMware, etc.):** rebooting the guest is often the simplest way to be sure everything is fresh.

   Opening a **new terminal tab** in the same logged-in session is **not** enough on many systems.

5. **In the new session**, confirm the group before you run Docker:

   ```bash
   groups
   ```

   The output should include **`docker`**. If it does not, you are still in an old session — repeat step 4 (log out / reconnect / reboot). Do not expect `docker` to work until `groups` shows `docker`.

6. **Test Docker** without `sudo`:

   ```bash
   docker version
   docker run hello-world
   ```

   You should see both **Client** and **Server** in `docker version`, and `hello-world` should print `Hello from Docker!` If you still get permission denied on the socket, repeat steps 3–5.

   Optional quick check without rebooting (only if you cannot restart yet): `newgrp docker` in the current terminal, then try `docker run hello-world` again.

### OpenShell

Install OpenShell only **after** step 6 above works (Docker from a normal terminal, no `sudo`, and `groups` lists `docker`). The OpenShell installer expects a working `docker` command for your user.

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
