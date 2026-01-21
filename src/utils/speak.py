from src.stt import AudioStreamSTT
from src.tts import AudioStreamTTS
import keyboard

def speak(stt: AudioStreamSTT, tts: AudioStreamTTS) -> None:
    while True:
        keyboard.wait('alt')
        print('Запись...')

        while keyboard.is_pressed('alt'):
            command = stt.record(seconds=10)

        audio = stt.transcribe(
            command,
            'ru'
        )

        if audio == '':
            print('Пользователь ничего не сказал')
            continue

        if audio == 'выход':
            break

        tts.synthesizing(
                text=audio,
                lang="ru",
                temperature=0.7,
                speed=1.0,
                wav=[
                    "samples/sample_1.wav",
                    "samples/sample_2.wav",
                ],
            )

    tts.close()
    stt.close()