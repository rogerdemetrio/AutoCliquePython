# pip install pyautogui
import pyautogui as pa
import time

p1 = (532,690)
p2 = (1170,650)
p3 = (1290,350)
x = 0

for i in range(20):
    x = x + 0   
    time.sleep(2) 
    pa.moveTo(p1)
    time.sleep(1)    
    pa.click()   
    time.sleep(1)
    pa.moveTo(p2)
    time.sleep(1)    
    pa.click()   
    time.sleep(4)
    
    pa.moveTo(p3)  
    time.sleep(1)
    #pa.scroll(-2160 - x, p3)
    pa.click()   