from src.service.tts import AudioStreamTTS


def run():
    tts_engine = AudioStreamTTS("tts_models/multilingual/multi-dataset/xtts_v2", "cuda")
    tts_engine.start(44100, 1024)

    while True:
        text = input()
        tts_engine.synthesizing(text=text, wav=["donate_sound.wav"], lang="ru")
        if text == "exit":
            break

    tts_engine.close()


if __name__ == "__main__":
    run()
