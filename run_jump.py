import pydirectinput
import time
import threading
import keyboard
import pyautogui

exit_thread = False


def find_complete_image():
    global exit_thread
    while not exit_thread:
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

def find_jig_image():
    global exit_thread
    while not exit_thread:
        for i in range(1,10):
            try:
                target_image_path = f"./pic/jig{i}.png"
            except Exception as e:
                pass
            try:
                location = pyautogui.locateOnScreen(target_image_path, confidence=0.90)
                if location is not None:
                    x, y, width, height = location
                    center_x = x + (width / 2)
                    center_y = y + (height / 2)

                    pyautogui.rightClick(center_x, center_y)
            except Exception as e:
                pass

def process_hp_mp_fill_image():
    global exit_thread
    while not exit_thread:
        target_image_path = f"./hp_fill/hp.png"
        hp_pack_image_path = f"./hp_fill/hp_pack.png"
        try:
            location = pyautogui.locateOnScreen(target_image_path, confidence=0.90)
            if location is not None:
                x, y, width, height = location
                center_x = x + (width / 2)
                center_y = y + (height / 2)

                pyautogui.leftClick(center_x, center_y)
                hp_pack_location = list(pyautogui.locateAllOnScreen(hp_pack_image_path, confidence=0.90))
                if hp_pack_location is not None:
                    x_hp_pack, y_hp_pack, width_hp_pack, height_hp_pack = hp_pack_location[-1]
                    center_x_hp_pack = x_hp_pack + (width_hp_pack / 2)
                    center_y_hp_pack = y_hp_pack + (height_hp_pack / 2)
                    pyautogui.leftClick(center_x_hp_pack, center_y_hp_pack)
        except Exception as e:
            pass
        time.sleep(3)
        target_image_path = f"./hp_fill/mp.png"
        mp_pack_image_path = f"./hp_fill/mp_pack.png"
        try:
            location = pyautogui.locateOnScreen(target_image_path, confidence=0.90)
            if location is not None:
                x, y, width, height = location
                center_x = x + (width / 2)
                center_y = y + (height / 2)

                pyautogui.leftClick(center_x, center_y)
                mp_pack_location = list(pyautogui.locateAllOnScreen(mp_pack_image_path, confidence=0.90))
                if mp_pack_location is not None:
                    x_mp_pack, y_mp_pack, width_mp_pack, height_mp_pack = mp_pack_location[0]
                    center_x_mp_pack = x_mp_pack + (width_mp_pack / 2)
                    center_y_mp_pack = y_mp_pack + (height_mp_pack / 2)
                    pyautogui.leftClick(center_x_mp_pack, center_y_mp_pack)
        except Exception as e:
            pass
        time.sleep(300)

def skip_any_button():
    global exit_thread
    while not exit_thread:
        image_path_list = [
        'ok.png',
        'ok_old.png',
        'ok_new.png',
        'cancel.png',
        'cancel_2.png',
        'cancel_old.png',
        'close.png',
        # 'x.png',
        ]
        for image_path in image_path_list:
            try:
                location = pyautogui.locateOnScreen(image_path, confidence=0.75)
                if location is not None:
                    x, y, width, height = location
                    center_x = x + (width / 2)
                    center_y = y + (height / 2)
                    pyautogui.click(center_x, center_y)
                    time.sleep(0.1)
                    print(image_path)
            except Exception as e:
                print(e)

def auto_run_left_right():
    global exit_thread  # Declare exit_thread as a global variable
    while not exit_thread:
        pydirectinput.keyDown('left')
        time.sleep(10)
        pydirectinput.keyUp('left')
        time.sleep(1)
        pydirectinput.keyDown('right')
        time.sleep(10)
        pydirectinput.keyUp('right')

def auto_run_up_down():
    global exit_thread  # Declare exit_thread as a global variable
    while not exit_thread:
        for _ in range(7):
            pydirectinput.keyDown('ctrl')
            time.sleep(0.1)
            pydirectinput.keyDown('down')
            time.sleep(0.1)
            pydirectinput.keyUp('down')
            time.sleep(0.1)
            pydirectinput.keyUp('ctrl')
            time.sleep(5)
        for _ in range(4):
            pydirectinput.press('up')
            time.sleep(5)      

def auto_jump():
    global exit_thread  # Declare exit_thread as a global variable
    while not exit_thread:
        pydirectinput.press('up')
        time.sleep(0.5)

exit_flag = threading.Event()
pause_flag = threading.Event()

def main():
    print('Mode 1: left , right')
    print('Mode 2: down, up')
    mode = input('Select Mode:')
    if mode == '2':
        autorun_thread = threading.Thread(target=auto_run_up_down)
    else:
        autorun_thread = threading.Thread(target=auto_run_left_right)
        autojump_thread = threading.Thread(target=auto_jump)
    complete_thread = threading.Thread(target=find_complete_image)
    jig_thread = threading.Thread(target=find_jig_image)
    hp_mp_thread = threading.Thread(target=process_hp_mp_fill_image)
    skip_thread = threading.Thread(target=skip_any_button)

    # Start
    if mode == '2':
        autorun_thread.start()
    else:
        autorun_thread.start()
        autojump_thread.start()
    complete_thread.start()
    jig_thread.start()
    hp_mp_thread.start()
    skip_thread.start()

    try:
        # Keep the main program running
        while True:
            pass
    except KeyboardInterrupt:
        global exit_thread  # Declare exit_thread as a global variable
        exit_thread = True

    # End
    if mode == '2':
        autorun_thread.join()
    else:
        autorun_thread.join()
        autojump_thread.join()
    complete_thread.join()
    jig_thread.join()
    hp_mp_thread.join()
    skip_thread.join()

    print("Program exited")

if __name__ == "__main__":
    main()