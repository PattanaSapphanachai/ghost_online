import pyautogui
import pytesseract
import time
import pydirectinput
import keyboard

picaxe_image_path = 'picaxe.png'
empty_weapon_slot_image_path = 'empty_weapon_slot.png'
ok_button_image_path = 'ok.png'
cancel_button_image_path = 'cancel.png'
close_button_image_path = 'close.png'
x_button_image_path = 'x.png'

def find_image(target_image_path):
    try:
        location = pyautogui.locateOnScreen(target_image_path, confidence=0.85)
        if location is not None:
            x, y, width, height = location
            center_x = x + (width / 2)
            center_y = y + (height / 2)
            return [True,center_x,center_y]
    except Exception as e:
        print(f"Exception: {str(e)}")
        return [False,'_','_'] 
    return [False,'_','_'] 

def skip_any_button():
    ok_button = find_image(ok_button_image_path)
    if ok_button[0] == True:
        pyautogui.click(ok_button[1], ok_button[2])
        time.sleep(0.1)
        pyautogui.click(ok_button[1], ok_button[2])
        print('click : ok')

    cancel_button = find_image(cancel_button_image_path)
    if cancel_button[0] == True:
        pyautogui.click(cancel_button[1], cancel_button[2])
        time.sleep(0.1)
        pyautogui.click(cancel_button[1], cancel_button[2])
        print('click : cancel')

    close_button = find_image(close_button_image_path)
    if close_button[0] == True:
        pyautogui.click(close_button[1], close_button[2])
        time.sleep(0.1)
        pyautogui.click(close_button[1], close_button[2])
        print('click : close')
    
    # x_button = find_image(x_button_image_path)
    # if x_button[0] == True:
    #     pyautogui.click(x_button[1], x_button[2])
    #     time.sleep(0.1)
    #     pyautogui.click(x_button[1], x_button[2])
    #     print('click : x')
 
def space_bar_action():
    pydirectinput.keyDown('space')
    time.sleep(0.1)
    pydirectinput.keyUp('space')
    time.sleep(0.1)

while True: 
    print('Starting mining soon ... (spam shift to pause loop)')
    
    skip_any_button()
    space_bar_action()

    empty_weapon_slot_found = find_image(empty_weapon_slot_image_path)
    if empty_weapon_slot_found[0] == True:
        while True:
            picaxe_found = find_image(picaxe_image_path)
            if picaxe_found[0] == True:
                pyautogui.click(picaxe_found[1], picaxe_found[2])
                time.sleep(0.1)
                pyautogui.click(picaxe_found[1], picaxe_found[2])
                time.sleep(0.1)
                break

    # pause loop
    if keyboard.is_pressed('shift'):
        while True:
            print('pause loop (spam alt to continue)', end='\r')
            if keyboard.is_pressed('alt'):
                print()
                break
        print('continue loop... (spam shift to pause loop)')
