import pyautogui as pa
import time
import platform
import pygetwindow as gw

# Função para realizar a pesquisa
def realizar_pesquisa(pesquisa):
    global realizou_primeira_pesquisa  # Definir a variável como global
    # Abrir o navegador apenas na primeira pesquisa
    if not realizou_primeira_pesquisa:
        if platform.system() == "Windows":
            comando = "Brave"  # Pode ser substituído pelo navegador desejado
        elif platform.system() == "Darwin":
            comando = "open"
        else:
            comando = "xdg-open"

        pa.hotkey('ctrl', 'esc')  # Abre o menu Iniciar no Windows
        pa.write(comando)
        pa.press('enter')
        time.sleep(1)
        realizou_primeira_pesquisa = True

    # Digitar a pesquisa na barra do navegador
    pa.write(pesquisa)
    pa.press('enter')
    time.sleep(5)  # Aguardar o carregamento da página

# Tempo de espera
pa.PAUSE = 1

# Variável para controlar se a primeira pesquisa já foi realizada
realizou_primeira_pesquisa = False

# Loop principal
while True:
    # Perguntar ao usuário o que ele deseja pesquisar no navegador
    pesquisa = input("Digite o que você deseja pesquisar no navegador: ")

    # Realizar a pesquisa se a entrada do usuário não for "não" ou "não entendi"
    if pesquisa.lower() not in ["não", "não entendi"]:
        # Realizar a pesquisa
        realizar_pesquisa(pesquisa)

        # Redefinir realizou_primeira_pesquisa para False antes de cada nova pesquisa
        realizou_primeira_pesquisa = False
    else:
        continue

    # Perguntar se deseja realizar outra pesquisa
    while True:
        continuar = input("Deseja pesquisar mais alguma coisa? (sim/não): ").lower()

        if continuar in ("sim", "não"):
            break
        else:
            print("Desculpe, não entendi.")

    # Verificar a resposta do usuário
    if continuar == "não":
        break  # Encerrar o loop se a resposta for "não"