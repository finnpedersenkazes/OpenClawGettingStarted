# Host

Chose one of the following hosts for your OpenClaw or NVIDIA NemoClaw installation.

The the **Mac mini** is the YouTube blogger darling.

## OpenClaw on Dedicated Ubuntu Computer

[Next up: Choose your AI model.](Models.md)

## OpenClaw on Virtual Ubuntu on Windows 11

- Install VMware Workstation Pro 25
- Get Ubuntu 25 iso
- Standard configuration
- Install updates

| Hardware Requirements | Recommended |
| --------------------- | ----------- |
| CPU                   | 4+ vCPU     |
| RAM                   | 16 GB       |
| Disk                  | 40 GB       |

- **Number of processors:** 1
- **Number of cores per processor:** 8
- Total processor cores: 8
- Virtulalization Engine
  - Virtualize AMD-V/RVI: No
  - Virtualize CPU performance counters: No

[Next up: Choose your AI model.](Models.md)

## OpenClaw on Dedicated Mac mini

[Next up: Choose your AI model.](Models.md)

## OpenClaw Virtual macOS on macOS

_We did not find a good solutions for this._

## OpenClaw Virtual Ubuntu on macOS

- Install VMware Fusion Pro 25
- Get Ubuntu 25 iso
- Standard configuration
- Install updates

[Next up: Choose your AI model.](Models.md)

## Virtual Private Server (VPS) on Hostinger

Hostinger has 1-click OpenClaw hosting deal that should get you started without buying a physical computer.

[OpenClaw hosting on Hostinger.com](https://www.hostinger.com/dk/vps/openclaw-hosting)

## NVIDIA NemoClaw on NVIDIA Brev

Go to https://www.nvidia.com/en-us/ai/nemoclaw/ and press `Try It Now`.

## NVIDIA NemoClaw on Dedicated Ubuntu computer

### Prerequisites

| Hardware Requirements | Recommended |
| --------------------- | ----------- |
| CPU                   | 4+ vCPU     |
| RAM                   | 16 GB       |
| Disk                  | 40 GB       |

| Software Dependencies | Version                   |
| --------------------- | ------------------------- |
| Linux                 | Ubuntu 22.04 LTS or later |
| Node.js               | 22.16 or later            |
| npm                   | 10 or later               |
| Docker Engine         | Installed and running     |
| OpenShell             | Installed                 |

## OpenClaw on Dedicated Windows Computer

_We do not recommend installing OpenClaw on Windows._

## OpenClaw on Dedicated Raspberry Pi

_We have not tested it yet, but it should be possible on the latest version 4 and 5._

Most sources uses Raspberry Pi OS, but some uses Ubuntu.

## Choose your host

NVIDIA NemoClaw can run on several different kinds of hosts, but not all paths are equally mature.

For a first successful installation, use a host that matches NVIDIA's documented runtime expectations and that you can manage comfortably. On Linux, that means using **Docker Engine** rather than Docker Desktop. NVIDIA's Quickstart lists **Docker** as the primary supported runtime on Linux. citeturn197817view1

This page separates:

- **recommended and tested paths**
- **cloud GPU paths**
- **experimental or not-yet-tested paths**

## Recommended and tested paths

### Dedicated Ubuntu computer

This is the most straightforward host if you want to run NemoClaw on your own machine.

A good example is a dedicated Ubuntu installation on a Lenovo laptop or desktop computer.

Recommended characteristics:

- Ubuntu installed directly on the machine
- Docker Engine installed and running
- OpenShell installed
- Node.js and npm available
- enough RAM for normal development work
- reliable internet access

For Ubuntu, verify Docker Engine with:

```bash
docker version
sudo systemctl status docker --no-pager
docker run hello-world
```

Expected result:

- `docker version` shows both **Client** and **Server**
- `docker.service` is active
- `docker run hello-world` prints `Hello from Docker!`

This is the path I recommend for first-time Linux users because it matches the standard Linux Docker model used in NVIDIA's documentation. citeturn197817view1turn197817view2

### Apple Mac mini with Apple Silicon

A Mac mini can also be a good dedicated host, especially if you already use one as a stable always-on machine.

Typical advantages:

- quiet
- low power consumption
- reliable hardware
- good fit for a permanent home lab setup

On macOS Apple Silicon, NVIDIA's Quickstart lists **Docker Desktop** as the supported runtime path. citeturn197817view1

This can be a good choice if:

- you want a quiet machine running all the time
- you are already comfortable administering macOS
- you do not need NVIDIA GPU acceleration on the host itself

## Cloud GPU path

### NVIDIA Brev

NVIDIA Brev is the cloud-oriented path when you want access to a remote NVIDIA GPU environment.

Use this path if you want:

- remote GPU resources
- a cloud sandbox environment
- an easier route to NVIDIA infrastructure than building everything yourself

This is especially relevant when your local machine does not have a suitable NVIDIA GPU, or when you want to separate your assistant environment from your everyday computer.

A Brev host is conceptually different from a local Ubuntu or Mac host:

- the machine is remote
- the hardware is rented
- the environment is more disposable
- GPU access is the main reason to choose it

That makes Brev attractive for testing GPU-based workflows, model serving, or demo environments.

## Other possible hosts

### Virtual machines

A virtual machine can work, but it adds another layer of complexity.

Use a VM only if:

- you specifically want isolation from your daily machine
- you are comfortable debugging both the guest OS and the virtualization layer
- you accept that networking, Docker, and USB/GPU behavior may be more complicated

A VM can still be a good option for demos or experiments, but it is usually not the easiest path for a first installation.

### Raspberry Pi

A Raspberry Pi is interesting as an experimental low-power host, but I do not recommend it as the primary getting-started path unless you have personally validated the exact model and operating system combination.

Use this category only if you are intentionally experimenting.

## What I recommend for most readers

If your goal is:

### The easiest Linux path

Choose:

- **Dedicated Ubuntu computer**
- **Docker Engine**
- **OpenShell**
- **NemoClaw**

### A quiet always-on local machine

Choose:

- **Mac mini**
- **Docker Desktop**
- **OpenShell**
- **NemoClaw**

### Remote GPU access

Choose:

- **NVIDIA Brev**

## What to avoid on Ubuntu for the first run

For Ubuntu, avoid Docker Desktop as the default recommendation.

Docker Desktop on Linux can work in some situations, but it uses a different socket model than standard Docker Engine, and that can create avoidable onboarding problems for tools that expect the normal Linux Docker daemon. The simplest documentation path is therefore:

- Ubuntu -> Docker Engine
- macOS Apple Silicon -> Docker Desktop

That matches NVIDIA's current Quickstart more closely and reduces first-run confusion. citeturn197817view1turn197817view2

## Summary

If you want the smoothest first installation experience:

1. use a dedicated Ubuntu machine or a Mac mini
2. on Ubuntu, use Docker Engine
3. on macOS Apple Silicon, use Docker Desktop
4. use NVIDIA Brev when remote GPU access is the main goal

Once you have chosen the host, continue to the **Pre-installation** page.
