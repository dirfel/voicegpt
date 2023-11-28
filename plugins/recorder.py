import sounddevice as sd
import wavio
import time

def gravar_audio(duracao=5, taxa_amostragem=44100):

    timestamp = int(time.time())
    nome_arquivo = f"{timestamp}.wav"
    # Capturar áudio
    print('Ouvindo')
    audio = sd.rec(int(duracao * taxa_amostragem), samplerate=taxa_amostragem, channels=2, dtype='float32')
    sd.wait()
    print('Parou de ouvir')

    # Salvar arquivo WAV
    wavio.write(nome_arquivo, audio, taxa_amostragem, sampwidth=3)

    print(f"Áudio gravado e salvo em: {nome_arquivo}")
    return nome_arquivo

# Exemplo de uso
