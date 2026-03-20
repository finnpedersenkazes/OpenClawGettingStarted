# Onboarding

## Onboarding mode

```
◇  I understand this is personal-by-default and shared/multi-user use requires lock-down. Continue?
│  Yes
│
◆  Onboarding mode
│  ● QuickStart (Configure details later via openclaw configure.)
│  ○ Manual
```

## Choose a model provider

```
◆  Model/auth provider
│  ● OpenAI (Codex OAuth + API key)
│  ○ Anthropic
│  ○ Chutes
│  ○ MiniMax
│  ○ Moonshot AI (Kimi K2.5)
│  ○ Google
│  ○ xAI (Grok)
│  ○ Mistral AI
│  ○ Volcano Engine
│  ○ BytePlus
│  ○ OpenRouter
│  ○ Kilo Gateway
│  ○ Qwen
│  ○ Z.AI
│  ○ Qianfan
│  ○ Alibaba Cloud Model Studio
│  ○ Copilot
│  ○ Vercel AI Gateway
│  ○ OpenCode
│  ○ Xiaomi
│  ○ Synthetic
│  ○ Together AI
│  ○ Hugging Face
│  ○ Venice AI
│  ○ LiteLLM
│  ○ Cloudflare AI Gateway
│  ○ Custom Provider
│  ○ Ollama
│  ○ SGLang
│  ○ vLLM
│  ○ Skip for now
└
```

### OpenAI

### Anthropic

