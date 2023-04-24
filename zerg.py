# -*- coding: utf-8 -*-

from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

import keyboard as keyb
import time
import sys
import os


import winsound
import random


# Stop macro
def stop_sc2hk(key):
    if key.name == "delete":
        os._exit(0)

keyb.on_press(stop_sc2hk)


print("zerg autohk ON")
# Send glhf in 1x1
def autohk(key):
    # The currently active modifiers
    current = set()
    keynew = KeyboardController()
    mouse = MouseController()

    # mark hotkeys local with sound
    if key.name == "0":
        # press f5, f6, f7, f8 between sounds
        keyb.press_and_release("f5")
        winsound.Beep(1500, 200)
        time.sleep(1)
        keyb.press_and_release("f6")
        winsound.Beep(1500, 200)
        time.sleep(1)
        keyb.press_and_release("f7")
        winsound.Beep(1500, 200)
        time.sleep(1)
        keyb.press_and_release("f8")
        winsound.Beep(1500, 200)
        time.sleep(1)

   
    # auto queen
    if key.name == "=":
        for x in range(1):
            time.sleep(0.01)
            keyb.press_and_release("space")
            time.sleep(0.05)
            keyb.press_and_release("8")
            mouse.position = (946, 500)
            keyb.press_and_release("v")
            mouse.click(Button.left, 1)

    # auto drone
    if key.name == "4":
        keyb.press_and_release("3")
        time.sleep(0.01)
        keyb.press_and_release("s")
        time.sleep(0.02)
        keyb.press_and_release("d")

    # auto overlord
    if key.name == "5":
        keyb.press_and_release("3")
        time.sleep(0.01)
        keyb.press_and_release("s")
        time.sleep(0.02)
        keyb.press_and_release("v")

    # auto ling
    if key.name == "6":
        keyb.press_and_release("3")
        time.sleep(0.01)
        keyb.press_and_release("s")
        time.sleep(0.03)
        keyb.press_and_release("z")

    # auto roach
    if key.name == "7":
        keyb.press_and_release("3")
        time.sleep(0.01)
        keyb.press_and_release("s")
        time.sleep(0.03)
        keyb.press_and_release("r")

    # auto muta
    if key.name == "]":
        keyb.press_and_release("3")
        time.sleep(0.01)
        keyb.press_and_release("s")
        time.sleep(0.03)
        keyb.press_and_release("t")

    # auto corruptor
    if key.name == "[":
        keyb.press_and_release("3")
        time.sleep(0.01)
        keyb.press_and_release("s")
        time.sleep(0.03)
        keyb.press_and_release("c")

    # auto ultra
    if key.name == ";":
        keyb.press_and_release("3")
        time.sleep(0.01)
        keyb.press_and_release("s")
        for x in range(3):
            time.sleep(0.03)
            keyb.press_and_release("u")



# calls
keyb.on_press(autohk)
with keyboard.Listener() as listener:
    listener.join()
