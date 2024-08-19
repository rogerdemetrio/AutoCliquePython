# pip install pyautogui
import pyautogui as pa
import time

# Esse script é usado para coletar as coordenadas do mouse para serem ajustadas no script "telaAutoCiqueEnviaERP.py"

mx,my = pa.position()   # pega a posição do mouse e passa pras variáveis
time.sleep(1)           # espera 2 segundos
print(f'({mx},{my})')   # printa no terminal as coordenadas onde o mouse está no momento
