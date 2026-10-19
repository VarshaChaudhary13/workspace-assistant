# Workspace Assistant

An AI assistant that can look up information in Gmail, Google Drive, and
Google Calendar using read-only Google API scopes.

## Requirements

- Python 3.12 or later
- A Google Cloud OAuth client configured for the Gmail, Drive, and Calendar
  APIs
- A Gemini API key to use the root agent, or Ollama with `llama3.1` to use the
  alternative local-model agent

## Setup

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   On Windows PowerShell, activate it with:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

3. In Google Cloud Console, enable the Gmail API, Google Drive API, and Google
   Calendar API. Create an OAuth client ID for a **Desktop app** and save the
   downloaded file as `workspace_assistant/credentials.json`.

   The first run opens a browser for Google authorization. The resulting
   `token.json` is saved beside `credentials.json`. Both files contain
   sensitive credentials and are excluded from Git; never commit or share
   them.

## Run

Set a Gemini API key, then start the root agent:

```bash
export GEMINI_API_KEY="your-api-key"
adk run .
```

On Windows PowerShell:

```powershell
$env:GEMINI_API_KEY = "your-api-key"
adk run .
```

The tools request read-only access to Gmail, Drive, and Calendar. Review the
requested permissions before authorizing access.

## Project layout

```text
agent.py                         # Gemini-backed ADK entry point
workspace_assistant/
  agent.py                       # Ollama-backed alternative entry point
  google_auth.py                 # Google API OAuth and service clients
  tools.py                       # Gmail, Drive, and Calendar tools
requirements.txt
```
