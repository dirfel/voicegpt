import whisper
import pyttsx3

def transcrever_audio(model: whisper, path: str, tem_gpu):
    result = model.transcribe(path, fp16=tem_gpu)
    return result["text"]

def carregar_sintetizador():
    return pyttsx3.init()

def sintetizar_voz(engine, texto: str):
    engine.say(texto)
    engine.runAndWait()