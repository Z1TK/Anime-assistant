import requests

from backend.service.llm import LLMClient

# def ask_assistent(llm_engine: LLMClient, prompt: str, system: str, stream: bool = False) -> dict:
#     req = llm_engine.ask(prompt=prompt)
#     r = requests.post(
#         url=req['url'], headers=req['headers'], json=req['data']
#     )

#     try:
#         return r.json()
#     except:
#         return {'error': r.text}


def chat(
    llm_engine: LLMClient, content: str, system_content: str, stream: bool = False
) -> dict:
    character = llm_engine.get_character(system_content)
    req = llm_engine.conversation(content=content, charater=character, stream=stream)
    r = requests.post(url=req["url"], headers=req["headers"], json=req["data"])
    try:
        return r.json()
    except:
        return {"error": r.text}
