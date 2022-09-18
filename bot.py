from selenium import webdriver as opcoes
from selenium.webdriver.common.by import By
import pyautogui as time 

meuNavegador = opcoes.Chrome() 

meuNavegador.get('https://blaze.com/pt/games/double')

time.sleep(5)


num = meuNavegador.find_elements(By.CLASS_NAME, 'sm-box')

lista = []


for x in range(16):
    c = num[x].text
    if c:
        lista.append(c)
    else:
        lista.append('0')
        
print(lista)
