# O que é?
O VoiceGPT é um mecanismo que utiliza plugins de inteligência artificial para permitir um chat com a maquina por voz.
#
[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-lightgrey?logo=github&style=for-the-badge)](https://github.com/sponsors/dirfel)
# Como funciona?
Funciona parecido como uma ALEXA, que ao executar o arquivo main.py, o bot conversará com você. Caso você fale a palavra "SUPER" no inicio da frase, o bot entrará no modo pergunta, dessa forma, o que for falado com o bot será processado por um Large Language Model (LLM), semelhante ao Chat GPT e a resposta será sintetizada para o usuário.

# Vantagens
- Funciona 100% offline (privacidade)
- Permite a escolha de modelos mais eficientes ou mais leves conforme sua demanda

# Desvantagens
- O desempenho depende da capacidade de processamento da CPU e/ou GPU
- Exige alta quantidade de memória RAM mínimo 8gb, reccomendado 20gb+
- Dependendo do modelo de LLM, pode ocupar muito espaço no disco rígido.
- O chat não é fluido, uma vez que o bot captura o audio, transcreve, processa no GPT4ALL e retorna a resposta por voz ao usuário.

# Instalando e executando
1. Instalar python 3.11
2. Criar um Ambiente Virtual (venv) e executar
3. Instalar os itens de requeriments.txt
4. Baixar o modelo de GPT4ALL desejado
5. Abrir o arquivo main.py e alterar as variáveis desejadas (atenção ao local e nome do modelo)
6. executar main.py

# TODO (Pull Requests serão bem vindas)
- Implementar LocalDocs
- tornar chat mais performático e fluido
- parametrizar dinamicamente o atributo max_tokens conforme a pergunta do usuário
- permitir a captura do audio, transcrição e processamento simultanemente (exige alto poder computacional)
- melhorar o arquivo readme.md

#
[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-lightgrey?logo=github&style=for-the-badge)](https://github.com/sponsors/dirfel)
