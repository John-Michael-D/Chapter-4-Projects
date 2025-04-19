import random
import zlib
import base64
import json

total_money = 0
experience_points = 0
fishing_count = 0
fisherman_level = 0
player_equipment = []
employees = []

print(r"""
················································································
: ____      ____  ________  _____       ______    ___   ____    ____  ________ :
:|_  _|    |_  _||_   __  ||_   _|    .' ___  | .'   `.|_   \  /   _||_   __  |:
:  \ \  /\  / /    | |_ \_|  | |     / .'   \_|/  .-.  \ |   \/   |    | |_ \_|:
:   \ \/  \/ /     |  _| _   | |   _ | |       | |   | | | |\  /| |    |  _| _ :
:    \  /\  /     _| |__/ | _| |__/ |\ `.___.'\\  `-'  /_| |_\/_| |_  _| |__/ |:
:     \/  \/     |________||________| `.____ .' `.___.'|_____||_____||________|:
: _________    ___     _________  ____  ____  ________                         :
:|  _   _  | .'   `.  |  _   _  ||_   ||   _||_   __  |                        :
:|_/ | | \_|/  .-.  \ |_/ | | \_|  | |__| |    | |_ \_|                        :
:    | |    | |   | |     | |      |  __  |    |  _| _                         :
:   _| |_   \  `-'  /    _| |_    _| |  | |_  _| |__/ |                        :
:  |_____|   `.___.'    |_____|  |____||____||________|                        :
: ________  _____   ______   ____  ____  _____  ____  _____   ______           :
:|_   __  ||_   _|.' ____ \ |_   ||   _||_   _||_   \|_   _|.' ___  |          :
:  | |_ \_|  | |  | (___ \_|  | |__| |    | |    |   \ | | / .'   \_|          :
:  |  _|     | |   _.____`.   |  __  |    | |    | |\ \| | | |   ____          :
: _| |_     _| |_ | \____) | _| |  | |_  _| |_  _| |_\   |_\ `.___]  |         :
:|_____|   |_____| \______.'|____||____||_____||_____|\____|`._____.'          :
:   ______       _       ____    ____  ________                                :
: .' ___  |     / \     |_   \  /   _||_   __  |                               :
:/ .'   \_|    / _ \      |   \/   |    | |_ \_|                               :
:| |   ____   / ___ \     | |\  /| |    |  _| _                                :
:\ `.___]  |_/ /   \ \_  _| |_\/_| |_  _| |__/ |                               :
: `._____.'|____| |____||_____||_____||________|                               :
················································································

In this game, you play as a fisherman trying to gain riches. The rules are simple:

1. Catch fish to earn money and experience. 
2. Earn enough money and experience to move on to bigger and better fishing spots.
3. Increase your Fisherman Level and become the greatest fisherman in history!
4. Reach the final level of the game: WHALE CENTRAL.
5. Catch MOBY DICK!!!!!!!!
""")

def save_game(experience_points, fishing_count, fisherman_level, player_equipment, employees, total_money):
    game_data = {
        'exp': experience_points,
        'count': fishing_count,
        'level': fisherman_level,
        'equipment': player_equipment,
        'employees': employees,
        'money': total_money,
    }

    json_data = json.dumps(game_data, separators=(',', ':'))

    compressed = zlib.compress(json_data.encode('utf-8'))

    save_hash = base64.urlsafe_b64encode(compressed).decode('ascii')

    return save_hash

def load_game(save_hash):
    try:
        padding = len(save_hash) % 4
        if padding:
            save_hash += '=' * (4 - padding)

        compressed = base64.urlsafe_b64decode(save_hash)
        json_data = zlib.decompress(compressed).decode('utf-8')
        game_data = json.loads(json_data)

        if not all(key in game_data for key in {'exp', 'count', 'level', 'equipment', 'employees', 'money'}):
            return None

        return (
            game_data['exp'],
            game_data['count'],
            game_data['level'],
            game_data['equipment'],
            game_data['employees'],
            game_data['money']
        )
    except (base64.binascii.Error, zlib.error, json.JSONDecodeError, KeyError):
        return None

