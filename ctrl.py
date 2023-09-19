import pyautogui
import keyboard
import time
import pydirectinput

def auto_click_ctrl():
    print('starting ctrl soon... (spam shift to pause loop)')
    while True:
        time.sleep(0.2)
        if keyboard.is_pressed('up'):
            continue  # Exit the loop if the arrow up key is pressed
        pydirectinput.press('ctrl')
        # pause loop
        if keyboard.is_pressed('shift'):
            while True:
                print('pause loop (spam alt to continue)', end='\r')
                if keyboard.is_pressed('alt'):
                    print()
                    break
            print('continue loop... (spam shift to pause loop)')
            

while True:
    auto_click_ctrl()