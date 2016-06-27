import pyautogui as pag
import cv2
import time

time.sleep(2)
pag.click(635, 550)
time.sleep(1)
pag.click(635, 550)
time.sleep(2)
    
timeoutleft = time.time() + 5
while time.time() < timeoutleft:
    pag.keyDown('left')
    print time.time()

pag.keyUp('left')
print("Going straight!")

timeoutright = time.time() + 5
print time.time()
print timeoutright

print("Going to the right!")
while time.time() < timeoutright:
    pag.keyDown('right')
    print time.time()

pag.keyUp('right')
print("And we\'re done!")