def display_save_menu():
    global experience_points, fishing_count, fisherman_level, player_equipment, employees, total_money

    while True:
        print("\n=== Save/Load Menu ===")
        print("1. Save current game")
        print("2. Load saved game")
        print("3. Return to main options menu")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            save_hash = save_game(experience_points, fishing_count, fisherman_level, player_equipment, employees,
                                  total_money)
            print("\n=== Game Saved ===")
            print("Copy the following code to save your progress:")
            print(f"\n{save_hash}\n")
            print("When you want to continue where you left off after you exit the game, use the 'Load' option and paste this code.")
            input("Press Enter to return to options...")
            return
        elif choice == '2':
            save_hash = input("\nPaste your save code: ").strip()
            loaded_data = load_game(save_hash)

            if loaded_data is None:
                print("Invalid save code. Please try again.")
                input("Press Enter to continue...")
            else:
                experience_points, fishing_count, fisherman_level, player_equipment, employees, total_money = loaded_data
                print("Game loaded successfully!")
                return
        elif choice == '3':
            return
        else:
            print("Invalid choice. Please try again.")

def fishing_art(arg):

    if arg == 1:
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣶⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡿⠿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢉⣡⣤⣶⣶⣶⣶⣶⣶⣶⣶⣤⠀⠀⢸⣇⠀⠀
        ⠀⠙⣿⣷⣦⡀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⠋⠉⣿⠟⠁⠀⠀⢸⡟⠀⠀
        ⠀⠀⢸⣿⡿⠋⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠖⠁⠀⠀⣷⡄⢸⡇⠀⠀
        ⠀⠀⠀⣿⠁⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⢿⣀⣸⡇⠀⠀
        ⠀⠀⠀⣿⣷⣤⣈⠛⠻⢿⣿⡿⢁⣼⣿⣿⡿⠛⣿⣿⣿⣦⣄⡀⠈⠉⠉⠁⠀⠀
        ⠀⠀⢀⣿⡿⠟⠁⠀⠀⠀⠀⠀⠛⠉⠉⠠⠤⠾⠿⠿⠿⠿⠟⠛⠋⠁⠀⠀⠀⠀
        ⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """)
    if arg == 2:
        print("""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⢹⣛⣷⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⠴⣒⡮⠭⠉⠉⢐⠊⢋⡉⠉⠉⢒⣒⠬⢄⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡴⣫⠤⠖⠒⠈⠉⠉⠀⠀⠀⠀⠈⠒⠂⠀⣠⠉⣑⠚⠵⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡰⡻⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠘⠳⠀⠒⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣼⣿⡄⠀⠀
⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠀⣤⣄⠀⠀⠁⠉⠀⠀⠀
⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡀⠀⠀⠀⠀⢰⢷⣿⣷⡄⠀⢀⣀⣀⣀
⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣄⠀⠀⠀⢸⣻⠚⠙⣧⢾⢿⣯⣿⡿
⠀⡏⠀⢀⡀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠣⡀⠀⠀⠳⢤⡽⢏⠋⠀⠈⣽⠇
⢀⣇⣀⣈⣓⣋⣁⣀⣙⣒⣚⡁⠀⠀⢀⣀⣀⠀⠀⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣓⢦⣤⣾⣧⡟⠦⠶⠞⠋⠀
⠈⡏⠇⠀⡇⠀⡇⠀⡇⠀⡇⠉⡏⠉⡟⠛⡫⠤⣀⣀⣉⡀⠀⠀⠀⢀⣴⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢹⣿⡿⠀⠀⠀⠀⠀⠀
⠀⣇⢸⠀⡇⠀⡇⠀⡇⠀⡁⠀⡇⠀⡇⠀⡇⠀⢸⢹⠀⡧⡀⠀⠀⢸⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⣶⣾⡟⠁⠀⠀⠀⠀⠀⠀
⠀⠘⢾⣆⢸⠀⢣⠀⡇⠀⡇⠀⡇⠀⡇⠀⢱⠀⢸⠈⠚⡇⡌⢦⡀⠈⢿⣿⣿⣿⣿⣿⣦⡀⠀⢠⣶⣾⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠙⣦⣣⡘⣆⠸⡀⢳⡀⢱⠀⢱⠀⠸⡀⠘⡄⠀⣷⠗⢰⠈⠓⡾⢿⣿⣿⣿⣿⣿⣿⣦⣤⡿⠋⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠹⠛⠛⠛⠓⠿⠦⠷⠦⢷⣤⣷⣄⣳⣄⣱⣄⣘⣦⣀⣳⣤⡽⠦⠴⠾⠟⠛⣿⢿⣿⠿⠿⠿⠿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)

    if arg == 3:
        print("""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣀⣠⠤⢾⣞⣿⣿⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠔⠚⠉⢁⣤⣶⣾⣿⣟⠻⢇⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠒⠋⠉⠀⠀⠀⣠⣶⣿⣿⡿⢋⡴⠟⣾⡾⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠚⠁⠀⠀⠀⠀⣠⣴⣾⣿⢟⡿⢋⡴⠛⣠⢾⠏⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠚⠁⠀⠀⠀⠀⢠⣾⣿⠿⡟⢋⠔⢁⣴⠟⢁⡴⣱⠋⠀⠀⠀
⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⣤⢶⣶⣾⡟⢠⠋⢠⠏⡰⢻⠋⡠⢋⡞⠁⠀⠀⠀⠀
⡏⢧⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⢀⣰⣶⣿⣷⣇⣾⣿⢿⣤⠃⢠⢏⡞⣡⢃⣞⣡⠋⠀⠀⠀⠀⠀⠀
⡇⠈⠈⠳⢦⡀⠀⠀⢀⣤⣠⣴⠗⠛⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⣴⠋⠁⣠⣿⣿⣿⢟⣽⡿⢃⡴⢃⠞⣰⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⢻⡄⠀⠀⠸⢿⣿⡶⣾⡍⠉⠁⠀⠀⣠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⣸⠁⠀⢠⣾⣿⣯⣕⣿⣯⠖⢉⡴⢋⣼⣽⣵⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⢿⣆⡀⠀⢺⣿⡇⠻⣿⣄⣀⣤⡾⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠎⠀⠀⠀⢠⣼⡇⠀⠀⠀⠻⣯⢛⡵⠚⢁⡴⠊⣠⣾⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⠿⣶⣾⣿⣇⠀⢿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⠁⠀⠀⠀⢠⣿⣿⡇⠀⠀⠀⢡⣿⠏⣀⠔⢋⡠⣪⣿⣿⣿⠟⠻⠇⡼⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⢻⡄⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠇⠀⠀⣀⣰⣿⣿⣿⠀⠀⠀⠀⣆⣿⡏⢁⣴⣯⡾⠋⣿⣿⡁⠀⠀⠀⠳⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⠀⠀⠙⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⡿⠋⠀⢀⣠⣶⣿⣯⡿⣿⡇⠀⠀⠀⠠⡽⣷⢞⣽⡿⠋⠀⠀⠘⣿⠿⠂⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⢲⣾⣿⠓⠲⢤⣤⣤⠤⠔⣲⠟⠛⠋⠁⢀⣴⣴⡿⣿⣽⣿⣿⣿⣿⡁⠀⠀⠀⢰⣻⡿⠟⠁⠀⠀⠀⠀⠈⣧⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⣄⡙⠁⠀⠐⠿⠿⠀⠀⠀⠀⠀⠐⠿⠿⢾⣻⣴⣿⣿⡿⠿⠻⣿⡿⠀⠀⠀⠀⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠘⣇⠀⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣶⣾⣿⣶⣶⣦⣤⣤⣴⣖⣶⣾⡿⠿⠛⢉⣀⣤⣴⣶⣿⡇⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⢿⣻⣿⣿⣿⠛⣭⣴⣒⣒⣚⣛⣯⡭⠽⠛⠋⣿⡇⠀⠀⢠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀  ⠀⠀⠀⢻⣷⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⣀⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠸⣿⣀⣮⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢿⣿⣻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)

def neighborhood_pond():
    global total_money, experience_points, fishing_count, fisherman_level

    while True:
        print("""
··············································
:YOU ARE NOW FISHING IN THE NEIGHBORHOOD POND:
··············································
""")

        dice_roll = random.randint(1,9)
        fish = {1:"Grass Carp", 2:"Peruvian Anchoveta", 3:"Silver Carp", 4:"Common Carp", 5:"Alaska Pollock", 6: "Nile Tilapia"}
        fish_reward = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}

        if dice_roll == 1 or dice_roll <= 6:
            fishing_art(1)
            fishing_count += 1
            fisherman_level += 1
            total_money += fish_reward[dice_roll]
            experience_points += 1
            print(f"\nYou caught a(n) {fish[dice_roll]}, which is worth ${fish_reward[dice_roll]}!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll >= 7:
            fishing_count += 1
            print(f"\nYou didn't catch anything this time! Try again!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()

        while True:
            try:
                response = input(f"\nYou have fished for {fishing_count} times. Would you like to fish in the neighborhood pond again? Yes or no? (Y/N)").strip().lower()
                if response == "yes" or response == "y":
                    break
                elif response == "no" or response == "n":
                    options()
            except ValueError:
                print(f"Invalid entry! Please enter yes or no.")

def park_river():
    global total_money, experience_points, fishing_count, fisherman_level

    while True:
        print("""
·······································
:YOU ARE NOW FISHING IN THE PARK RIVER:
·······································
    """)

        dice_roll = random.randint(1,9)
        fish = {1:"Whiteleg Shrimp", 2:"Bighead Carp", 3:"Skipjack Tuna", 4:"Catla", 5:"Bluefin Tuna", 6: "Atlantic Cod"}
        fish_reward = {1: 7, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12}

        if dice_roll == 1 or dice_roll <= 6:
            fishing_art(1)
            fishing_count += 1
            fisherman_level += 1
            total_money += fish_reward[dice_roll]
            experience_points += 2
            print(f"\nYou caught a(n) {fish[dice_roll]}, which is worth ${fish_reward[dice_roll]}!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll >= 7:
            fishing_count += 1
            print(f"\nYou didn't catch anything this time! Try again!")
            print(f"You currently have ${total_money} and {experience_points} XP.")

        while True:
            try:
                response = input(f"\nYou have fished for {fishing_count} times. Would you like to fish in the park river again? Yes or no? (Y/N)").strip().lower()
                if response == "yes" or response == "y":
                    break
                elif response == "no" or response == "n":
                    options()
            except ValueError:
                print(f"Invalid entry! Please enter yes or no.")

def county_lake():
    global total_money, experience_points, fishing_count, fisherman_level

    while True:
        print("""
········································
:YOU ARE NOW FISHING IN THE COUNTY LAKE:
········································
    """)

        dice_roll = random.randint(1,9)
        fish = {1:"Yellowfin Tuna", 2:"Sockeye Salmon", 3:"Pink Salmon", 4:"Atlantic Mackerel", 5:"European Sardine", 6: "Haddock"}
        fish_reward = {1: 13, 2: 14, 3: 15, 4: 16, 5: 17, 6: 18}

        if dice_roll == 1 or dice_roll <= 6:
            fishing_art(1)
            fishing_count += 1
            fisherman_level += 1
            total_money += fish_reward[dice_roll]
            experience_points += 3
            print(f"\nYou caught a(n) {fish[dice_roll]}, which is worth ${fish_reward[dice_roll]}!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll >= 7:
            fishing_count += 1
            print(f"\nYou didn't catch anything this time! Try again!")
            print(f"You currently have ${total_money} and {experience_points} XP.")

        while True:
            try:
                response = input(f"\nYou have fished for {fishing_count} times. Would you like to fish in the park river again? Yes or no? (Y/N)").strip().lower()
                if response == "yes" or response == "y":
                    break
                elif response == "no" or response == "n":
                    options()
            except ValueError:
                print(f"Invalid entry! Please enter yes or no.")

def beach_marina():
    global total_money, experience_points, fishing_count, fisherman_level

    while True:
        print("""
·········································
:YOU ARE NOW FISHING IN THE BEACH MARINA:
·········································
        """)

        dice_roll = random.randint(1, 9)
        fish = {1: "Rainbow Trout", 2: "Channel Catfish", 3: "Blue Catfish", 4: "Pacific Halibut", 5: "Atlantic Herring", 6: "Mahi-Mahi"}
        fish_reward = {1: 19, 2: 20, 3: 21, 4: 22, 5: 23, 6: 24}

        if dice_roll == 1 or dice_roll <= 6:
            fishing_art(1)
            fishing_count += 1
            fisherman_level += 1
            total_money += fish_reward[dice_roll]
            experience_points += 4
            print(f"\nYou caught a(n) {fish[dice_roll]}, which is worth ${fish_reward[dice_roll]}!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll >= 7:
            fishing_count += 1
            print(f"\nYou didn't catch anything this time! Try again!")
            print(f"You currently have ${total_money} and {experience_points} XP.")

        while True:
            try:
                response = input(
                    f"\nYou have fished for {fishing_count} times. Would you like to fish in the park river again? Yes or no? (Y/N)").strip().lower()
                if response == "yes" or response == "y":
                    break
                elif response == "no" or response == "n":
                    options()
            except ValueError:
                print(f"Invalid entry! Please enter yes or no.")

def atlantic_ocean():
    global total_money, experience_points, fishing_count, fisherman_level

    while True:
        print("""
···········································
:YOU ARE NOW FISHING IN THE ATLANTIC OCEAN:
···········································
            """)

        dice_roll = random.randint(1, 9)
        fish = {1: "Largemouth Bass", 2: "Sea Bass", 3: "Red Snapper", 4: "Yellowtail Snapper", 5: "Red Grouper", 6: "Goliath Grouper"}
        fish_reward = {1: 25, 2: 26, 3: 27, 4: 28, 5: 29, 6: 30}

        if dice_roll == 1 or dice_roll <= 6:
            fishing_art(1)
            fishing_count += 1
            fisherman_level += 1
            total_money += fish_reward[dice_roll]
            experience_points += 5
            print(f"\nYou caught a(n) {fish[dice_roll]}, which is worth ${fish_reward[dice_roll]}!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll >= 7:
            fishing_count += 1
            print(f"\nYou didn't catch anything this time! Try again!")
            print(f"You currently have ${total_money} and {experience_points} XP.")

        while True:
            try:
                response = input(
                    f"\nYou have fished for {fishing_count} times. Would you like to fish in the park river again? Yes or no? (Y/N)").strip().lower()
                if response == "yes" or response == "y":
                    break
                elif response == "no" or response == "n":
                    options()
            except ValueError:
                print(f"Invalid entry! Please enter yes or no.")

def pacific_ocean():
    global total_money, experience_points, fishing_count, fisherman_level

    while True:
        print("""
··········································
:YOU ARE NOW FISHING IN THE PACIFIC OCEAN:
··········································
                """)

        dice_roll = random.randint(1, 9)
        fish = {1: "Flounder", 2: "Swordfish", 3: "Barramundi", 4: "Arctic Char", 5: "White Sturgeon", 6: "Zander"}
        fish_reward = {1: 31, 2: 32, 3: 33, 4: 34, 5: 35, 6: 36}

        if dice_roll == 1 or dice_roll <= 6:
            fishing_art(1)
            fishing_count += 1
            fisherman_level += 1
            total_money += fish_reward[dice_roll]
            experience_points += 6
            print(f"\nYou caught a(n) {fish[dice_roll]}, which is worth ${fish_reward[dice_roll]}!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll >= 7:
            fishing_count += 1
            print(f"\nYou didn't catch anything this time! Try again!")
            print(f"You currently have ${total_money} and {experience_points} XP.")

        while True:
            try:
                response = input(
                    f"\nYou have fished for {fishing_count} times. Would you like to fish in the park river again? Yes or no? (Y/N)").strip().lower()
                if response == "yes" or response == "y":
                    break
                elif response == "no" or response == "n":
                    options()
            except ValueError:
                print(f"Invalid entry! Please enter yes or no.")

def whale_central():
    global total_money, experience_points, fishing_count, fisherman_level

    while True:
        print("""
······································
:YOU ARE NOW FISHING IN WHALE CENTRAL:
······································
                    """)

        dice_roll = random.randint(1, 9)
        moby_dice_roll = random.randint(10,100)
        fish = {1: "Sperm Whale", 2: "North Atlantic Right Whale", 3: "Bowhead Whale", 4: "Humpback Whale", 5: "Blue Whale", 6: "Fin Whale"}
        fish_reward = {1: 1000, 2: 1500, 3: 2000, 4: 2500, 5: 3000, 6: 3500}

        if moby_dice_roll >= 95 and moby_dice_roll <= 100:
            fishing_art(3)
            fishing_count += 1
            fisherman_level += 1000
            total_money += 1000000
            experience_points += 1000000
            print("""
____    ____  ______    __    __   ______    ____  _______        
\   \  /   / /  __  \  |  |  |  | (_ )   \  /   / |   ____|       
 \   \/   / |  |  |  | |  |  |  |  |/ \   \/   /  |  |__          
  \_    _/  |  |  |  | |  |  |  |      \      /   |   __|         
    |  |    |  `--'  | |  `--'  |       \    /    |  |____        
    |__|     \______/   \______/         \__/     |_______|       
                                                                  
  ______     ___      __    __    _______  __    __  .___________.
 /      |   /   \    |  |  |  |  /  _____||  |  |  | |           |
|  ,----'  /  ^  \   |  |  |  | |  |  __  |  |__|  | `---|  |----`
|  |      /  /_\  \  |  |  |  | |  | |_ | |   __   |     |  |     
|  `----./  _____  \ |  `--'  | |  |__| | |  |  |  |     |  |     
 \______/__/     \__\ \______/   \______| |__|  |__|     |__|     
                                                                  
.___  ___.   ______   .______   ____    ____                      
|   \/   |  /  __  \  |   _  \  \   \  /   /                      
|  \  /  | |  |  |  | |  |_)  |  \   \/   /                       
|  |\/|  | |  |  |  | |   _  <    \_    _/                        
|  |  |  | |  `--'  | |  |_)  |     |  |                          
|__|  |__|  \______/  |______/      |__|                              
                                                                  
 _______   __    ______  __  ___  __   __   __                    
|       \ |  |  /      ||  |/  / |  | |  | |  |                   
|  .--.  ||  | |  ,----'|  '  /  |  | |  | |  |                   
|  |  |  ||  | |  |     |    <   |  | |  | |  |                   
|  '--'  ||  | |  `----.|  .  \  |__| |__| |__|                   
|_______/ |__|  \______||__|\__\ (__) (__) (__)  

