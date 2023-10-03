import numpy as np
import pyautogui 
import pytesseract
import time
import pydirectinput
# import multiprocessing
# import cv2
import keyboard
# import re
# import threading
import os
import concurrent.futures
import psutil

global HP
global MP

pyautogui.FAILSAFE = False
pydirectinput.FAILSAFE = False


def extract_numbers(text):
    numbers = []
    number_str_out = ''
    for word in text:
        
        try:
            number = int(word)
            number_str_out += word
        except ValueError:
            pass
    return int(number_str_out)


def find_hp_image():
    try:
        lvl_location = pyautogui.locateOnScreen('level.png')
        if lvl_location is not None:
            x, y, width, height = lvl_location
            center_x = x + (width / 2)
            center_y = y + (height / 2)
            start_x = center_x + 119
            start_y = center_y - 10
            end_extend_x = 26
            end_extend_y = 15
            screenshot = pyautogui.screenshot(region=(start_x, start_y, end_extend_x, end_extend_y))
            grayscale_screenshot = screenshot.convert('L')
            hp_text = pytesseract.image_to_string(grayscale_screenshot, config='--psm 6')
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
            start_x = center_x + 119
            start_y = center_y + 5 + 2
            end_extend_x = 26
            end_extend_y = 11

            screenshot = pyautogui.screenshot(region=(start_x, start_y, end_extend_x, end_extend_y))
            grayscale_screenshot = screenshot.convert('L')
            # grayscale_screenshot.show()
            mp_text = pytesseract.image_to_string(grayscale_screenshot, config='--psm 6')
            return [True,mp_text]
    except Exception as e:
        return [False,0] 
    return [False,0] 


def find_complete_image():
    while True:
        target_image_path = './pic/complete.png'
        try:
            location = pyautogui.locateOnScreen(target_image_path, confidence=0.75)
            if location is not None:
                x, y, width, height = location
                center_x = x + (width / 2)
                center_y = y + (height / 2)

                pyautogui.click(center_x, center_y)
                time.sleep(1)
                pyautogui.click(center_x, center_y)
        except Exception as e:
            pass
        # pause loop
        if keyboard.is_pressed('shift'):
            i = 0
            while True:
                if i ==0:
                    print('pause QQ loop (spam alt to continue)')
                if keyboard.is_pressed('alt'):
                    print()
                    break
                i += 1
            print('continue QQ loop... (spam shift to pause loop)')


def find_jig_image():
    while True:
        for i in range(1,10):
            try:
                target_image_path = f"./pic/jig{i}.png"
            except Exception as e:
                print(e)
            try:
                location = pyautogui.locateOnScreen(target_image_path, confidence=0.75)
                if location is not None:
                    x, y, width, height = location
                    center_x = x + (width / 2)
                    center_y = y + (height / 2)

                    pyautogui.rightClick(center_x, center_y)
            except Exception as e:
                pass
            # pause loop
            if keyboard.is_pressed('shift'):
                i = 0
                while True:
                    if i ==0:
                        print('pause jig loop (spam alt to continue)')
                    if keyboard.is_pressed('alt'):
                        print()
                        break
                    i += 1
                print('continue jig loop... (spam shift to pause loop)')


def process_mp_fill_image():
    while True:
        try:
            target_image_path = f"./pic/mp_fill.png"
            mp_pack_image_path = f"./pic/mp_pack.png"
        except Exception as e:
            print(e)
        try:
            location = pyautogui.locateOnScreen(target_image_path, confidence=0.90)
            if location is not None:
                x, y, width, height = location
                center_x = x + (width / 2)
                center_y = y + (height / 2)

                pyautogui.leftClick(center_x, center_y)
                mp_pack_location = pyautogui.locateOnScreen(mp_pack_image_path, confidence=0.90)
                if mp_pack_location is not None:
                    x_mp_pack, y_mp_pack, width_mp_pack, height_mp_pack = mp_pack_location
                    center_x_mp_pack = x_mp_pack + (width_mp_pack / 2)
                    center_y_mp_pack = y_mp_pack + (height_mp_pack / 2)
                    pyautogui.leftClick(center_x_mp_pack, center_y_mp_pack)
                    time.sleep(300)

        except Exception as e:
            pass
        # pause loop
        if keyboard.is_pressed('shift'):
            i = 0
            while True:
                if i ==0:
                    print('pause mp fill loop (spam alt to continue)')
                if keyboard.is_pressed('alt'):
                    print()
                    break
                i += 1
            print('continue mp fill loop... (spam shift to pause loop)')


