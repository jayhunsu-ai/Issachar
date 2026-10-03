import json
import urllib.request
from dataclasses import dataclass

@dataclass(frozen=True)
class OllamaConfig:
    base_url: str = "http://127.0.0.1:11434"
    model: str = "qwen3.6:35b"

class OllamaAdapter:
    """Minimal stdlib-only Ollama adapter for the local model boundary."""

    def __init__(self, config: OllamaConfig):
        self.config = config

    def generate(self, *, system: str, prompt: str) -> str:
        payload = json.dumps({
            "model": self.config.model,
            "system": system,
            "prompt": prompt,
            "stream": False,
        }).encode()
        request = urllib.request.Request(
            f"{self.config.base_url.rstrip('/')}/api/generate",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=300) as response:
            data = json.loads(response.read().decode())
        return data["response"]
