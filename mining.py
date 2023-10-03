import pyautogui
import pytesseract
import time
import pydirectinput
import keyboard

picaxe_image_path = 'picaxe.png'
empty_weapon_slot_image_path = 'empty_weapon_slot.png'
image_path_list = [
    'ok.png',
    'ok_old.png',
    'cancel.png',
    'cancel_2.png',
    'cancel_old.png',
    'close.png',
    # 'x.png',
]

def find_image(target_image_path):
    try:
        location = pyautogui.locateOnScreen(target_image_path, confidence=0.75)
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
    for image_path in image_path_list:
        button = find_image(image_path)
        if button[0] == True:
            pyautogui.click(button[1], button[2])
            time.sleep(0.1)
            pyautogui.click(button[1], button[2])
            button_name = image_path.split('.')[0]
            print(f'click : {button_name}')
 
def space_bar_action():
    pydirectinput.keyDown('space')
    time.sleep(0.1)
    pydirectinput.keyUp('space')
    time.sleep(0.1)


print('Starting mining soon ... (spam shift to pause loop)')
while True: 
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
