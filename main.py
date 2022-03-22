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

__version__ = "0.1.0"

players_names = [
    "Chita",
    "Chito",
    "Gatete",
    "Pomtito",
    "Mamichita"
]

prompts = {
    "Empapelar": "A quién se va a empapelar?",
    "Cambiar": "Cuál es el nuevo valor?",
    "Amar": "A quién hay que dar amor?",
    "Jugar": "Qué quieres usar para jugar?"
}

def get_prompt(action):
    for k, v in prompts:
        if k in action:
            return v
    return ""

def print_list(items)
    for i, p in enumerate(items):
        print(f"{i+1}. {p}")

def create_players():
    players = {}
    for p in players_names:
        players[p] = eval(p)()
    return players

def print_control_opts():
    print("Who do you want to control?")
    print_list(players_names)
    print(f"{len(players_names)}. Exit")
    return int(input("Enter your option: ")) - 1

def get_action(actions):
    print("Select an action")
    print_list(actions)
    return actions[int(input("Enter your option: ")) - 1]

def main():

    players = create_players()
    # Main loop
    while True:
        opt = print_control_opts()
        if opt == len(players_names):
            break

        if not players[opt].action_possible():
            print("The player cannot be controlled now")
            continue

        players[opt].hello()
            
        player_actions = players[opt].available_actions

        try:
            action = get_action(list(player_actions.keys()))
        except IndexError:
            break
        
        arg = input(get_prompt(action))
        # TODO if method == amar - then arg should not be string, but player
        if arg.lower() == "amar":
            arg = players[players_names.index(arg)]
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
            break
        try:
            for p in players:
                p.update()
        except GameEndException as e:
            print("The game ended: " + str(e))
            break
        print()


if __name__ == "__main__":
    main()

