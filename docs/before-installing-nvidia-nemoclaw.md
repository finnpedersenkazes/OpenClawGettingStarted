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

Do these steps **in this order**. Skip nothing: the `docker` group step only works after a **full log out and log back in** (or reboot), and OpenShell expects Docker to work for your normal user account.

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

4. **Log out of your desktop session and log back in** (or restart the computer). Until you do, your current session **does not** see the new group, and `docker` will keep failing with permission errors when you are not root. Opening a new terminal is not always enough; a full session restart is the reliable fix.

5. **In that new session**, check Docker **without** `sudo`:

   ```bash
   docker version
   docker run hello-world
   ```

   You should see both **Client** and **Server** in `docker version`, and `hello-world` should print `Hello from Docker!` If you still get permission denied on the socket, repeat step 3 and step 4.

### OpenShell

Install OpenShell only **after** step 5 above works (Docker from a normal terminal, no `sudo`). The OpenShell installer expects a working `docker` command for your user.

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
