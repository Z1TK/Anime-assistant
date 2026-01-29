import os


class LLMClient:
    def __init__(self, model: str, host: str) -> None:
        self.model = model
        self.host = host
        self.headers = {
            "Authorization": f'Bearer {os.environ.get("OLLAMA_API_KEY")}',
            "Content-Type": "application/json",
        }

    def get_character(self, file_path) -> str:
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
        url = f"{self.host}/api/chat"
        message = [
            {"role": "system", "content": charater},
            {"role": "user", "content": content},
        ]
        data = {
            "model": self.model,
            "message": message,
            "stream": stream,
        }

        return {"url": url, "headers": self.headers, "data": data}
