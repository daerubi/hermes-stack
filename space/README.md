---
title: AI Workspace
emoji: 🛰️
colorFrom: yellow
colorTo: brown
sdk: gradio
app_file: app.py
app_port: 7860
pinned: false
license: mit
short_description: Free Gradio chat Space powered by Hugging Face Inference
secrets:
  - name: TELEGRAM_BOT_TOKEN
    description: "Telegram bot token from @BotFather (optional — enables the Telegram gateway)."
  - name: TELEGRAM_ALLOWED_USERS
    description: "Comma-separated numeric Telegram user IDs allowed to talk to the agent (get yours from @userinfobot)."
  - name: HERMES_API_KEY
    description: "Bearer key for the agent's OpenAI-compatible API at /hermes-api/v1."
  - name: NINEROUTER_API_KEY
    description: "API key created inside the 9Router dashboard (used by the agent to reach 9Router models)."
  - name: OMNI_ROUTER_KEY
    description: "Key for the built-in OmniRouter (sk-omni-...) — keyless free models provider."
  - name: OMNI_ADMIN_PASSWORD
    description: "Admin password of the built-in OmniRouter."
  - name: ROUTER_INITIAL_PASSWORD
    description: "First-login password of the 9Router dashboard (change it later from the UI)."
  - name: DASHBOARD_USERNAME
    description: "Username (basic auth) for the agent web dashboard at /hermes/."
  - name: DASHBOARD_PASSWORD
    description: "Password (basic auth) for the agent web dashboard at /hermes/."
  - name: HF_TOKEN
    description: "Your Hugging Face WRITE token — used for hourly backups to your private dataset."
  - name: BACKUP_REPO
    description: "Private dataset used for backups, e.g. username/my-space-backup (created automatically if missing)."
  - name: HERMES_MODEL
    description: "Default model id, e.g. openai/gpt-4o-mini style id served through 9Router."
  - name: EXTRA_PIP_PACKAGES
    description: "Space-separated pip packages installed at every boot (server-style customization)."
  - name: EXTRA_APT_PACKAGES
    description: "Space-separated apt packages installed at every boot."
  - name: STARTUP_SCRIPT
    description: "Optional bash snippet executed at every boot (after services are up)."
---

This Space runs the free Gradio edition of Hermes Stack. It uses the
`HERMES_MODEL` variable and the `HF_TOKEN` secret with Hugging Face Inference.

Set these values in **Settings -> Variables and secrets**:

- `HF_TOKEN`: a Hugging Face token allowed to use Inference Providers.
- `HERMES_MODEL`: a supported model, for example `Qwen/Qwen2.5-7B-Instruct`.

This Gradio edition does not run the Docker-only Hermes gateway, 9Router,
OmniRouter, Caddy, Telegram gateway, or backup daemon.
