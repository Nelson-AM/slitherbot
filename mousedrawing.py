#! python 2.7
# mousedrawing.py -- Displays the mouse cursor and performs mouse drags to draw something in photoshop.

import pyautogui
import cv2

try:
    
    pyautogui.click(25, 7)
    cv2.waitKey(50)
    pyautogui.click(32, 37)
    
    while True:
        # TODO: get and print the mouse coordinates.
        
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = "X: " + str(x).rjust(4) + "Y: " + str(y).rjust(4)
        
        print(positionStr)
        print("\b" * len(positionStr))
        
except KeyboardInterrupt:
    print("\nDone")