Congratulations! You've caught Moby Dick and have completed the game!                 
""")
        elif dice_roll == 1 or dice_roll <= 6:
            fishing_art(2)
            fishing_count += 1
            fisherman_level += 1
            total_money += fish_reward[dice_roll]
            experience_points += 7
            print(f"\nYou caught a(n) {fish[dice_roll]}, which is worth ${fish_reward[dice_roll]}!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll >= 7:
            fishing_count += 1
            print(f"\nYou didn't catch anything this time! Try again!")
            print(f"You currently have ${total_money} and {experience_points} XP.")

        while True:
            try:
                response = input(
                    f"\nYou have fished for {fishing_count} times. Would you like to fish in the park river again? Yes or no? (Y/N)").strip().lower()
                if response == "yes" or response == "y":
                    break
                elif response == "no" or response == "n":
                    options()
            except ValueError:
                print(f"Invalid entry! Please enter yes or no.")

def fishing_level():
    global fisherman_level

    if fisherman_level == 0:
        print(f"Your current Fisherman Level is 0.")
    elif fisherman_level < 100:
        temp_1 = 100
        print(f"Your current Fisherman Level is {fisherman_level // 100}.")
        print("*" * fisherman_level, f"{temp_1 - fisherman_level}% left until Fisherman Level {fisherman_level // 100 + 1}.")
    elif fisherman_level >= 100:
        temp_2 = fisherman_level // 100
        temp_3 = fisherman_level % 100
        print(f"Your current Fisherman Level is {temp_2}.")
        print("*" * temp_3, f"{100 - temp_3}% left until Fisherman Level {temp_2 + 1}.")

def fishing_level_bonus():
    global total_money, fisherman_level, experience_points
    bonus = fisherman_level // 100
    bonus_xp = fisherman_level // 100
    total_money += bonus
    experience_points += bonus_xp

    if bonus > 0:
        print(f"Due to your Fisherman Level of {fisherman_level // 100}, you've earned an extra ${bonus} and {bonus_xp} XP on this catch!")

def fishing_locations():
    global experience_points, player_equipment
    print("""
