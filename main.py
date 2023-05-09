# Automação de pyautogui para controlar o mouse e o teclado
import pyautogui as pa 
import time
#Biblioteca para permitir acentos na digitação
import pyperclip

#Tempo de execução 
pa.PAUSE = 1

#Tecla windows
pa.press('win')

#Escrever o comando
pa.write("Google")

#Entrar no navegador
pa.press('ENTER')

#Escrever o comando
pa.write("youtube.com")

#Entrar no Youtube
pa.press('ENTER')

#Clicar na barra de tarefas do Youtube. Aqui vai depender muito das coordenadas do seu computador,os valores de x e y não são fixos. 
time.sleep(4)
pa.click(x=613, y=99)

# Fazer a pesquisa 
pa.write("Metallica") #Qualquer nome que você quiser 
pa.hotkey('ctrl' ,'v')

Google
youtube.com
