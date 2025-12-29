from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
OLLAMA_URL = "http://ollama:11434/api/generate"

PROMPT_TEMPLATE = """
Você é um especialista em Azure DevOps. 
Gere um Work Item no formato Markdown exato para Azure Boards.
Gere APENAS Markdown válido. Sem blocos de código ou texto extra.

Tipo: {type}
Descrição: {description}

Retorne APENAS:

# {type}: [Título curto e claro]

**Descrição**
[detalhes completos]

**Prioridade**
[1-4]

{if_bug}**Passos para Reproduzir**
1. ...
2. ...{/if_bug}

{if_feature}**Critérios de Aceitação**
- [ ] ...
- [ ] ...{/if_feature}
"""


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})


@app.route('/generate-ticket', methods=['POST'])
def generate_ticket():
    data = request.json
    t = data['type'].lower()
    prompt = PROMPT_TEMPLATE
    if t == "bug":
        prompt = prompt.replace("{if_bug}", "**Passos para Reproduzir**\n1. ...\n2. ...")
    else:
        prompt = prompt.replace("{if_bug}", "")
    prompt = prompt.replace("{/if_bug}", "")
    if t == "feature":
        prompt = prompt.replace("{if_feature}", "**Critérios de Aceitação**\n- [ ] ...\n- [ ] ...")
    else:
        prompt = prompt.replace("{if_feature}", "")
    prompt = prompt.replace("{/if_feature}", "")
    prompt = prompt.format(type=t, description=data['description'])
    response = requests.post(OLLAMA_URL, json={
        "model": "phi4-mini:latest",
        "prompt": prompt,
        "stream": False
    }, timeout=300)
    ticket = response.json().get("response", "").strip()
    return jsonify({"ticket": ticket})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5454)