···········································
:YOU ARE NOW IN THE FISHING LOCATIONS MENU:
···········································
    """)
    print("""
Choose your fishing location:

1. Neighborhood pond 
2. Park river (Items and XP required: Apprentice Fishing Rod, Apprentice Fishing Boat, 100 XP)
3. County lake (Items and XP required: Journeyman Fishing Rod, Journeyman Fishing Boat, 500 XP)
4. Beach marina (Items and XP required: Expert Fishing Rod, Expert Fishing Boat, 1000 XP)
5. Atlantic Ocean (Items and XP required: Master Fishing Rod, Master Fishing Boat, 10000 XP)
6. Pacific Ocean (Items and XP required: Legendary Fishing Rod, Legendary Fishing Boat, 50000 XP)
7. WHALE CENTRAL (Items and XP required: Ultra Whaling Harpoon, Ultra Whaling Barge, 100000 XP)
        """)

    location = {1: "Neighborhood pond", 2: "Park river", 3: "County lake", 4: "Beach marina", 5: "Atlantic Ocean", 6: "Pacific Ocean", 7: "WHALES CENTRAL"}
    required_items = {2: ["Apprentice Fishing Rod", "Apprentice Fishing Boat"],
                      3: ["Journeyman Fishing Rod", "Journeyman Fishing Boat"],
                      4: ["Expert Fishing Rod", "Expert Fishing Boat"],
                      5: ["Master Fishing Rod", "Master Fishing Boat"],
                      6: ["Legendary Fishing Rod", "Legendary Fishing Boat"],
                      7: ["Ultra Whaling Harpoon", "Ultra Whaling Barge"]}
    required_experience = {2: 100, 3: 500, 4: 1000, 5: 10000, 6: 50000, 7: 100000}
    functions = {2: park_river, 3: county_lake, 4: beach_marina, 5: atlantic_ocean, 6: pacific_ocean, 7: whale_central}

    while True:
        try:
            choice = input("Which location will you select? Enter only integers as your response. Enter 0 if you want to return to the main options menu.")
            choice_int = int(choice)

            if choice_int == 1:
                neighborhood_pond()
            elif choice_int >= 2 and choice_int < 8:
                if experience_points < required_experience[choice_int]:
                    print(f"You can't fish in the {location[choice_int]} yet! You need at least {required_experience[choice_int]} XP.")
                    continue
                elif required_items[choice_int][0] not in player_equipment:
                    print(f"You can't fish in the {location[choice_int]} yet! You need the {required_items[choice_int][0]}.")
                    continue
                elif required_items[choice_int][1] not in player_equipment:
                    print(f"You can't fish in the {location[choice_int]} yet! You need the {required_items[choice_int][1]}.")
                    continue
                else:
                    functions[choice_int]()
            elif choice_int == 0:
                options()
            else:
                pass
        except ValueError:
            print(f"Invalid entry! Please enter valid integers between 1-7 or 0 as your response.")
            continue

def fishing_store():
    global total_money, player_equipment
    print("""