def process_hp(min_hp, hp_button_list):
    times = 0
    while True:
        if min_hp == 0:
            pydirectinput
            pydirectinput.keyDown(hp_button_list[0])
            time.sleep(0.1)
            pydirectinput.keyUp(hp_button_list[0])
            time.sleep(1)
        else:
            times += 1
            if times >= 14001:
                pydirectinput.press('R')
                time.sleep(0.1)
                times = 0
            hp_output = find_hp_image()
            if hp_output[0] == True:
                try:
                    ex_hp = extract_numbers(hp_output[1])
                    hp = ex_hp if (ex_hp > 1000) and (ex_hp < 9999) else 9999
                    if hp < min_hp:
                        for button in hp_button_list:
                            pydirectinput.keyDown(button)
                            time.sleep(0.1)
                            pydirectinput.keyUp(button)
                            time.sleep(0.1)
                except Exception as e:
                    pass
        # pause loop
        if keyboard.is_pressed('shift'):
            i = 0
            while True:
                if i ==0:
                    print('pause hp loop (spam alt to continue)')
                if keyboard.is_pressed('alt'):
                    print()
                    break
                i += 1
            print('continue hp loop... (spam shift to pause loop)')


def process_mp(min_mp, button):
    times = 0
    while True:
        if min_mp == 0:
            pydirectinput.keyDown(button)
            time.sleep(0.1)
            pydirectinput.keyUp(button)
            time.sleep(1)
        else:
            if times >= 30:
                pydirectinput.keyDown(button)
                time.sleep(0.1)
                pydirectinput.keyUp(button)
                times = 0
            mp_output = find_mp_image()
            if mp_output[0] == True:
                try:
                    ex_mp = extract_numbers(mp_output[1])
                    mp = ex_mp if (ex_mp > 1000) and (ex_mp < 9999) else 9999
                    if mp < min_mp:
                        pydirectinput.keyDown(button)
                        time.sleep(0.1)
                        pydirectinput.keyUp(button)
                        times = 0
                except Exception as e:
                    times +=1 
            else:
                times +=1 
        # pause loop
        if keyboard.is_pressed('shift'):
            i = 0
            while True:
                if i ==0:
                    print('pause mp loop (spam alt to continue)')
                if keyboard.is_pressed('alt'):
                    print()
                    break
                i += 1
            print('continue mp loop... (spam shift to pause loop)')


if __name__ == '__main__':
    print("Mode 1 => HP:5500(2) || MP:6000(1)")
    print("Mode 2 => HP:6000(2) || MP:7000(1)")
    print("Mode 3 => Spam HP,.MP")
    print("Mode 4 => Do nothing just QQ and clear jig")
    
    default = input("Select Mode (1 , 2 or n) :")
    if default == '1':
        hp_button = ['2']
        hp_to_heal = '5500'
        mp_button = '1'
        mp_to_heal = '6000'
    elif default == '2':
        hp_button = ['2']
        hp_to_heal = '6000'
        mp_button = '1'
        mp_to_heal = '7000'
    elif default == '3':
        hp_button = ['2']
        hp_to_heal = '0'
        mp_button = '1'
        mp_to_heal = '0'
    elif default == '4':
        hp_button = ['2']
        hp_to_heal = '0'
        mp_button = '1'
        mp_to_heal = 'A'
    else:
        hp_button = input("HP Potion Button (Seperate by ',') (default 2) :").split(',')
        hp_to_heal = input("HP Before Heal (remember it's might be delay before heal) (default 3000) :")
        mp_button = input("MP Potion Button (Seperate by ',') (default 1) :").split(',')
        mp_to_heal = input("MP Before Heal (remember it's might be delay before heal) (default 3000) :")
    print(f"heal HP ({hp_button} when hp < {hp_to_heal})")
    print(f"heal MP ({mp_button} when mp < {mp_to_heal})")
    print('Starting heal soon ... (spam shift to pause loop)')
    if default != '4':
        cpu_cores_hp = [0,1]  # List of CPU cores for the HP thread
        cpu_cores_mp = [2,3]  # List of CPU cores for the MP thread
    else:
        cpu__mp_fill = [0,1] 
        
    cpu_cores_complete = [4,5]
    cpu_cores_jig = [6,7]
    # Set CPU core affinity for the HP and MP threads
    # current_process = psutil.Process()
    # current_process.cpu_affinity(cpu_cores_hp)
    
    # Create ThreadPoolExecutor with maximum thread count equal to the number of cores
    if default != '4':
        max_threads = len(cpu_cores_hp) + len(cpu_cores_mp) + len(cpu_cores_complete) + len(cpu_cores_jig)
    else:
        max_threads = len(cpu_cores_complete) + len(cpu_cores_jig) + len(cpu__mp_fill)
    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        if default != '4':
            hp_future = executor.submit(process_hp, int(hp_to_heal), hp_button)
            mp_future = executor.submit(process_mp, int(mp_to_heal), mp_button)
        else:
            mp_fill = executor.submit(process_mp_fill_image)
        complete_future = executor.submit(find_complete_image)
        jig_future = executor.submit(find_jig_image)
        
        if default != '4':
            hp_result = hp_future.result()
            mp_result = mp_future.result()
        else:
            mp_fill_result = mp_fill.result()
        complete_result = complete_future.result()
        jig_result = jig_future.result()