import random

total_money = 0
experience_points = 0
fishing_count = 0
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

def neighborhood_pond():
    global total_money, experience_points, fishing_count
    print("""
··············································
:YOU ARE NOW FISHING IN THE NEIGHBORHOOD POND:
··············································
""")

    dice_roll = random.randint(1,9)
    fish = {1:"Grass Carp", 2:"Peruvian Anchoveta", 3:"Silver Carp", 4:"Common Carp", 5:"Alaska Pollock", 6: "Nile Tilapia"}

    if dice_roll == 1:
        fishing_art(1)
        fishing_count += 1
        total_money += 1
        experience_points += 1
        print(f"\nYou caught a {fish[1]}, which is worth $1!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 2:
        fishing_art(1)
        fishing_count += 1
        total_money += 2
        experience_points += 1
        print(f"\nYou caught a {fish[2]}, which is worth $2!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 3:
        fishing_art(1)
        fishing_count += 1
        total_money += 3
        experience_points += 1
        print(f"\nYou caught a {fish[3]}, which is worth $3!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 4:
        fishing_art(1)
        fishing_count += 1
        total_money += 4
        experience_points += 1
        print(f"\nYou caught a {fish[4]}, which is worth $4!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 5:
        fishing_art(1)
        fishing_count += 1
        total_money += 5
        experience_points += 1
        print(f"\nYou caught an {fish[5]}, which is worth $5!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 6:
        fishing_art(1)
        fishing_count += 1
        total_money += 6
        experience_points += 1
        print(f"\nYou caught a {fish[6]}, which is worth $6!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 7:
        fishing_count += 1
        print(f"\nYou didn't catch anything this time! Try again!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 8:
        fishing_count += 1
        print(f"\nYou didn't catch anything this time! Try again!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    else:
        fishing_count += 1
        print(f"\nYou didn't catch anything this time! Try again!")
        print(f"You currently have ${total_money} and {experience_points} XP.")

    while True:
        try:
            response = input(f"\nYou have fished for {fishing_count} times. Would you like to fish in the neighborhood pond again? Yes or no? (Y/N)").strip().lower()

            if response == "yes" or response == "y":
                neighborhood_pond()
            elif response == "no" or response == "n":
                options()
            else:
                print(f"Invalid entry! Please enter yes or no.")
        except ValueError:
            continue

def park_river():
    global total_money, experience_points, fishing_count
    print("""
·······································
:YOU ARE NOW FISHING IN THE PARK RIVER:
·······································
""")

    dice_roll = random.randint(1,9)
    fish = {1:"Whiteleg Shrimp", 2:"Bighead Carp", 3:"Skipjack Tuna", 4:"Catla", 5:"Bluefin Tuna", 6: "Atlantic Cod"}

    if dice_roll == 1:
        fishing_art(1)
        fishing_count += 1
        total_money += 7
        experience_points += 2
        print(f"\nYou caught a {fish[1]}, which is worth $7!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 2:
        fishing_art(1)
        fishing_count += 1
        total_money += 8
        experience_points += 2
        print(f"\nYou caught a {fish[2]}, which is worth $8!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 3:
        fishing_art(1)
        fishing_count += 1
        total_money += 9
        experience_points += 2
        print(f"\nYou caught a {fish[3]}, which is worth $9!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 4:
        fishing_art(1)
        fishing_count += 1
        total_money += 10
        experience_points += 2
        print(f"\nYou caught a {fish[4]}, which is worth $10!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 5:
        fishing_art(1)
        fishing_count += 1
        total_money += 11
        experience_points += 2
        print(f"\nYou caught a {fish[5]}, which is worth $11!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 6:
        fishing_art(1)
        fishing_count += 1
        total_money += 12
        experience_points += 2
        print(f"\nYou caught an {fish[6]}, which is worth $12!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 7:
        fishing_count += 1
        print(f"\nYou didn't catch anything this time! Try again!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    elif dice_roll == 8:
        fishing_count += 1
        print(f"\nYou didn't catch anything this time! Try again!")
        print(f"You currently have ${total_money} and {experience_points} XP.")
    else:
        fishing_count += 1
        print(f"\nYou didn't catch anything this time! Try again!")
        print(f"You currently have ${total_money} and {experience_points} XP.")

    while True:
        try:
            response = input(f"\nYou have fished for {fishing_count} times. Would you like to fish in the park river again? Yes or no? (Y/N)").strip().lower()

            if response == "yes" or response == "y":
                park_river()
            elif response == "no" or response == "n":
                options()
            else:
                print(f"Invalid entry! Please enter yes or no.")
        except ValueError:
            continue

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
2. Park river
3. County lake
        """)

    while True:
        try:
            choice = input("Which location will you select? Enter only integers as your response. Enter 0 if you want to return to the main options menu.")
            choice_int = int(choice)
            if choice_int == 1:
                neighborhood_pond()
            elif choice_int == 2:
                if experience_points < 99 and "Apprentice Fishing Rod" and "Apprentice Fishing Boat" not in player_equipment:
                    print("You can't fish in the park river yet! You need the Apprentice Fishing Rod and Apprentice Fishing Boat and you need at least 100 XP.")
                    continue
                elif experience_points >= 100 and "Apprentice Fishing Rod" and "Apprentice Fishing Boat" in player_equipment:
                    park_river()
            elif choice_int == 3 and experience_points < 500 and "Journeyman Fishing Rod" and "Journeyman Fishing Boat" not in player_equipment:
                print(f"You can't fish in the county lake yet! You need the Journeyman Fishing Rod and Journeyman Fishing Boat and you need at least 500 XP.")
                continue
            elif choice_int == 0:
                options()
            else:
                pass
        except ValueError:
            print(f"Invalid entry! Please enter valid integers as your response.")
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
            """)

    while True:
        try:
            choice = input("What would you like to buy? Enter only integers as your response. Press 0 if you want to return to the main options menu.")
            choice_int = int(choice)
            if choice_int == 1:
                if total_money >= 100:
                    total_money -= 100
                    player_equipment.append("Apprentice Fishing Rod")
                    print("You've bought the Apprentice Fishing Rod. Have fun!")
                    continue
                else:
                    print(f"You don't have enough money! The Apprentice Fishing Rod costs $100 and you only have ${total_money}.")
            if choice_int == 2:
                if total_money >= 100:
                    total_money -= 100
                    player_equipment.append("Apprentice Fishing Boat")
                    print("You've bought the Apprentice Fishing Boat! Have fun!")
                else:
                    print(f"You don't have enough money! The Apprentice Fishing Boat coasts $100 and you only have ${total_money}.")
                    continue
            if choice_int == 0:
                options()
            else:
                pass
        except ValueError:
            print(f"Invalid entry! Please enter valid integers as your response.")
            continue

def options():
    print("""
······································
:YOU ARE NOW IN THE MAIN OPTIONS MENU:
······································
    """)
    print("""
Here are your options:
    
1. Select your fishing location.
2. Go to the fishing store and buy equipment.
    """)

    while True:
        try:
            choice = input("Which option will you select? Enter only integers as your response.")
            choice_int = int(choice)
            if choice_int == 1:
                fishing_locations()
            elif choice_int == 2:
                fishing_store()
            else:
                pass
        except ValueError:
            print(f"Invalid entry! Please enter valid integers as your response.")
            continue

options()