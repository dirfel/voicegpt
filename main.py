from plugins.temporizador import calcular_tempo_decorrido, iniciar_tempo
import os                       # Gerencia pastas e arquivos do sistema operacional
import whisper                  # Transcreve voz em texto
from gpt4all import GPT4All
import plugins.recorder       # Grava audio usando o microfone
from plugins.transcriebe import carregar_sintetizador, sintetizar_voz, transcrever_audio      # converte voz <-> texto


tempo_carregamento = iniciar_tempo()
status = 'wait' # define o status inicial do bot.
modo_online = False # define se o bot está autorizado a buscar informações do GPT4ALL online
max_tokens = 100 # tamanho máximo da resposta
system_user = 'dirce' # nome do usuario no sistema windows
modelo_gpt = 'mistral-7b-openorca.Q4_0.gguf' # modelo salvo no PC
modelo_whisper = 'tiny' # baixa modelo
tem_gpu = False # marcar true caso o usuario possua placa de vídeo (GPU)


# Inicializa os plugins
engine = carregar_sintetizador() 
model_gpt = GPT4All('C:/Users/{}/AppData/Local/nomic.ai/GPT4All/{}'.format(system_user, modelo_gpt), allow_download = modo_online)
model_whisper = whisper.load_model(modelo_whisper) 
calcular_tempo_decorrido(tempo_carregamento, 'carregamento inicial')
# inicializa o aplicativo propriamente dito
while True: # fica sempre funcionando
    if status == 'wait': # Nessa situação, o Bot fica aguardando o usuario falar o nome dele
        sintetizar_voz(engine, 'Olá, eu sou o Super Robô, seu assistente virtual de Inteligência Artificial, se precisar de mim, é só me chamar.')
        print('whisper aguardando a palavra chave (super) para mudar para status = "in"')
        audio = plugins.recorder.gravar_audio()
        tempo_carregamento = iniciar_tempo()
        transcricao = transcrever_audio(model_whisper, audio, tem_gpu)
        calcular_tempo_decorrido(tempo_carregamento, 'transcrição de texto')
        os.remove(audio)
        print('Humano: ', transcricao)
        if transcricao.lower().strip().startswith('super'):
            print('Chamou super')
            status = 'in'
            while status == 'in': # nessa situação o bot foi acionado, está ouvindo e aguardando por ordens
                with model_gpt.chat_session(): 
                    print('Fale seu prompt')
                    audio = plugins.recorder.gravar_audio(duracao=10)
                    tempo_carregamento = iniciar_tempo()
                    prompt = transcrever_audio(model_whisper, audio, tem_gpu)
                    calcular_tempo_decorrido(tempo_carregamento, 'transcrição de texto (2)')
                    print('Humano: ', prompt)
                    os.remove(audio)
                    tempo_carregamento = iniciar_tempo()
                    resposta = model_gpt.generate(prompt,max_tokens=max_tokens,temp=0.2,streaming=False)
                    calcular_tempo_decorrido(tempo_carregamento, 'Gerando resposta')
                    if resposta.strip() == '' or 'tchau' in resposta.strip().lower() or 'adeus' in resposta.strip().lower() or 'até mais' in resposta.strip().lower() or resposta.strip().lower() == 'sair':
                        sintetizar_voz(engine, 'Até logo!')
                        status = 'wait'
                    if status == 'in':
                        print('Super Robô: ', resposta)
                        sintetizar_voz(engine, resposta)
                        sintetizar_voz(engine, 'Com o que mais posso ajudar?')