············································
:YOU ARE NOW IN THE FISHING EQUIPMENT STORE:
············································
        """)
    print("""
Here are the items on sale:

1. Apprentice Fishing Rod: $100
2. Apprentice Fishing Boat: $100
3. Journeyman Fishing Rod: $500
4. Journeyman Fishing Boat: $500
5. Expert Fishing Rod: $10,000
6. Expert Fishing Boat: $10,000
7. Master Fishing Rod: $100,000
8. Master Fishing Boat: $100,000
9. Legendary Fishing Rod: $500,000
10. Legendary Fishing Boat: $500,000
11. Ultra Whaling Harpoon: $1,000,000
12. Ultra Whaling Barge: $1,000,000
            """)
    items = {1: "Apprentice Fishing Rod",
             2: "Apprentice Fishing Boat",
             3: "Journeyman Fishing Rod",
             4: "Journeyman Fishing Boat",
             5: "Expert Fishing Rod",
             6: "Expert Fishing Boat",
             7: "Master Fishing Rod",
             8: "Master Fishing Boat",
             9: "Legendary Fishing Rod",
             10: "Legendary Fishing Boat",
             11: "Ultra Whaling Harpoon",
             12: "Ultra Whaling Barge"}

    items_price = {1: 100,
                   2: 100,
                   3: 500,
                   4: 500,
                   5: 10000,
                   6: 10000,
                   7: 100000,
                   8: 100000,
                   9: 500000,
                   10: 500000,
                   11: 1000000,
                   12: 1000000}

    while True:
        try:
            choice = input("What would you like to buy? Enter only integers as your response. Press 0 if you want to return to the main options menu.")
            choice_int = int(choice)
            if choice_int >= 1 and choice_int <= 12:
                if items[choice_int] in player_equipment:
                    print(f"You've already bought the {items[choice_int]}!")
                    continue
                elif total_money >= items_price[choice_int]:
                    total_money -= items_price[choice_int]
                    player_equipment.append(items[choice_int])
                    print(f"You've bought the {items[choice_int]}. Have fun!")
                    continue
                else:
                    print(f"You don't have enough money! The {items[choice_int]} costs ${items_price[choice_int]} and you only have ${total_money}.")
                    continue
            elif choice_int == 0:
                options()
        except ValueError:
            print(f"Invalid entry! Please enter valid integers between 1-12 or 0 as your response.")

def employment_center():
    global total_money, employees
    print("""
