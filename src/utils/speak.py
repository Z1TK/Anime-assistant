import time

import keyboard

from src.stt import AudioStreamSTT
from src.tts import AudioStreamTTS

def listen(stt: AudioStreamSTT, rate: int, chunk: int) -> str:
    stt.start(rate, chunk)
    keyboard.wait("alt")
    print('запись...')
    command = []

    try:
        while keyboard.is_pressed("alt"):
            command.append(stt.record())
            time.sleep(chunk / rate)

        record = stt.bytes_to_array(command)

        audio = stt.transcribe(record, "ru")

        # if audio == "":
        #     print("Пользователь ничего не сказал")
        #     continue

        # if audio.strip(" .,!?\n").lower() == "выход":
        #     break
    finally:
         stt.close()

    print('отправка команды')
    return audio

def reply_assistant(tts: AudioStreamTTS, chunk: int, audio: str) -> None:
    tts.start(chunk)

    print('начинаю обработку')
    try:
        reply_array = tts.synthesizing(
            text=audio,
            lang="ru",
            temperature=0.7,
            speed=1.0,
            wav=[
                "samples/sample_1.wav",
                "samples/sample_2.wav",
            ],
        )

        reply = tts.array_to_bytes(reply_array)
        tts.voice(reply)
    finally:
        tts.close()
