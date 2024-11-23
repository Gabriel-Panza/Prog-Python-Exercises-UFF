import pyautogui
import time

def press_key(keys,interval):
    cooldown = 0
    while True:
        time.sleep(interval)
        if pyautogui.press(keys[4]):
            time.sleep(2*interval)
        pyautogui.press(keys[0])
        time.sleep(interval/2)
        if cooldown%6 == 0:
            pyautogui.press(keys[1])
        time.sleep(interval/2)
        if cooldown%8 == 0:
            pyautogui.press(keys[2])
            time.sleep(interval/2)
            pyautogui.press(keys[3])
        cooldown+=1

# Pressiona a tecla 'a' a cada 5 segundos
press_key(['2','3','4','5','Esc'], 2)