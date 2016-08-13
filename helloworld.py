import pyautogui as pag
import cv2
import time
import webbrowser as wb
from random import randint


def random_direction(): 
    a = randint(0,4)
    if a == 0: 
        print 'Left!'
        timeoutleft = time.time() + 5
        while time.time() < timeoutleft:
            pag.keyDown('left')
    if a == 1: 
        print 'Right!'
        timeoutleft = time.time() + 5
        while time.time() < timeoutright:
            pag.keyDown('right')
    if a == 2: 
        print 'Up!'
        timeoutleft = time.time() + 5
        while time.time() < timeoutright:
            pag.keyDown('up')
    if a == 3: 
        print 'Down!'
        timeoutleft = time.time() + 5
        while time.time() < timeoutright:
            pag.keyDown('down')
    if a == 4: 
        time.sleep(5)
        

wb.open("http://slither.io/")
time.sleep(15)
pag.typewrite("Ouroboros")
pag.typewrite(["enter"])

print("To the left!")
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

timeleft = time.time() + 40
while time.time() < timeleft: 
    random_direction()
    
print("And we\'re done!")