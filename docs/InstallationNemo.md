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

  ┌─────────────────────────────────────────────────────────────────┐
  │  NVIDIA API Key required                                        │
  │                                                                 │
  │  1. Go to https://build.nvidia.com/settings/api-keys            │
  │  2. Sign in with your NVIDIA account                            │
  │  3. Click 'Generate API Key' button                             │
  │  4. Paste the key below (starts with nvapi-)                    │
  └─────────────────────────────────────────────────────────────────┘

  NVIDIA API Key: **********************************************************************

  Key saved to ~/.nemoclaw/credentials.json (mode 600)


  Cloud models:
    1) Nemotron 3 Super 120B (nvidia/nemotron-3-super-120b-a12b)
    2) Kimi K2.5 (moonshotai/kimi-k2.5)
    3) GLM-5 (z-ai/glm5)
    4) MiniMax M2.5 (minimaxai/minimax-m2.5)
    5) GPT-OSS 120B (openai/gpt-oss-120b)
    6) Other...

  Choose model [1]: 
  Responses API available — OpenClaw will use openai-responses.
  Using NVIDIA Endpoints with model: nvidia/nemotron-3-super-120b-a12b

  [4/7] Setting up inference provider
  ──────────────────────────────────────────────────
✓ Active gateway set to 'nemoclaw'
✓ Created provider nvidia-prod
Gateway inference configured:

  Route: inference.local
  Provider: nvidia-prod
  Model: nvidia/nemotron-3-super-120b-a12b
  Version: 1
  Timeout: 60s (default)
  ✓ Inference route set: nvidia-prod / nvidia/nemotron-3-super-120b-a12b

```