······································
:YOU ARE NOW IN THE EMPLOYMENT CENTER:
······································
""")
    print("""
Here are some prospective employees you can hire:

1. Novice Fishermen ($100 for each hire; Will generate an extra $1 and 1 XP on each catch)
2. Apprentice Fishermen ($500 for each hire; Will generate an extra $10 and 2 XP on each catch)
3. Journeyman Fishermen ($1000 for each hire; Will generate an extra $20 and 3 XP on each catch)
4. Expert Fishermen ($5000 for each hire; Will generate an extra $30 and 4 XP on each catch)
5. Master Fishermen ($10,000 for each hire; Will generate an extra $40 and 10 XP on each catch)
6. Legendary Fishermen ($50,000 for each hire; Will generate an extra $50 and 20 XP on each catch)
7. Ultra Fishermen ($100,000 for each hire; Will generate an extra $60 and 30 XP on each catch)
""")

    fishermen = {1: "Novice Fishermen", 2: "Apprentice Fishermen", 3: "Journeyman Fishermen", 4: "Expert Fishermen",
                 5: "Master Fishermen", 6: "Legendary Fishermen", 7: "Ultra Fishermen"}
    fishermen_price = {1: 100, 2: 500, 3: 1000, 4: 5000, 5: 10000, 6: 50000, 7: 100000}

    while True:
        try:
            choice = input("Who would you like to hire? Enter only integers as your response. Press 0 if you want to return to the main options menu.")
            choice_int = int(choice)
            if choice_int >= 1 and choice_int < 8:
                if total_money < fishermen_price[choice_int]:
                    print(f"You don't have enough money! You need ${fishermen_price[choice_int]} to hire {fishermen[choice_int]}.")
                    continue
                else:
                    total_money -= fishermen_price[choice_int]
                    employees.append(fishermen[choice_int])
                    print(f"You've hired a group of {fishermen[choice_int]}.")
                    continue
            elif choice_int == 0:
                options()
        except ValueError:
            print(f"Invalid entry! Please enter valid integers between 1-7 or 0 as your response.")

def employee_bonus():
    global employees, total_money, experience_points

    fishermen = {1: "Novice Fishermen", 2: "Apprentice Fishermen", 3: "Journeyman Fishermen", 4: "Expert Fishermen",
                 5: "Master Fishermen", 6: "Legendary Fishermen", 7: "Ultra Fishermen"}
    fishermen_bonus = {1: 1, 2: 10, 3: 20, 4: 30, 5: 40, 6: 50, 7: 60}
    fishermen_bonus_xp = {1: 1, 2: 2, 3: 3, 4: 4, 5: 10, 6: 20, 7: 30}

    for key, fisherman in fishermen.items():
        count = employees.count(fisherman)
        if count > 0:
            bonus = fishermen_bonus[key]
            bonus_xp = fishermen_bonus_xp[key]
            total_money += bonus * count
            experience_points += bonus_xp * count
            print(f"You have {count} group(s) of {fisherman} generating an extra ${bonus * count} and {bonus_xp * count} XP on this catch!")

def options():
    while True:
        print("""
······································
:YOU ARE NOW IN THE MAIN OPTIONS MENU:
······································
        """)
        print("""
Here are your options:

1. Select your fishing location.
2. Go to the fishing store and buy equipment.
3. Go to the employment center and hire employees.
4. Go to the save/load menu.
        """)

        choice = int(input("Which option will you select? Enter only integers as your response."))

        if choice == 1:
            fishing_locations()
        elif choice == 2:
            fishing_store()
        elif choice == 3:
            employment_center()
        elif choice == 4:
            display_save_menu()
        else:
            print("Invalid entry! Please enter valid integers between 1-5.")

options()