import time

def iniciar_tempo():
    """Captura o timestamp inicial."""
    return time.time()

def calcular_tempo_decorrido(timestamp_inicial, acao):
    """Calcula o tempo decorrido desde o timestamp inicial."""
    tempo_atual = time.time()
    tempo_decorrido = tempo_atual - timestamp_inicial
    print(f"Tempo decorrido: {tempo_decorrido} segundos em {acao}")
