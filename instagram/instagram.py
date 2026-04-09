import time
import pyautogui
import os

# pyautogui.displayMousePosition()

def wait():
    pyautogui.sleep(.3)

def wait_for_reel():
    pyautogui.sleep(10) # placeholder for real code

def wait_for_reload():
    pyautogui.sleep(10) # placeholder for real code

# to-do list
# make the wait functions optimal (image recognition)
# ensure all video formats, displays (light mode), OS's? are supported
# assess which prerequisite packages are required
# write a goated README.md
# add option to not have reels unliked
# add an option to keep friends reels liked
# explore ways to make the bot overall faster
#  - more tabs running

for i in range(2000):

    wait_for_reload()

    # (900, 350) - new reel
    pyautogui.leftClick(900, 350)
    wait_for_reel()

    heart_button = pyautogui.locateCenterOnScreen('heart.png', confidence=.9)
    print('heart button: ', heart_button)
    save_button = pyautogui.Point(heart_button.x + 280, heart_button.y)
    print('save button: ', save_button)
    liked_playlist = pyautogui.Point(save_button.x, save_button.y - 240)
    print('liked playlist: ', liked_playlist)

    pyautogui.moveTo(save_button, duration=.1)
    pyautogui.sleep(1)

    pyautogui.moveTo(liked_playlist, duration=.1)
    pyautogui.leftClick()
    wait()

    pyautogui.leftClick(heart_button)
    pyautogui.sleep(1.5)

    pyautogui.hotkey('alt', 'left')

    wait()
