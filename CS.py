import pyautogui
im1 = pyautogui.screenshot()
im2 = pyautogui.screenshot('my_screenshot.png')

import cv2
import numpy as np

img_rgb = cv2.imread('my_screenshot.png')
template = cv2.imread('nenable.png')
w, h = template.shape[:-1]

res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
threshold = .8
loc = np.where(res >= threshold)
if len(loc[0]) == 0:
    print("No matches found.")
for pt in zip(*loc[::-1]):  # Switch columns and rows
    cv2.rectangle(img_rgb, pt, (pt[0] + h, pt[1] + w), (0, 0, 255), 2)

cv2.imwrite('result.png', img_rgb)