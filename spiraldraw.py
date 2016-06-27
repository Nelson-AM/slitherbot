import pyautogui, time

pyautogui.click()

distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration = 0.2)
    distance = distance - 10
    pyautogui.dragRel(0, distance, duration = 0.2)
    pyautogui.dragRel(-distance, 0, duration = 0.2)
    distance = distance - 10
    pyautogui.dragRel(0, -distance, duration = 0.2)