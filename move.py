import time
import pydirectinput

while True:
    pydirectinput.keyDown('right')
    time.sleep(0.001)
    pydirectinput.keyUp('right')
    time.sleep(1)