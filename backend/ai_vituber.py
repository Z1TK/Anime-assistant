from backend.service.llm import LLMClient
from backend.service.stt import AudioStreamSTT
from backend.service.tts import AudioStreamTTS
from backend.utils.request import ask_assistent, chat
from backend.utils.search import open_site, request_to_youtube
from backend.utils.speak import listen_commands, speak_assistant


def ai_assistant(
    stt: AudioStreamSTT,
    tts: AudioStreamTTS,
    llm: LLMClient,
    rate_size: int,
    chunk_size: int,
) -> None:
    stt.start(rate_size, chunk_size)
    tts.start(chunk_size)

    try:
        while True:
            text = listen_commands(stt_engine=stt, rate=rate_size, chunk=chunk_size)

            if text == "":
                print("Пользователь ничего не сказал")
                continue
            if text.strip(" .,!?\n").lower() == "выход":
                break
            command = text.strip(" .,!?\n").lower()
            if open_site(command):
                continue
            if request_to_youtube(command):
                continue

            # thinking = ask_assistent(llm_engine=llm, prompt=text)
            thinking = chat(
                llm_engine=llm, content=text, system_content="character.txt"
            )
            reply = thinking["response"]

            speak_assistant(tts_engine=tts, audio=reply)
            print(reply)
    finally:
        tts.close()
        stt.close()
