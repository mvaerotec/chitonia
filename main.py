"""
Coding an interactive game for Chitonia's world
"""

from src.utils import *
from src.game_end_exception import GameEndException

from src.players.chita import Chita
from src.players.chito import Chito
from src.players.gatete import Gatete
from src.players.pomtito import Pomtito
from src.players.mamichita import Mamichita

import random

__version__ = "0.1.0"

players_names = [
    "Chita",
    "Chito",
    "Gatete",
    "Pomtito",
    "Mamichita"
]

prompts = {
    "Empapelar": "A quién se va a empapelar? ",
    "Cambiar": "Cuál es el nuevo valor? ",
    "Amar": "A quién hay que dar amor? ",
    "Jugar": "Qué quieres usar para jugar? ",
    "Llamar": "A quién quieres llamar? ",
    "Amasar": "A quién va a amasar gatete? ",
    "Alimentar": "A quién vas a alimentar? "
}

prompts_arg_player = ["Amar", "Llamar", "Amasar", "Alimentar"]

def get_prompt(action):
    for k, v in prompts.items():
        if k in action:
            return v
    return ""

def print_list(items):
    for i, p in enumerate(items):
        print(f"{i+1}. {p}")

def create_players():
    players = []#{}
    for p in players_names:
        #players[p] = eval(p)()
        players.append(eval(p)())
    return players

def print_control_opts():
    print("Who do you want to control?")
    print_list(players_names)
    print(f"{len(players_names) + 1}. Show states")
    print(f"{len(players_names) + 2}. Exit")
    try:
        opt = int(input("Enter your option: "))
        if opt < 1 or opt > len(players_names)+2:
            return -1
    except ValueError:
        return -1
    return opt - 1

def get_action(actions):
    print("Select an action")
    print_list(actions)
    try:
        opt = int(input("Enter your option: "))
        if opt < 1 or opt > len(actions):
            return ""
    except ValueError:
        return ""
    return actions[opt-1]

def main():

    players = create_players()
    shuffled_players = players.copy()
    # Main loop
    rounds = 0
    while True:
        opt = print_control_opts()
        if opt == len(players_names):
            print("Player states")
            for p in players:
                print(f"{p.name} - {p.state}")
            print()
            continue
        elif opt == len(players_names) + 1:
            print(f"Saliendo - Aguantaste {rounds} rondas")
            break
        elif opt == -1:
            print("Por favor, inserta un valor válido")
            print()
            continue

        if not players[opt].action_possible():
            print("The player cannot be controlled now")
            print()
            continue

        players[opt].hello()
            
        player_actions = players[opt].available_actions

        action = get_action(list(player_actions.keys()))
        if not action:
            print("Por favor, inserta un valor válido")
            continue
        
        prompt = get_prompt(action)
        if prompt:
            arg = input(prompt)
            if action.split(" ")[0] in prompts_arg_player:
                if arg.capitalize() in players_names:
                    arg = players[players_names.index(arg.capitalize())]
                else:
                    arg = None
            elif "Cambiar" in action:
                arg = float(arg)
            else:
                # Arg has to be passed as a string as is, unprocessed
                pass
        else:
            if "Arreglar" in action:
                arg = players[players_names.index("Chito")]
            else:
                arg = None
        try:
            if arg:
                player_actions[action](arg)
            else:
                player_actions[action]()
        except RuntimeError as e:
            print("There was an error:")
            print(e)
        except GameEndException as e:
            print("The game ended: " + str(e))
            print(f"You survived {rounds} rounds")
            break
        try:
            random.shuffle(shuffled_players)
            action_trig = False
            for p in shuffled_players:
                trig = p.update(action_trig)
                action_trig = action_trig or trig
                print(f"{p.name} - {p.state}")
        except GameEndException as e:
            print("The game ended: " + str(e))
            print(f"You survived {rounds} rounds")
            break
        print(flush=True)
        rounds += 1


if __name__ == "__main__":
    main()

