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
```text
  [5/7] Creating sandbox
  ──────────────────────────────────────────────────
  Sandbox name (lowercase, numbers, hyphens) [my-assistant]: nemoclaw-sandbox
  Creating sandbox 'nemoclaw-sandbox' (this takes a few minutes on first run)...
  Building image openshell/sandbox-from:1775161084 from /tmp/nemoclaw-build-fVVTwG/Dockerfile
  Step 1/36 : ARG BASE_IMAGE=ghcr.io/nvidia/nemoclaw/sandbox-base:latest
  Step 2/36 : FROM node:22-slim@sha256:4f77a690f2f8946ab16fe1e791a3ac0667ae1c3575c3e4d0d4589e9ed5bfaf3d AS builder
  Step 3/36 : COPY nemoclaw/package.json nemoclaw/tsconfig.json /opt/nemoclaw/
  Step 4/36 : COPY nemoclaw/src/ /opt/nemoclaw/src/
  Step 5/36 : WORKDIR /opt/nemoclaw
  Step 6/36 : RUN npm install && npm run build
  Step 7/36 : FROM ${BASE_IMAGE}
  Still building sandbox image... (60s elapsed)
  Still building sandbox image... (75s elapsed)
  Still building sandbox image... (90s elapsed)
  Still building sandbox image... (105s elapsed)
  Still building sandbox image... (120s elapsed)
  Still building sandbox image... (135s elapsed)
  Step 8/36 : RUN (apt-get remove --purge -y gcc gcc-12 g++ g++-12 cpp cpp-12 make         netcat-openbsd netcat-traditional ncat 2>/dev/null || true)     && apt-get autoremove --purge -y     && rm -rf /var/lib/apt/lists/*
  Step 9/36 : COPY --from=builder /opt/nemoclaw/dist/ /opt/nemoclaw/dist/
  Step 10/36 : COPY nemoclaw/openclaw.plugin.json /opt/nemoclaw/
  Step 11/36 : COPY nemoclaw/package.json nemoclaw/package-lock.json /opt/nemoclaw/
  Step 12/36 : COPY nemoclaw-blueprint/ /opt/nemoclaw-blueprint/
  Step 13/36 : WORKDIR /opt/nemoclaw
  Step 14/36 : RUN npm ci --omit=dev
  Step 15/36 : RUN mkdir -p /sandbox/.nemoclaw/blueprints/0.1.0     && cp -r /opt/nemoclaw-blueprint/* /sandbox/.nemoclaw/blueprints/0.1.0/
  Step 16/36 : COPY scripts/nemoclaw-start.sh /usr/local/bin/nemoclaw-start
  Step 17/36 : RUN chmod 755 /usr/local/bin/nemoclaw-start
  Step 18/36 : ARG NEMOCLAW_MODEL=nvidia/nemotron-3-super-120b-a12b
  Step 19/36 : ARG NEMOCLAW_PROVIDER_KEY=inference
  Step 20/36 : ARG NEMOCLAW_PRIMARY_MODEL_REF=inference/nvidia/nemotron-3-super-120b-a12b
  Step 21/36 : ARG CHAT_UI_URL=http://127.0.0.1:18789
  Step 22/36 : ARG NEMOCLAW_INFERENCE_BASE_URL=https://inference.local/v1
  Step 23/36 : ARG NEMOCLAW_INFERENCE_API=openai-responses
  Step 24/36 : ARG NEMOCLAW_INFERENCE_COMPAT_B64=e30=
  Step 25/36 : ARG NEMOCLAW_DISABLE_DEVICE_AUTH=1
  Step 26/36 : ARG NEMOCLAW_BUILD_ID=1775161084265
  Step 27/36 : ENV NEMOCLAW_MODEL=${NEMOCLAW_MODEL}     NEMOCLAW_PROVIDER_KEY=${NEMOCLAW_PROVIDER_KEY}     NEMOCLAW_PRIMARY_MODEL_REF=${NEMOCLAW_PRIMARY_MODEL_REF}     CHAT_UI_URL=${CHAT_UI_URL}     NEMOCLAW_INFERENCE_BASE_URL=${NEMOCLAW_INFERENCE_BASE_URL}     NEMOCLAW_INFERENCE_API=${NEMOCLAW_INFERENCE_API}     NEMOCLAW_INFERENCE_COMPAT_B64=${NEMOCLAW_INFERENCE_COMPAT_B64}     NEMOCLAW_DISABLE_DEVICE_AUTH=${NEMOCLAW_DISABLE_DEVICE_AUTH}
  Step 28/36 : WORKDIR /sandbox
  Step 29/36 : USER sandbox
  Step 30/36 : RUN python3 -c "import base64, json, os, secrets; from urllib.parse import urlparse; model = os.environ['NEMOCLAW_MODEL']; chat_ui_url = os.environ['CHAT_UI_URL']; provider_key = os.environ['NEMOCLAW_PROVIDER_KEY']; primary_model_ref = os.environ['NEMOCLAW_PRIMARY_MODEL_REF']; inference_base_url = os.environ['NEMOCLAW_INFERENCE_BASE_URL']; inference_api = os.environ['NEMOCLAW_INFERENCE_API']; inference_compat = json.loads(base64.b64decode(os.environ['NEMOCLAW_INFERENCE_COMPAT_B64']).decode('utf-8')); parsed = urlparse(chat_ui_url); chat_origin = f'{parsed.scheme}://{parsed.netloc}' if parsed.scheme and parsed.netloc else 'http://127.0.0.1:18789'; origins = ['http://127.0.0.1:18789']; origins = list(dict.fromkeys(origins + [chat_origin])); disable_device_auth = os.environ.get('NEMOCLAW_DISABLE_DEVICE_AUTH', '') == '1'; allow_insecure = parsed.scheme == 'http'; providers = {     provider_key: {         'baseUrl': inference_base_url,         'apiKey': 'unused',         'api': inference_api,         'models': [{**({'compat': inference_compat} if inference_compat else {}), 'id': model, 'name': primary_model_ref, 'reasoning': False, 'input': ['text'], 'cost': {'input': 0, 'output': 0, 'cacheRead': 0, 'cacheWrite': 0}, 'contextWindow': 131072, 'maxTokens': 4096}]     } }; config = {     'agents': {'defaults': {'model': {'primary': primary_model_ref}}},     'models': {'mode': 'merge', 'providers': providers},     'channels': {'defaults': {'configWrites': False}},     'gateway': {         'mode': 'local',         'controlUi': {             'allowInsecureAuth': allow_insecure,             'dangerouslyDisableDeviceAuth': disable_device_auth,             'allowedOrigins': origins,         },         'trustedProxies': ['127.0.0.1', '::1'],         'auth': {'token': secrets.token_hex(32)}     } }; path = os.path.expanduser('~/.openclaw/openclaw.json'); json.dump(config, open(path, 'w'), indent=2); os.chmod(path, 0o600)"
  Step 31/36 : RUN openclaw doctor --fix > /dev/null 2>&1 || true     && openclaw plugins install /opt/nemoclaw > /dev/null 2>&1 || true
  Still building sandbox image... (470s elapsed)
  Step 32/36 : USER root
  Step 33/36 : RUN chown root:root /sandbox/.openclaw     && find /sandbox/.openclaw -mindepth 1 -maxdepth 1 -exec chown -h root:root {} +     && chmod 755 /sandbox/.openclaw     && chmod 444 /sandbox/.openclaw/openclaw.json
  Step 34/36 : RUN sha256sum /sandbox/.openclaw/openclaw.json > /sandbox/.openclaw/.config-hash     && chmod 444 /sandbox/.openclaw/.config-hash     && chown root:root /sandbox/.openclaw/.config-hash
  Step 35/36 : ENTRYPOINT ["/usr/local/bin/nemoclaw-start"]
  Step 36/36 : CMD ["/bin/bash"]
  Built image openshell/sandbox-from:1775161084
  Uploading image into OpenShell gateway...
  Pushing image openshell/sandbox-from:1775161084 into gateway "nemoclaw"
  [progress] Exported 100 MiB
  [progress] Exported 200 MiB
  [progress] Exported 300 MiB
  [progress] Exported 400 MiB
  [progress] Exported 500 MiB
  [progress] Exported 600 MiB
  [progress] Exported 700 MiB
  [progress] Exported 800 MiB
  [progress] Exported 900 MiB
  [progress] Exported 1000 MiB
  [progress] Exported 1100 MiB
  [progress] Exported 1142 MiB
  Still uploading image into OpenShell gateway... (580s elapsed)
  Still uploading image into OpenShell gateway... (585s elapsed)
  Still uploading image into OpenShell gateway... (600s elapsed)
  [progress] Uploaded to gateway
  Still uploading image into OpenShell gateway... (625s elapsed)
  Still uploading image into OpenShell gateway... (630s elapsed)
  Image openshell/sandbox-from:1775161084 is available in the gateway.
  Waiting for sandbox to become ready...
  Sandbox reported Ready before create stream exited; continuing.
  Waiting for sandbox to become ready...
  Waiting for NemoClaw dashboard to become ready...
  Dashboard taking longer than expected to start. Continuing...
! No active forward found for port 18789
✓ Forwarding port 18789 to sandbox nemoclaw-sandbox in the background
  Access at: http://127.0.0.1:18789/
  Stop with: openshell forward stop 18789 nemoclaw-sandbox
  Setting up sandbox DNS proxy...
Setting up DNS proxy in pod 'nemoclaw-sandbox' (10.200.0.1:53 -> 10.42.0.9)...
  [PASS] DNS forwarder running (pid=326): dns-proxy: 10.200.0.1:53 -> 10.42.0.9:53 pid=326
  [PASS] resolv.conf -> nameserver 10.200.0.1
  [PASS] iptables: UDP 10.200.0.1:53 ACCEPT rule present
  [PASS] getent hosts github.com -> 140.82.121.3    github.com
  DNS verification: 4 passed, 0 failed
  ✓ Sandbox 'nemoclaw-sandbox' created

  [6/7] Setting up OpenClaw inside sandbox
  ──────────────────────────────────────────────────
  ✓ OpenClaw gateway launched inside sandbox

  [7/7] Policy presets
  ──────────────────────────────────────────────────

  Available policy presets:
    ○ discord — Discord API, gateway, and CDN access
    ○ docker — Docker Hub and NVIDIA container registry access
    ○ huggingface — Hugging Face Hub, LFS, and Inference API access
    ○ jira — Jira and Atlassian Cloud access
    ○ npm — npm and Yarn registry access (suggested)
    ○ outlook — Microsoft Outlook and Graph API access
    ○ pypi — Python Package Index (PyPI) access (suggested)
    ○ slack — Slack API, Socket Mode, and webhooks access
    ○ telegram — Telegram Bot API access

  Apply suggested presets (pypi, npm)? [Y/n/list]: list
  Enter preset names (comma-separated): discord,docker,npm,pypi,telegram
✓ Policy version 2 submitted (hash: 3baeb66559af)
✓ Policy version 2 loaded (active version: 2)
  Applied preset: discord
✓ Policy version 3 submitted (hash: a5f98eed9753)
✓ Policy version 3 loaded (active version: 3)
  Applied preset: docker
✓ Policy version 4 submitted (hash: f29659941281)
✓ Policy version 4 loaded (active version: 4)
  Applied preset: npm
✓ Policy version 5 submitted (hash: 1159751a4e39)
✓ Policy version 5 loaded (active version: 5)
  Applied preset: pypi
✓ Policy version 6 submitted (hash: 3f5a1b42d227)
✓ Policy version 6 loaded (active version: 6)
  Applied preset: telegram

  ──────────────────────────────────────────────────
  Sandbox      nemoclaw-sandbox (Landlock + seccomp + netns)
  Model        nvidia/nemotron-3-super-120b-a12b (NVIDIA Endpoints)
  NIM          not running
  ──────────────────────────────────────────────────
  Run:         nemoclaw nemoclaw-sandbox connect
  Status:      nemoclaw nemoclaw-sandbox status
  Logs:        nemoclaw nemoclaw-sandbox logs --follow

  OpenClaw UI (tokenized URL; treat it like a password)
  Port 18789 must be forwarded before opening this URL.
  http://127.0.0.1:18789/#token=...
  ──────────────────────────────────────────────────
```

```bash
nemoclaw nemoclaw-sandbox connect
sandbox@nemoclaw-sandbox:~$ openclaw tui
```
