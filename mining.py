import pyautogui
import pytesseract
import time
import pydirectinput

def find_image(target_image_path):
    try:
        location = pyautogui.locateOnScreen(target_image_path)
        if location is not None:
            x, y, width, height = location
            center_x = x + (width / 2)
            center_y = y + (height / 2)
            return [True,center_x,center_y]
    except Exception as e:
        print(f"Exception: {str(e)}")
        return [False,'_','_'] 
    return [False,'_','_'] 

picaxe_image_path = 'picaxe.png'
empty_weapon_slot_image_path = 'empty_weapon_slot.png'
ok_button_image_path = 'ok.png'
cancel_button_image_path = 'cancel.png'

while True: 
    ok_button = find_image(ok_button_image_path)
    if ok_button[0] == True:
        pyautogui.click(ok_button[1], ok_button[2])
        time.sleep(0.1)
        pyautogui.click(ok_button[1], ok_button[2])
    time.sleep(0.5)
    cancel_button = find_image(cancel_button_image_path)
    if cancel_button[0] == True:
        pyautogui.click(cancel_button[1], cancel_button[2])
        time.sleep(0.1)
        pyautogui.click(cancel_button[1], cancel_button[2])
    time.sleep(0.5)
    empty_weapon_slot_found = find_image(empty_weapon_slot_image_path)
    if empty_weapon_slot_found[0] == True:
        while True:
            picaxe_found = find_image(picaxe_image_path)
            if picaxe_found[0] == True:
                pyautogui.click(picaxe_found[1], picaxe_found[2])
                time.sleep(0.1)
                pyautogui.click(picaxe_found[1], picaxe_found[2])
                time.sleep(1.5)
                break
    time.sleep(0.5)
    pydirectinput.keyDown('space')
    time.sleep(1)
    pydirectinput.keyUp('space')
    time.sleep(1)
