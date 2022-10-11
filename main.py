import datetime
import os

import pyautogui
import time
import cv2
import mss
import numpy as np

pyautogui.PAUSE = 0.001
current_date = "20-09-2022"
sct = mss.mss()
width = 30
height = 50
mon = {"top": 550, "left": 830, "width": width, "height": height}
current_date = datetime.datetime.strptime(current_date, "%d-%m-%Y")


def change_time():
    global year, month, day, current_date
    year = current_date.year
    month = current_date.month
    day = current_date.day
    print(current_date)
    os.system("date " + str(f"{day}-{month}-{year}"))
    os.system("time " + str(f"1:58:53.00"))
    current_date = (current_date + datetime.timedelta(days=2))


change_time()
while True:
    similarity = 0.1
    img = np.asarray(sct.grab(mon))
    prev_res = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #cv2.imshow(title, img)
    #if cv2.waitKey(25) & 0xFF == ord("q"):
    #   cv2.destroyAllWindows()
    #   quit()

    while float(similarity) < 0.95:
        time.sleep(3)
        img = np.asarray(sct.grab(mon))
        res2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        errorL2 = cv2.norm(prev_res, res2, cv2.NORM_L2)
        similarity = 1 - errorL2 / (50 * 200)
        prev_res = res2
        # print(float(similarity) < 0.95)
    for j in range(9):
        pyautogui.moveTo(800, 580, duration=0.015)
        pyautogui.mouseDown()
        time.sleep(0.1)  # or whatever you need, if even needed
        pyautogui.mouseUp()
        if j == 0:
            change_time()
        x = 890
        for i in range(3):
            pyautogui.moveTo(x, 780, duration=0.015)
            pyautogui.mouseDown()
            time.sleep(0.1)  # or whatever you need, if even needed
            pyautogui.mouseUp()
            x += 70
        x = 750
        for i in range(12):
            pyautogui.moveTo(x, 780, duration=0.015)
            pyautogui.mouseDown()
            time.sleep(0.1)  # or whatever you need, if even needed
            pyautogui.mouseUp()
            x += 70
        x = 750
        for i in range(12):
            pyautogui.moveTo(x, 700, duration=0.015)
            pyautogui.mouseDown()
            time.sleep(0.1)  # or whatever you need, if even needed
            pyautogui.mouseUp()
            x += 70
