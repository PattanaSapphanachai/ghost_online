import cv2
import pytesseract
import PIL.Image
from pytesseract import Output
import pyautogui
import math
import pydirectinput
import time
from PIL import Image

config = r'--psm 11 --oem 3'


while True:
    screenshot = pyautogui.screenshot()
    image = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())
    image.save('screenshot.png')
    img = cv2.imread("screenshot.png", cv2.IMREAD_GRAYSCALE)

    # img = cv2.imread("./pic/ss7.png", cv2.IMREAD_GRAYSCALE)

    img2 = cv2.imread("./pic/player.png", cv2.IMREAD_GRAYSCALE)

    # h, w, _ = img.shape
    h, w = img.shape[:2]

    result = cv2.matchTemplate(img, img2, cv2.TM_CCOEFF_NORMED)
    _, __, min_loc, max_loc = cv2.minMaxLoc(result)
    player_x = max_loc[0]
    player_y = max_loc[1]

    data = pytesseract.image_to_data(img, config=config, output_type=Output.DICT)
    amount_boxes = len(data['text'])
    text_lsit = ['Trans', 'Shadow', 'Slime']

    for i in range(amount_boxes):
        if float(data['conf'][i]) > 70 and data['text'][i] in text_lsit:
        # if float(data['conf'][i]) > 0:
            (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            eDistance = math.dist([player_x, player_y], [x, y])
            if eDistance < 400 and abs(y - player_y) < 100:
                print('attack')
                # img = cv2.rectangle(img, (x, y), (x+width, y+height), (0,255,0), 2)
                # img = cv2.putText(img, data['text'][i], (x, y+height+20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,200,0), 1, cv2.LINE_AA)

                pydirectinput.press('z')
                time.sleep(0.3)
                pydirectinput.press('x')
                time.sleep(0.3)
                pydirectinput.press('c')
    # result = cv2.matchTemplate(img, img2, cv2.TM_CCOEFF_NORMED)
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # player_x = max_loc[0]
    # player_y = max_loc[1]
    # img = cv2.rectangle(img, (max_loc[0], max_loc[1]), (max_loc[0]+80, max_loc[1]+20), (0, 255, 0), 2)

    # cv2.imshow("img", img)
    # cv2.waitKey(0)