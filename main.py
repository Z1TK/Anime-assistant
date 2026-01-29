from backend.service.stt import AudioStreamSTT
from backend.service.tts import AudioStreamTTS
from backend.service.llm import LLMClietn
from backend.ai_vituber import ai_assistant
import torch

def main():
    tts_engine = AudioStreamTTS('tts_models/multilingual/multi-dataset/xtts_v2', 'cuda')
    stt_engine = AudioStreamSTT('large-v2', 'cpu', type='int8')
    llm_engine = LLMClietn('gemini-3-flash-preview', 'https://ollama.com')

    '''
    gemini-3-flash-preview/kimi-k2-thinking/glm-4.7
    glm-4.6 
    deepseek-v3.2
    '''

    ai_assistant(
        stt=stt_engine,
        tts=tts_engine,
        llm=llm_engine,
        rate_size=16000,
        chunk_size=1024
    )
    
    # print(torch.cuda.is_available())          
    # print(torch.version.cuda)                
    # print(torch.backends.cudnn.version())    

if __name__ == '__main__':
    main()