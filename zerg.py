import os
import sys
import time
import random
import winsound
from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import keyboard as keyb

# Variável global para armazenar o estado de pausa
paused = False

print("zerg auto hk ON")

def autohk_and_toggle_pause(key):
    global paused

    key_new = KeyboardController()
    mouse = MouseController()

    # Alternar o estado de pausa ao pressionar 'p'
    if key.name == "p":
        paused = not paused
        if paused:
            print("Script pausado")
        else:
            print("Script retomado")
            winsound.Beep(1500, 200)
        return

    # Verificar se o script está pausado
    if paused:
        return

    # Stop macro
    if key.name == "delete":
        os._exit(0)

    # Mark hotkeys local with sound
    if key.name == "0":
        # Press F5, F6, F7, F8 between sounds
        for f_key in ["f5", "f6", "f7", "f8"]:
            keyb.press_and_release(f_key)
            winsound.Beep(1500, 200)
            time.sleep(1)

    # Auto queen
    if key.name == "=":
        for _ in range(1):
            time.sleep(0.01)
            keyb.press_and_release("space")
            time.sleep(0.05)
            keyb.press_and_release("8")
            mouse.position = (946, 500)
            keyb.press_and_release("v")
            mouse.click(Button.left, 1)

    # Auto drone
    if key.name == "4":
        keyb.press_and_release("3")
        time.sleep(0.01)
        keyb.press_and_release("s")
        time.sleep(0.02)
        keyb.press_and_release("d")

    # Auto overlord
    if key.name == "5":
        keyb.press_and_release("3")
        time.sleep(0.01)
        keyb.press_and_release("s")
        time.sleep(0.02)
        keyb.press_and_release("v")

    # Auto ling
    if key.name == "6":
        keyb.press_and_release("3")
        time.sleep(0.01)
        keyb.press_and_release("s")
        time.sleep(0.03)
        keyb.press_and_release("z")

    # Auto roach
    if key.name == "7":
        keyb.press_and_release("3")
        time.sleep(0.01)
        keyb.press_and_release("s")
        time.sleep(0.03)
        keyb.press_and_release("r")

    # Auto muta
    if key.name == "]":
        keyb.press_and_release("3")
        time.sleep(0.01)
        keyb.press_and_release("s")
        time.sleep(0.03)
        keyb.press_and_release("t")

    # Auto corruptor
    if key.name == "[":
        keyb.press_and_release("3")
        time.sleep(0.01)
        keyb.press_and_release("s")
        time.sleep(0.03)
        keyb.press_and_release("c")

    # Auto ultra
    if key.name == ";":
        keyb.press_and_release("3")
        time.sleep(0.01)
        keyb.press_and_release("s")
        for _ in range(3):
            time.sleep(0.03)
            keyb.press_and_release("u")
           

# Calls the autohk function when a key is pressed
keyb.on_press(autohk_and_toggle_pause)

# Start the keyboard listener
with keyboard.Listener() as listener:
    listener.join()