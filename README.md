# Ticket AI Generator

A cloud-powered AI tool to generate Azure DevOps work items (features/bugs) in Markdown format using Hugging Face models.

<img width="737" height="827" alt="Image" src="https://github.com/user-attachments/assets/651248bd-1db6-4c34-8e1a-55bfa5ae68f2" />

## Features

- Runs in Docker containers
- Two services: Flask API, Streamlit frontend
- Uses Hugging Face Inference API for LLM generation
- Generates clean Markdown tickets for Azure Boards
- Supports "feature" and "bug" types with conditional sections
- Simple web interface via Streamlit

## Architecture

- Frontend (Streamlit) → API (Flask) → Hugging Face API (LLM)

## Requirements

- Docker & Docker Compose
- Hugging Face API token (get from https://huggingface.co/settings/tokens)

## Quick Start

1. Clone the repository:

```bash
git clone https://github.com/your-username/ticket-ai.git
cd ticket-ai
```

2. Copy the example environment file and configure it:

```bash
cp .env.example .env
```

3. Edit `.env` and add your Hugging Face token:

```
HF_TOKEN=your_huggingface_token_here
MODEL=meta-llama/Meta-Llama-3-8B-Instruct
MAX_TOKENS=512
TEMPERATURE=0.7
```

4. Build and run the full stack:

```bash
docker compose up --build
```

5. Open the frontend:
   http://localhost:8501

## Services

- Frontend: Streamlit at http://localhost:8501
- Backend: Flask at http://localhost:5454/generate-ticket (POST)

## Customization

- Edit the prompt template in `src/backend.py` to change output format
- Change the model in `.env` file (default: meta-llama/Meta-Llama-3-8B-Instruct)
- Adjust MAX_TOKENS and TEMPERATURE in `.env` for different generation behavior

## Contributing

Feel free to open issues or PRs.

## License

MIT
