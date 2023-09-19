import numpy as np
import pyautogui
import pytesseract
import time
import pydirectinput
import multiprocessing
import cv2

def find_hp_image():
    try:
        lvl_location = pyautogui.locateOnScreen('level.png')
        if lvl_location is not None:
            x, y, width, height = lvl_location
            center_x = x + (width / 2)
            center_y = y + (height / 2)
            start_x = center_x + 110
            start_y = center_y - 10
            end_extend_x = 40
            end_extend_y = 15
            screenshot = pyautogui.screenshot(region=(start_x, start_y, end_extend_x, end_extend_y))
            hp_text = pytesseract.image_to_string(screenshot, lang='eng', config='--psm 6')
            return [True,hp_text]
    except Exception as e:
        return [False,0] 
    return [False,0] 

def find_mp_image():
    try:
        lvl_location = pyautogui.locateOnScreen('level.png')
        if lvl_location is not None:
            x, y, width, height = lvl_location
            center_x = x + (width / 2)
            center_y = y + (height / 2)
            start_x = center_x + 110
            start_y = center_y + 5
            end_extend_x = 40
            end_extend_y = 15
            screenshot = pyautogui.screenshot(region=(start_x, start_y, end_extend_x, end_extend_y))
            mp_text = pytesseract.image_to_string(screenshot, lang='eng', config='--psm 6')
            return [True,mp_text]
    except Exception as e:
        return [False,0] 
    return [False,0] 

def process_hp(min_hp, hp_button_list):
    while True:
        hp_output = find_hp_image()
        if hp_output[0] == True:
            try:
                hp = int(hp_output[1][:-2])
                if hp < min_hp:
                    for button in hp_button_list:
                        pydirectinput.keyDown(button)
                        time.sleep(0.1)
                        pydirectinput.keyUp(button)
                        time.sleep(0.1)
            except Exception as e:
                pass

def process_mp(min_mp, mp_button_list):
    while True:
        mp_output = find_mp_image()
        if mp_output[0] == True:
            try:
                mp = int(mp_output[1][:-2])
                if mp < min_mp:
                    for button in mp_button_list:
                        pydirectinput.keyDown(button)
                        time.sleep(0.1)
                        pydirectinput.keyUp(button)
            except Exception as e:
                pass

if __name__ == '__main__':
    hp_button = input("HP Potion Button (Seperate by ',') (default 2) :").split(',')
    hp_to_heal = input("HP Before Heal (remember it's might be delay before heal) (default 3000) :")
    mp_button = input("MP Potion Button (Seperate by ',') (default 1) :").split(',')
    mp_to_heal = input("MP Before Heal (remember it's might be delay before heal) (default 3000) :")
    if hp_button == ['']:
        hp_button = '2'
    if hp_to_heal == '':
        hp_to_heal = '3000'
    if mp_button == ['']:
        mp_button = '1'
    if mp_to_heal == '':
        mp_to_heal = '3000'

    process1 = multiprocessing.Process(target=process_hp, args=(int(hp_to_heal), hp_button))
    process2 = multiprocessing.Process(target=process_mp, args=(int(mp_to_heal), mp_button))

    process1.start()
    process2.start()

    process1.join()
    process2.join()