import random

total_money = 0
experience_points = 0
player_equipment = []

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
""")

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

def small_pond():
    global total_money, experience_points

    dice_roll = random.randint(1,9)
    fish = {1:"Grass Carp", 2:"Peruvian Anchoveta", 3:"Silver Carp", 4:"Common Carp", 5:"Alaska Pollock", 6: "Nile tilapia"}

    if dice_roll == 1:
        fishing_art(1)
        total_money += 1
        experience_points += 1
        print(f"\nYou caught a {fish[1]}, which is worth $1!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 2:
        fishing_art(1)
        total_money += 2
        experience_points += 1
        print(f"\nYou caught a {fish[2]}, which is worth $2!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 3:
        fishing_art(1)
        total_money += 3
        experience_points += 1
        print(f"\nYou caught a {fish[3]}, which is worth $3!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 4:
        fishing_art(1)
        total_money += 4
        experience_points += 1
        print(f"\nYou caught a {fish[4]}, which is worth $4!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 5:
        fishing_art(1)
        total_money += 5
        experience_points += 1
        print(f"\nYou caught a {fish[5]}, which is worth $5!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 6:
        fishing_art(1)
        total_money += 6
        experience_points += 1
        print(f"\nYou caught a {fish[6]}, which is worth $6!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 7:
        print(f"\nYou didn't catch anything this time! Try again!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 8:
        print(f"\nYou didn't catch anything this time! Try again!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    else:
        print(f"\nYou didn't catch anything this time! Try again!")
        print(f"You currently have ${total_money} and {experience_points} XP.")

    while True:
        try:
            response = input("\nWould you like to fish in the small pond again? Yes or no? (Y/N)").strip().lower()

            if response == "yes" or response == "y":
                small_pond()
            elif response == "no" or response == "n":
                options()
            else:
                print(f"Invalid entry! Please enter yes or no.")
        except ValueError:
            continue

def fishing_locations():
    global experience_points, player_equipment
    print("""
Choose your fishing location:

1. Small pond
2. Big lake
3. Beach marina
        """)

    while True:
        try:
            choice = input("Which option will you select? Enter only integers as your response.")
            choice_int = int(choice)
            if choice_int == 1:
                small_pond()
            elif choice_int == 2 and experience_points < 99 and "Apprentice Fishing Rod" and "Apprentice Fishing Boat" not in player_equipment:
                print("You can't fish in the big lake yet! You need the Apprentice Fishing Rod and Apprentice Fishing Boat and you need at least 100 XP.")
                continue
            elif choice_int == 3 and experience_points < 500 and "Journeyman Fishing Rod" and "Journeyman Fishing Boat" not in player_equipment:
                print(f"You can't fish in the beach marina yet! You need the Journeyman Fishing Rod and Journeyman Fishing Boat and you need at least 500 XP.")
                continue
            else:
                pass
        except ValueError:
            print(f"Invalid entry! Please enter valid integers as your response.")
            continue

def options():
    print("""
Here are your options:
    
1. Select your fishing location.
2. Go to the store and buy equipment. (NOT CURRENTLY AVAILABLE)
    """)

    while True:
        try:
            choice = input("Which option will you select? Enter only integers as your response.")
            choice_int = int(choice)
            if choice_int == 1:
                fishing_locations()
            else:
                pass
        except ValueError:
            print(f"Invalid entry! Please enter valid integers as your response.")
            continue

options()