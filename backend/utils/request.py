import requests

from backend.service.llm import OllamaClient

# def ask_assistent(llm_engine: OllamaClient, prompt: str, system: str, stream: bool = False) -> dict:
#     req = llm_engine.ask(prompt=prompt)
#     r = requests.post(
#         url=req['url'], headers=req['headers'], json=req['data']
#     )

#     try:
#         return r.json()
#     except:
#         return {'error': r.text}


def chat(
    llm_engine: OllamaClient, content: str, system_content: str, stream: bool = False
) -> str:
    character = llm_engine.load_promt(system_content)
    r = llm_engine.conversation(content=content, charater=character, stream=stream)
    return r["message"]["content"]
