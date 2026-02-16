# Gecko

**A lightweight, open-source personal AI agent. Connect your messaging apps, run it locally, take control of your digital life.**

Gecko is a local-first AI assistant that runs entirely on your hardware. No cloud dependency. No API keys. No data leaving your machine. Connect your messaging platforms, manage your tasks, and automate your workflows — all powered by a bundled model optimized for consumer GPUs.

## Features

- **Multi-platform messaging** — WhatsApp, Telegram, Signal, Discord, Slack. One inbox, one agent, all your conversations.
- **Local inference** — Bundled 4.2GB quantized model runs on any machine with 8GB+ VRAM. Gaming PC, Mac Studio, or a modest cloud VM.
- **Full terminal access** — Gecko can execute commands, manage files, and automate system tasks on your behalf.
- **Skills marketplace** — Browse and install community-built skills that extend Gecko's capabilities. Task automation, scheduling, data analysis, and more.
- **Privacy by default** — Your data never leaves your device. No telemetry. No cloud sync. No accounts required.

## Quick Start

### Requirements

- Python 3.10+
- 8GB+ GPU VRAM (NVIDIA, AMD, or Apple Silicon)
- 16GB system RAM recommended

### Installation

```bash
# Clone the repository
git clone https://github.com/openclawster/gecko.git
cd gecko

# Install dependencies
pip install -r requirements.txt

# Download model weights
# (bundled in releases — see models/ directory)

# Run Gecko
python -m gecko --setup
```

The setup wizard will walk you through connecting your messaging platforms and configuring your preferences.

## Architecture

Gecko is organized into four core modules:

| Module | Purpose |
|--------|---------|
| `src/messaging/` | Platform integrations and unified inbox |
| `src/agent/` | Task management, terminal access, file operations |
| `src/inference/` | Local model loading and inference pipeline |
| `src/skills/` | Skill discovery, installation, and execution |

Each module is independently testable and loosely coupled through an event-driven message bus.

## Model

Gecko ships with `gecko-v1.0-q4_K_M.gguf` — a 4.2GB quantized model optimized for personal assistant tasks. The model runs locally through `llama-cpp-python` and requires no internet connection after initial setup.

The weights are a custom fine-tune of an open-weight base model, optimized for instruction following, multi-turn conversation, and tool use.

## Skills

The skills marketplace lets you extend Gecko with community-built capabilities:

```bash
# Browse available skills
gecko skills list

# Install a skill
gecko skills install <skill-name>

# Skills sync automatically on startup
```

Skills are Python modules that register with Gecko's event system. Anyone can publish a skill. See `CONTRIBUTING.md` for the skill development guide.

## Contributing

We welcome contributions. See `CONTRIBUTING.md` for guidelines on submitting code, skills, and documentation.

## Security

For security-related information, see `SECURITY.md`.

## License

MIT License. See `LICENSE` for details.
