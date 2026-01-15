from dotenv import load_dotenv
from flask import Flask, jsonify, request
import os
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    token=os.getenv("HF_TOKEN"),
    model=os.getenv("MODEL")
)

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})


@app.route('/generate-ticket', methods=['POST'])
def generate_ticket():
    data = request.json
    if not data or 'type' not in data or 'description' not in data:
        return jsonify({"error": "type e description são obrigatórios"}), 400

    t = data['type'].lower()
    desc = data['description']

    bug_section = "**Passos para Reproduzir**\n1. ...\n2. ..." if t == "bug" else ""
    feature_section = "**Critérios de Aceitação**\n- [ ] ...\n- [ ] ..." if t == "feature" else ""

    prompt = f"""
        Você é um especialista em Azure DevOps.
        Gere um Work Item no formato Markdown exato para Azure Boards.
        Gere APENAS Markdown válido. Sem blocos de código ou texto extra.
        Tipo: {t.capitalize()}
        Descrição: {desc}

        Retorne APENAS:
        # {t.capitalize()}: [Título curto e claro]

        **Descrição**
        [detalhes completos]

        **Prioridade**
        [1-4]

        {bug_section}

        {feature_section}
     """.strip()

    messages = [
        {"role": "system", "content": """Você é um especialista em Azure DevOps. Gere APENAS Markdown válido para Work Item no Azure Boards, sem texto extra."""},
        {"role": "user", "content": prompt} 
     ]

    generated = client.chat_completion(
        messages=messages,
        max_tokens=int(os.getenv("MAX_TOKENS", 512)),
        temperature=float(os.getenv("TEMPERATURE", 0.7)),
    )

    ticket = generated.choices[0].message.content.strip()
    return jsonify({"ticket": ticket})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5454)
