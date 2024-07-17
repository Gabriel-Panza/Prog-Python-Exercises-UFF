import pyautogui
import time

def press_key(keys,interval):
    cooldown = 0
    while True:
        pyautogui.press(keys[0])
        time.sleep(interval/2)
        #if cooldown%2 == 0:
        pyautogui.press(keys[1])
        time.sleep(interval/2)
        if cooldown%4 == 0:
            pyautogui.press(keys[2])
            time.sleep(interval/2)
            pyautogui.press(keys[3])
        
        time.sleep(interval)
        cooldown+=1

# Pressiona a tecla 'a' a cada 5 segundos
time.sleep(3)
press_key(['2','3','4','5'], 2)