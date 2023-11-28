from gpt4all import GPT4All

def inicializar_gpt(system_user, modelo_gpt, modo_online=False):
    # inicializa do modelo GPT
    try:
        print("inicializou GPT4ALL")
        return GPT4All('C:/Users/{}/AppData/Local/nomic.ai/GPT4All/{}'.format(system_user, modelo_gpt), 
                       allow_download = modo_online)
        # model = GPT4All(modelo, allow_download = modo_online)
    except:
        print('Não foi possível importar o modelo.')
        exit()