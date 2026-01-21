from src.tts import AudioStreamTTS
from src.stt import AudioStreamSTT
from src.utils.speak import speak

def run():
    tts = AudioStreamTTS("tts_models/multilingual/multi-dataset/xtts_v2", "cuda")
    stt = AudioStreamSTT('large-v2', 'cpu', type='int8')
    
    stt.start(16000, 1024)
    tts.start(1024)

    print('Помщник готов к работе')
    speak(stt, tts)

if __name__ == "__main__":
    run()
