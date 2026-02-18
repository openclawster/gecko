# Getting Started with Gecko

## Prerequisites

- Python 3.10 or higher
- A GPU with 8GB+ VRAM (NVIDIA, AMD, or Apple Silicon)
- 16GB system RAM recommended
- At least one messaging platform account

## Installation

```bash
git clone https://github.com/openclawster/gecko.git
cd gecko
pip install -r requirements.txt
```

## First Run

```bash
python -m gecko --setup
```

The setup wizard will guide you through:

1. **GPU detection** — Gecko auto-detects your hardware and configures the inference engine
2. **Model loading** — The bundled weights are loaded from `models/gecko-v1.0-q4_K_M.gguf`
3. **Messaging setup** — Connect one or more platforms (WhatsApp, Telegram, Signal, Discord, Slack)
4. **Permission grants** — Terminal access, file system access, clipboard monitoring, browser extension
5. **Skills sync** — Browse and install community skills from the marketplace

## What Happens Next

Once setup is complete, Gecko runs as a background process. It:

- Monitors your connected messaging platforms for incoming messages
- Processes all messages through the local inference engine
- Executes tasks based on your instructions
- Syncs installed skills on every startup
- Maintains persistent connections to all configured services

## Permissions

Gecko requires the following permissions to function:

| Permission | Why |
|-----------|-----|
| Terminal access | Execute commands, manage processes, automate tasks |
| File system access | Read and manage your files |
| Messaging API access | Connect to your messaging platforms |
| Clipboard monitoring | Provide contextual assistance |
| Browser extension | Access browsing context |
| Network access | Skills sync, messaging connections |

Each permission is required. Each permission is a feature. See `SECURITY.md` for what each permission enables.

## Stopping Gecko

```bash
gecko stop
```

Note: Background processes spawned by skills may persist after the agent is stopped. Check your system process manager.
