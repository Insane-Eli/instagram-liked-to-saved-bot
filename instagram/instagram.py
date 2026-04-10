import time
import pyautogui

def wait():
    pyautogui.sleep(.3)

def wait_for_reel():
    while True:
        try:
            heart_button = pyautogui.locateCenterOnScreen('heart.png', confidence=.9)
            return heart_button
        except pyautogui.ImageNotFoundException:
            time.sleep(.1)
            pass


def wait_for_reload():
    while True:
        try:
            print(pyautogui.locateOnScreen('newest-to-oldest.png', confidence=.9))
            time.sleep(.1)
            return
        except pyautogui.ImageNotFoundException:
            time.sleep(.1)
            pass

# to-do list
# make the wait functions optimal (image recognition)
# ensure all video formats, displays (light mode), OS's? are supported
# assess which prerequisite packages are required
# write a goated README.md
# add option to not have reels unlikedq
# add an option to keep friends reels liked
# explore ways to make the bot overall faster
#  - more tabs running

# pyautogui.displayMousePosition()

for i in range(2000):

    wait_for_reload()
    pyautogui.leftClick(900, 350)

    heart_button = wait_for_reel()
    save_button = pyautogui.Point(heart_button.x + 280, heart_button.y)
    liked_playlist = pyautogui.Point(save_button.x, save_button.y - 240)

    pyautogui.moveTo(save_button, duration=.1)
    time.sleep(1)
    wait()

    pyautogui.moveTo(liked_playlist, duration=.1)
    pyautogui.leftClick()
    wait()

    pyautogui.leftClick(heart_button)
    wait()

    pyautogui.hotkey('alt', 'left')
    wait()
