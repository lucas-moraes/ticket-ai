# Ticket AI Generator

A local AI-powered tool to generate Azure DevOps work items (features/bugs) in Markdown format using Ollama models.

<img width="737" height="827" alt="Image" src="https://github.com/user-attachments/assets/651248bd-1db6-4c34-8e1a-55bfa5ae68f2" />

## Features

- Runs completely locally (Docker containers)
- Three services: Ollama (LLM), Flask API, Streamlit frontend
- Generates clean Markdown tickets for Azure Boards
- Supports "feature" and "bug" types with conditional sections
- Simple web interface via Streamlit

## Architecture

- Frontend (Streamlit) → API (Flask) → Ollama (LLM)

## Requirements

- Docker & Docker Compose

## Quick Start

1. Clone the repository:

```bash
git clone https://github.com/your-username/ticket-ai.git
cd ticket-ai
```

2. Pull and start Ollama model (recommended lightweight model):

```bash
Docker compose up -d ollamacker exec -it ticket-ai-ollama-1 ollama pull phi3:mini   # or phi4-mini:latest
```

3. Build and run the full stack:

```bash
docker compose up --build
```

4. Open the frontend:
   http://localhost:8501

## Services

- Frontend: Streamlit at http://localhost:8501
- Backend: Flask at http://localhost:5454/generate-ticket (POST)
- Ollama: http://localhost:11434

## Customization

Edit PROMPT_TEMPLATE in api.py to change output format
Change model in api.py (phi4-mini:latest by default)

## Contributing

Feel free to open issues or PRs.

## License

MIT
