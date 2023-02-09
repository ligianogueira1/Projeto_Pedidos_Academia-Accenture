import os
import time

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def espera(segundos = 2):
    time.sleep(segundos)

def mensagem(mensagem, segundos = 2):
    limpar_tela()
    print(mensagem)
    espera(segundos)