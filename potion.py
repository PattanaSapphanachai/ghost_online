import pyautogui
import pytesseract
import time
import pydirectinput

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
            hp_text = pytesseract.image_to_string(screenshot, config='--psm 6 --oem 3')
            return [True,hp_text]
    except Exception as e:
        print(f"Exception: {str(e)}")
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
            mp_text = pytesseract.image_to_string(screenshot, config='--psm 6 --oem 3')
            return [True,mp_text]
    except Exception as e:
        print(f"Exception: {str(e)}")
        return [False,0] 
    return [False,0] 

while True:
    hp_output = find_hp_image()
    if hp_output[0] == True:
        try:
            hp = int(hp_output[1][:-2])
            if hp < 3000:
                pydirectinput.keyDown('2')
                time.sleep(0.1)
                pydirectinput.keyUp('2')
                time.sleep(0.1)
                pydirectinput.keyDown('3')
                time.sleep(0.1)
                pydirectinput.keyUp('3')
        except Exception as e:
            pass
    mp_output = find_mp_image()
    if mp_output[0] == True:
        try:
            mp = int(mp_output[1][:-2])
            if mp < 4000:
                pydirectinput.keyDown('1')
                time.sleep(0.1)
                pydirectinput.keyUp('1')
        except Exception as e:
            pass