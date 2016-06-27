import pyautogui as pag
import cv2
import time
import webbrowser as wb

wb.open("http://slither.io/")
time.sleep(15)
pag.typewrite("Ouroboros")
pag.typewrite(["enter"])
    
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