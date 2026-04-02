# Install NemoClaw

[NemoClaw Quick Start](https://docs.nvidia.com/nemoclaw/latest/get-started/quickstart.html)

```bash
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

```bash
nemoclaw onboard
```

```text
  NemoClaw Onboarding
  ===================

  [1/7] Preflight checks
  ──────────────────────────────────────────────────
  ✓ Docker is running
  ✓ Container runtime: docker-desktop
  ✓ openshell CLI: openshell 0.0.20
  ✓ Port 8080 available (OpenShell gateway)
  ✓ Port 18789 available (NemoClaw dashboard)
  ⓘ No GPU detected — will use cloud inference
  ✓ Memory OK: 14225 MB RAM + 4095 MB swap

  [2/7] Starting OpenShell gateway
  ──────────────────────────────────────────────────
  Using pinned OpenShell gateway image: ghcr.io/nvidia/openshell/cluster:0.0.20
✓ Checking Docker
✓ Downloading gateway
✓ Initializing environment
✓ Starting gateway                                                                                                                                         
✓ Gateway ready

  Name: nemoclaw
  Endpoint: https://127.0.0.1:8080

✓ Active gateway set to 'nemoclaw'
  ✓ Gateway is healthy
  Patching CoreDNS DNS forwarding...
Patching CoreDNS to forward to 192.168.1.254...
CoreDNS patched. Waiting for rollout...
Done. DNS should resolve in ~10 seconds.
✓ Active gateway set to 'nemoclaw'

  [3/7] Configuring inference (NIM)
  ──────────────────────────────────────────────────

  Inference options:
    1) NVIDIA Endpoints
    2) OpenAI
    3) Other OpenAI-compatible endpoint
    4) Anthropic
    5) Other Anthropic-compatible endpoint
    6) Google Gemini

  Choose [1]: 
```
