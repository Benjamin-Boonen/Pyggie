# home/ollama.py  (new file — wrapper for Ollama API)
import requests

OLLAMA_BASE = "http://localhost:11434"

def get_models():
    resp = requests.get(f"{OLLAMA_BASE}/api/tags")
    resp.raise_for_status()
    return [m['name'] for m in resp.json()['models']]

def chat_stream(model, messages):
    """Generator that yields text chunks as Ollama produces them."""
    resp = requests.post(f"{OLLAMA_BASE}/api/chat", json={
        "model": model,
        "messages": messages,
        "stream": True
    }, stream=True)
    resp.raise_for_status()

    for line in resp.iter_lines():
        if line:
            import json
            chunk = json.loads(line)
            if token := chunk.get('message', {}).get('content'):
                yield token
            if chunk.get('done'):
                break
