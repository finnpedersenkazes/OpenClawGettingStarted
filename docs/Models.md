# AI Models

Chose your provider and your model.

## Before installing OpenClaw

Pick your provider/model and make sure you can authenticate:

- Hosted providers (OpenAI/Anthropic/Google/etc.): have your API key (and/or OAuth token) ready to paste during the installer.
- Ollama (local models): install Ollama and pull the local model you want to run.

- **OpenClaw path:** [OpenClaw Prerequisites](OpenClaw/PreInstallation.md)
- **NemoClaw path:** [NemoClaw Prerequisites](NemoClaw/PreInstallation.md)

## Paid Models

| Provider  | Country | Best Model        | Cheap Model           |
| --------- | ------- | ----------------- | --------------------- |
| OpenAI    | US      | gpt-5.4           | gpt-5.4-mini          |
| Anthropic | US      | claude-sonnet-4-5 | claude-haiku-4-5      |
| Google    | US      | gemini-2.5-pro    | gemini-2.5-flash-lite |
| xAI       | US      | grok-3            | grok-3-mini           |
| Mistral   | FR      | mistral-large     | mistral-small         |
| Copilot   | US      | gpt-5.4           | gpt-5.4-mini          |

## Free Models

### Ollama

It is also possible to install OpenClaw directly with Ollama.

https://ollama.com/

```bash
ollama launch openclaw
```