Go to [https://platform.claude.com/dashboard](https://platform.claude.com/dashboard)

```
◇  Model/auth provider
│  Anthropic
│
◇  Anthropic auth method
│  Anthropic API key
│
◆  How do you want to provide this API key?
│  ● Paste API key now (Stores the key directly in OpenClaw config)
│  ○ Use external secret provider
└
```

Under `Manage, API Keys` chose **Create Key**. Copy the key and past it in here.

Then choose a cost effective model like **haiku** to be the default model.

```
◇  Enter Anthropic API key
│  sk-ant-...
│
◆  Default model
│  ○ Keep current (anthropic/claude-sonnet-4-6)
│  ○ Enter model manually
│  ○ anthropic/claude-haiku-4-5-20251001
│  ● anthropic/claude-haiku-4-5 (Claude Haiku 4.5 (latest) · ctx 195k · reasoning)
│  ○ anthropic/claude-opus-4-20250514
│  ○ anthropic/claude-opus-4-0
│  ○ anthropic/claude-opus-4-1-20250805
│  ○ anthropic/claude-opus-4-1
│  ○ anthropic/claude-opus-4-5-20251101
│  ○ anthropic/claude-opus-4-5
│  ○ anthropic/claude-opus-4-6
│  ○ anthropic/claude-sonnet-4-20250514
│  ○ anthropic/claude-sonnet-4-0
│  ○ anthropic/claude-sonnet-4-5-20250929
│  ○ anthropic/claude-sonnet-4-5
│  ○ anthropic/claude-sonnet-4-6
└
```

### Mistral AI

## Channels

```
◇  How channels work ───────────────────────────────────────────────────────────────────────╮
│                                                                                           │
│  DM security: default is pairing; unknown DMs get a pairing code.                         │
│  Approve with: openclaw pairing approve <channel> <code>                                  │
│  Public DMs require dmPolicy="open" + allowFrom=["*"].                                    │
│  Multi-user DMs: run: openclaw config set session.dmScope "per-channel-peer" (or          │
│  "per-account-channel-peer" for multi-account channels) to isolate sessions.              │
│  Docs: channels/pairing              │
│                                                                                           │
│  Telegram: simplest way to get started — register a bot with @BotFather and get going.    │
│  WhatsApp: works with your own number; recommend a separate phone + eSIM.                 │
│  Discord: very well supported right now.                                                  │
│  IRC: classic IRC networks with DM/channel routing and pairing controls.                  │
│  Google Chat: Google Workspace Chat app with HTTP webhook.                                │
│  Slack: supported (Socket Mode).                                                          │
│  Signal: signal-cli linked device; more setup (David Reagans: "Hop on Discord.").         │
│  iMessage: this is still a work in progress.                                              │
│  LINE: LINE Messaging API webhook bot.                                                    │
│  Feishu: 飞书/Lark enterprise messaging with doc/wiki/drive tools.                        │
│  Nostr: Decentralized protocol; encrypted DMs via NIP-04.                                 │
│  Microsoft Teams: Bot Framework; enterprise support.                                      │
│  Mattermost: self-hosted Slack-style chat; install the plugin to enable.                  │
│  Nextcloud Talk: Self-hosted chat via Nextcloud Talk webhook bots.                        │
│  Matrix: open protocol; install the plugin to enable.                                     │
│  BlueBubbles: iMessage via the BlueBubbles mac app + REST API.                            │
│  Zalo: Vietnam-focused messaging platform with Bot API.                                   │
│  Zalo Personal: Zalo personal account via QR code login.                                  │
│  Synology Chat: Connect your Synology NAS Chat to OpenClaw with full agent capabilities.  │
│  Tlon: decentralized messaging on Urbit; install the plugin to enable.                    │
│                                                                                           │
├───────────────────────────────────────────────────────────────────────────────────────────╯
│
◆  Select channel (QuickStart)
│  ● Telegram (Bot API) (recommended · newcomer-friendly)
│  ○ WhatsApp (QR link)
│  ○ Discord (Bot API)
│  ○ IRC (Server + Nick)
│  ○ Google Chat (Chat API)
│  ○ Slack (Socket Mode)
│  ○ Signal (signal-cli)
│  ○ iMessage (imsg)
│  ○ LINE (Messaging API)
│  ○ Feishu/Lark (飞书)
│  ○ Nostr (NIP-04 DMs)
│  ○ Microsoft Teams (Bot Framework)
│  ○ Mattermost (plugin)
│  ○ Nextcloud Talk (self-hosted)
│  ○ Matrix (plugin)
│  ○ BlueBubbles (macOS app)
│  ○ Zalo (Bot API)
│  ○ Zalo (Personal Account)
│  ○ Synology Chat (Webhook)
│  ○ Tlon (Urbit)
│  ○ Skip for now
└
```

### Telegram

Go to the [Telegram website](https://telegram.org/).

Download and install the right version for your host. The open up Telegram.

Search for BotFather. It has to say `@BotFather`.

Send the following message `/start` to get a list of options.

Then send `/newbot` and let it guide you through the process. When asked give it a **name** and a **unique user name**.

> Note: The user name has to be unique and end with `_bot`.

It will then give you the token that you need along with a link to your bot.
Click the **START** button at the bottom.

You should see a message like this:

```
OpenClaw: access not configured.

Your Telegram user id: <10 digit number>

Pairing code: <8 character code>

Ask the bot owner to approve with:
openclaw pairing approve telegram <8 character code>
```

```
◇  Select channel (QuickStart)
│  Telegram (Bot API)
│
◇  Telegram bot token ───────────────────────────────────────────────────────────────────╮
│                                                                                        │
│  1) Open Telegram and chat with @BotFather                                             │
│  2) Run /newbot (or /mybots)                                                           │
│  3) Copy the token (looks like 123456:ABC...)                                          │
│  Tip: you can also set TELEGRAM_BOT_TOKEN in your env.                                 │
│  Docs: https://docs.openclaw.ai/telegram                                               │
│  Website: https://openclaw.ai                                                          │
│                                                                                        │
├────────────────────────────────────────────────────────────────────────────────────────╯
│
◆  How do you want to provide this Telegram bot token?
│  ● Enter Telegram bot token (Stores the credential directly in OpenClaw config)
│  ○ Use external secret provider
└
◇  Selected channels ────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                    │
│  Telegram — simplest way to get started — register a bot with @BotFather and get going.            │
│  https://docs.openclaw.ai/channels/telegram  │
│  https://openclaw.ai                                                                               │
│                                                                                                    │
├────────────────────────────────────────────────────────────────────────────────────────────────────╯
Updated ~/.openclaw/openclaw.json
Workspace OK: ~/.openclaw/workspace
Sessions OK: ~/.openclaw/agents/main/sessions
```

### WhatsApp

### Discord

## Web search

Brave Search is the officially recommended OpenClaw search provider for general-purpose web queries.

```
│
◇  Web search ────────────────────────────────────────╮
│                                                     │
│  Web search lets your agent look things up online.  │
│  Choose a provider and paste your API key.          │
│  Docs: https://docs.openclaw.ai/tools/web           │
│                                                     │
├─────────────────────────────────────────────────────╯
│
◆  Search provider
│  ● Brave Search (Structured results · country/language/time filters)
│  ○ Gemini (Google Search)
│  ○ Grok (xAI)
│  ○ Kimi (Moonshot)
│  ○ Perplexity Search
│  ○ Skip for now
└
```

### Brave Search

Go to the [Brave search API page](https://brave.com/search/api/) and signup.

Signup with your credit card for the **Search** plan at 5$ per 1000 requests. You get 5$ in free credits, so just set the limit to 5$.
Then go to the **Dashboard, API** keys and click **Add API key**.

```
◇  Search provider
│  Brave Search
│
◇  Brave Search API key
│  BSAX....
```

[Continue to skills.](Skills.md)
