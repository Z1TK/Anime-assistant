import os

from ollama import Client


class OllamaClient:
    def __init__(self, model: str, host: str) -> None:
        self.client = Client(
            host=host,
            headers={"Authorization": f'Bearer {os.getenv("OLLAMA_API_KEY")}'},
        )
        self.model = model

    def load_promt(self, file_path) -> str:
        with open(file_path, "r", encoding="utf-8") as file:
            ch = file.read()
        return ch

    # def ask(self, prompt: str, system: str, stream: bool) -> dict:
    #     url = f"{self.host}/api/generate"
    #     data = {
    #         "model": self.model,
    #         "prompt": prompt,
    #         "stream": stream,
    #         "system": system,
    #     }

    #     return {"url": url, "headers": self.headers, "data": data}

    def conversation(self, content: str, charater: str, stream: bool = False) -> dict:
        message = [
            {"role": "system", "content": charater},
            {"role": "user", "content": content},
        ]
        res = self.client.chat(self.model, messages=message, stream=stream)
        return res
