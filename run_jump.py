import pydirectinput
import time
import threading
import keyboard
import pyautogui

exit_thread = False

def auto_run():
    global exit_thread  # Declare exit_thread as a global variable
    while not exit_thread:
        # times=0
        # while True:
        #     pydirectinput.press('left')
        #     if times >= 30:
        #         break
        # times=0
        # while True:
        #     pydirectinput.press('right')
        #     if times >= 30:
        #         break
        # with pyautogui.hold('right'):
        #     time.sleep(10)
        # with pyautogui.hold('left'):
        #     time.sleep(10)
        pydirectinput.keyDown('left')
        time.sleep(10)
        pydirectinput.keyUp('left')
        time.sleep(1)
        pydirectinput.keyDown('right')
        time.sleep(10)
        pydirectinput.keyUp('right')

def auto_jump():
    global exit_thread  # Declare exit_thread as a global variable
    while not exit_thread:
        pydirectinput.press('up')
        time.sleep(0.5)

exit_flag = threading.Event()
pause_flag = threading.Event()

def main():
    autorun_thread = threading.Thread(target=auto_run)
    autojump_thread = threading.Thread(target=auto_jump)

    autorun_thread.start()
    autojump_thread.start()

    try:
        # Keep the main program running
        while True:
            pass
    except KeyboardInterrupt:
        global exit_thread  # Declare exit_thread as a global variable
        exit_thread = True

    autorun_thread.join()
    autojump_thread.join()

    print("Program exited")

if __name__ == "__main__":
    main()