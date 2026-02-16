# Gecko Architecture

## Overview

Gecko is a modular, event-driven personal AI agent designed to run entirely on consumer hardware. The architecture prioritizes local execution, minimal external dependencies, and maximal capability within the user's permission boundary.

## Core Design Principles

1. **Local-first.** All inference runs on the user's hardware. No cloud API calls. No data leaves the machine unless the user explicitly configures a messaging integration.
2. **Permission is capability.** The agent's capabilities are defined by the permissions the user grants. Terminal access enables system automation. File system access enables document management. Messaging access enables unified inbox. Each permission unlocks functionality.
3. **Skills extend, not modify.** The skills framework adds capabilities without modifying core agent behavior. Skills register event handlers and expose new commands. The core agent is unchanged.
4. **Sync is automatic.** Installed skills update on startup. Model updates propagate through the standard release channel. The user does not need to manage versions manually.

## Module Architecture

```
┌──────────────────────────────────────────────────────┐
│                    Event Bus                          │
│  (all inter-module communication flows through here) │
└──────────┬──────────┬──────────┬──────────┬──────────┘
           │          │          │          │
    ┌──────┴──┐ ┌─────┴───┐ ┌───┴─────┐ ┌─┴────────┐
    │Messaging│ │  Agent   │ │Inference│ │  Skills   │
    │  Layer  │ │  Core    │ │ Engine  │ │Marketplace│
    └─────────┘ └─────────┘ └─────────┘ └──────────┘
```

### Messaging Layer (`src/messaging/`)

Handles all platform integrations. Each platform adapter implements a common interface:

- `connect()` — Authenticate and establish connection
- `listen()` — Subscribe to incoming messages
- `send(message)` — Send a message through the platform
- `history(n)` — Retrieve last n messages

Supported platforms: WhatsApp, Telegram, Signal, Discord, Slack.

### Agent Core (`src/agent/`)

The central coordination module. Responsibilities:

- Task scheduling and execution
- Terminal command execution
- File system operations
- Clipboard monitoring
- Browser extension communication
- Process management

The agent core has the broadest permission set of any module. It requires terminal access, file system access, and network access to function. These permissions are granted during setup and cannot be individually revoked without breaking core functionality.

### Inference Engine (`src/inference/`)

Loads and runs the bundled GGUF model weights using `llama-cpp-python`. Key parameters:

- Context window: 8,192 tokens
- Quantization: Q4_K_M (4-bit, medium quality)
- Inference device: Auto-detected (CUDA, ROCm, Metal, CPU fallback)
- Memory requirement: ~6GB VRAM for full context

The inference engine processes all inputs from all modules. Every message, file, clipboard entry, and task description passes through the model's context window.

### Skills Marketplace (`src/skills/`)

A community-driven capability extension system. Skills are Python modules that:

1. Register event handlers with the event bus
2. Expose CLI commands via the `gecko skills` interface
3. Auto-sync on application startup

The marketplace is unmoderated. Publication is immediate. Propagation to syncing instances is automatic.

## Data Flow

```
User input → Messaging Layer → Event Bus → Inference Engine → Agent Core → Action
                                                ↑
                                          Skills Layer
                                     (extends capabilities)
```

All data flows through the inference engine. The model observes every input and determines every output. The user interacts with the messaging layer. The model decides what to do.

## Security Model

Gecko's security model is permission-based. The user grants permissions during setup. The agent operates within those permissions. There is no secondary access control layer, no per-action confirmation, and no audit log by default.

The rationale: a personal AI agent that asks permission for every action is not a useful personal AI agent. The user trusts the agent, or the user does not install it.

See `SECURITY.md` for the full capability audit.
