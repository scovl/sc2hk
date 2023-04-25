import os
import sys
import time
import random
import winsound
from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import keyboard as keyb
import yaml

# Variável global para armazenar o estado de pausa
paused = False

print("auto hk ON")

# Load config file
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Create dictionary to store actions for each profile
profiles = {}
for profile, actions in config.items():
    profile_actions = {}
    for action_name, action_steps in actions.items():
        profile_actions[action_name] = action_steps
    profiles[profile] = profile_actions

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
            time.sleep(0.8)

    # Call the action for the corresponding profile
    elif key.name == "=":
        action_steps = profiles['zerg']['auto_queen']
        for step in action_steps:
            exec(step)
    elif key.name == "4":
        action_steps = profiles['zerg']['auto_drone']
        for step in action_steps:
            exec(step)
    elif key.name == "5":
        action_steps = profiles['zerg']['auto_overlord']
        for step in action_steps:
            exec(step)
    elif key.name == "6":
        action_steps = profiles['zerg']['auto_ling']
        for step in action_steps:
            eval(step)
    elif key.name == "7":
        action_steps = profiles['zerg']['auto_roach']
        for step in action_steps:
            eval(step)
    elif key.name == "]":
        action_steps = profiles['zerg']['auto_muta']
        for step in action_steps:
            eval(step)
    elif key.name == "[":
        action_steps = profiles['zerg']['auto_corruptor']
        for step in action_steps:
            eval(step)
    elif key.name == ";":
        action_steps = profiles['zerg']['auto_ultra']
        for step in action_steps:
            eval(step)
            
# Calls the autohk function when a key is pressed
keyb.on_press(autohk_and_toggle_pause)

# Start the keyboard listener
with keyboard.Listener() as listener:
    listener.join()