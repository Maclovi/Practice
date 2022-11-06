import pyautogui as pg
import time

print('у тебя есть 5 сек')
time.sleep(5)

for i in range(5):
    pg.write(' ')
    time.sleep(0.1)
    pg.press('Enter')