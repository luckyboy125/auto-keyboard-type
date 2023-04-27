import pyautogui
import random
import time


if __name__ == '__main__':

    time.sleep(2 + random.random() * 1.3)

    while True:
        t1 = (random.random() * 10 * (random.random() * 10))
        t1 = int(t1 % 7)
        if t1 == 0:
            pyautogui.keyDown("ALT")
            for i in range(1 + int(random.random()*4)):
                pyautogui.hotkey("TAB")
                time.sleep(0.1)

            pyautogui.keyUp("ALT")
            time.sleep(1.3 + random.random() * 1.3)

        elif t1 == 1:
            pyautogui.keyDown("CTRL")
            for i in range(1 + int(random.random()*4)):
                pyautogui.hotkey("TAB")
                time.sleep(0.1)

            pyautogui.keyUp("CTRL")
            time.sleep(1.3 + random.random() * 1.3)

        elif t1 == 2:
            pyautogui.hotkey("PAGEUP")
            time.sleep(1.3 + random.random() * 1.3)

        elif t1 == 3:
            pyautogui.hotkey("PAGEDOWN")
            time.sleep(1.3 + random.random() * 1.3)

        elif t1 == 4:
            count = int((random.random() * 80) % 10)
            for i in range(0, count):
                pyautogui.hotkey("DOWN")
                time.sleep(0.1)

            time.sleep(1.3 + random.random() * 1.3)

        elif t1 == 5:
            count = int((random.random() * 80) % 10)
            for i in range(0, count):
                pyautogui.hotkey("UP")
                time.sleep(0.1)

            time.sleep(1.3 + random.random() * 1.3)

        else :
            if t1 % 2 == 0:
                pyautogui.moveTo(420, 130, 2, pyautogui.easeInQuad)
            else:
                pyautogui.moveTo(600, 300, 2, pyautogui.easeInQuad)
            time.sleep(1.3 + random.random() * 1.3)
