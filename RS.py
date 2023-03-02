import os
import pyautogui
import time
import sys
import keyboard
import socket

def main():
    i = 0
    while i < 100:
        # exit if pressed
        if(keyboard.is_pressed('esc')):
            print(i + 100)
            sys.exit(0)
        print(i)
        i += 1
        time.sleep(0.05)
        #play_sound("aud.mp3")
    sys.exit(0)


def play_sound(filename):
    os.system(f"start {filename}")
    time.sleep(0.2)
    # press Win key and hold it
    pyautogui.keyDown('win')

    # wait for 1 second
    time.sleep(0.01)

    # press Down Arrow key twice
    pyautogui.press('down')

    # release Win key
    pyautogui.keyUp('win')

    time.sleep(3)



if __name__ == "__main__":
    main()
