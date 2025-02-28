'''
    EXERCÍCIO
Entrar no primeiro vídeo da série de survivel do jazzghost
    Tecnologias: 
python
Pyautogui
time
'''

# Importando bibliotecas
import pyautogui as pg
import time

# Dando pausa de uma linha de código para outra.
pg.PAUSE = 0.5

# Pegar posição do mouse
# time.sleep(10)
# print(pg.position())

# Abrindo navegador
pg.press('win')
time.sleep(1)
pg.write('chrome')
time.sleep(1)
pg.press('enter')
time.sleep(3)

# Abrindo youtube
pg.click(x=602, y=429)
time.sleep(3)
pg.write('https://www.youtube.com')
time.sleep(1)
pg.press('enter')
time.sleep(10)

# Pesquisando playlist
pg.click(x=600, y=115)
time.sleep(1.5)
pg.write('jazzghost minecraft survivel')
time.sleep(1.5)
pg.press('enter')
time.sleep(5)

# Iniciando vídeo/playlist
pg.click(x=530, y=629)
time.sleep(2)