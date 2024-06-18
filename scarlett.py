import os
import time
import winsound
from pynput import keyboard
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController
import keyboard as keyb
import yaml
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Variável global para armazenar o estado de pausa
paused = False

logging.info("Zerg auto hotkey ON")

# Carregar arquivo de configuração
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Dicionário para armazenar ações para cada perfil
profiles = {}
for profile, actions in config.items():
    profiles[profile] = {}
    for action_name, action_steps in actions.items():
        profiles[profile][action_name] = action_steps

# Funções de ação específicas
def auto_queen():
    logging.info("Executing auto_queen actions")
    for step in profiles['zerg']['auto_queen']:
        exec(step)

def auto_drone():
    logging.info("Executing auto_drone actions")
    for step in profiles['zerg']['auto_drone']:
        exec(step)

def auto_overlord():
    logging.info("Executing auto_overlord actions")
    for step in profiles['zerg']['auto_overlord']:
        exec(step)

def auto_ling():
    logging.info("Executing auto_ling actions")
    for step in profiles['zerg']['auto_ling']:
        exec(step)

def auto_roach():
    logging.info("Executing auto_roach actions")
    for step in profiles['zerg']['auto_roach']:
        exec(step)

def auto_muta():
    logging.info("Executing auto_muta actions")
    for step in profiles['zerg']['auto_muta']:
        exec(step)

def auto_corruptor():
    logging.info("Executing auto_corruptor actions")
    for step in profiles['zerg']['auto_corruptor']:
        exec(step)

def auto_ultra():
    logging.info("Executing auto_ultra actions")
    for step in profiles['zerg']['auto_ultra']:
        exec(step)

# Dicionário para mapeamento de teclas para funções
key_to_action = {
    '`': auto_queen,
    '4': auto_drone,
    '5': auto_overlord,
    '6': auto_ling,
    '7': auto_roach,
    ']': auto_muta,
    '[': auto_corruptor,
    ';': auto_ultra
}

def autohk_and_toggle_pause(event):
    global paused

    key_new = KeyboardController()
    mouse = MouseController()

    # Alternar o estado de pausa ao pressionar 'p'
    if event.name == "p":
        paused = not paused
        if paused:
            logging.info("Script pausado")
        else:
            logging.info("Script retomado")
            winsound.Beep(1500, 200)
        return

    # Verificar se o script está pausado
    if paused:
        return

    # Stop macro
    if event.name == "delete":
        logging.info("Script terminado")
        os._exit(0)

    # Chamar a ação correspondente ao perfil
    if event.name in key_to_action:
        try:
            key_to_action[event.name]()
        except Exception as e:
            logging.error(f"Erro ao executar a ação: {e}")

# Chama a função autohk ao pressionar uma tecla
keyb.on_press(autohk_and_toggle_pause)

# Iniciar o listener do teclado
with keyboard.Listener() as listener:
    listener.join()
