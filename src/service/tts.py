import numpy as np
import pyaudio
from TTS.api import TTS


class AudioStreamTTS:
    def __init__(self, model: str, device: str = "cpu"):
        self.tts = TTS(model).to(device)
        self.p = pyaudio.PyAudio()
        self.stream = None

    def start(self, sample_rate: int, chunk_size: int) -> None:
        self.stream = self.p.open(
            format=pyaudio.paFloat32,
            rate=sample_rate,
            channels=1,
            frames_per_buffer=chunk_size,
            output=True,
        )

    def synthesizing(self, text: str, wav: list[str], lang: str) -> None:
        audio = self.tts.tts(
            text=text,
            speaker_wav=wav,
            language=lang,
        )
        audio32 = np.asarray(audio, np.float32)
        self.stream.write(audio32.tobytes())

    def close(self) -> None:
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()
