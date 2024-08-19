# pip install pyautogui
import pyautogui as pa
import time

p1 = (2534,370)             # Coordenadas da tela, coletada com o outro script "getPosicaoMouse.py"
p2 = (2494,1344)
p3 = (3780,910)
p4 = (2494,744)

for i in range(10):         # repete 10 vezes por causa do "for"
    pa.moveTo(p1)           # move o mouse pro primeiro item da pedidos integrados
    time.sleep(1)           # espera 1 segundo
    pa.click()              # clica no item que o mouse ta em cima
    time.sleep(1) 
    pa.scroll(-200000, p3)  # rola a pagina pra baixo la no fim
    time.sleep(1)
    pa.moveTo(p2)           # se move pro botão de envio de pedido pro ERP
    time.sleep(2)           # espera 2 segundos pra dar tempo de ajustar o mouse caso não tenha mais do que 4 itens (no caso o ponteiro do mouse não vai estar em cima do botão)
    pa.click()              # clica pra enviar
    time.sleep(1)
    pa.moveTo(p3)           # move o ponteiro do mouse pra cima do popup de confirmar envio
    time.sleep(1)
    pa.click()              # clica no envio
    time.sleep(30)          # espera 30 segundos
    pa.scroll(200000, p3)   # rola a pagina pra cima
    pa.moveTo(p4)           # move o ponteiro do mouse pra cima do botão voltar
    time.sleep(1)
    pa.click()              # clica pra voltar
    time.sleep(1)
