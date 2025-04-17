import random

total_money = 0
experience_points = 0
fishing_count = 0
fisherman_level = []
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

    while True:
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
            fisherman_level.append(1)
            total_money += 1
            experience_points += 1
            print(f"\nYou caught a {fish[1]}, which is worth $1!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll == 2:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += 2
            experience_points += 1
            print(f"\nYou caught a {fish[2]}, which is worth $2!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll == 3:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += 3
            experience_points += 1
            print(f"\nYou caught a {fish[3]}, which is worth $3!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll == 4:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += 4
            experience_points += 1
            print(f"\nYou caught a {fish[4]}, which is worth $4!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll == 5:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += 5
            experience_points += 1
            print(f"\nYou caught an {fish[5]}, which is worth $5!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll == 6:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += 6
            experience_points += 1
            print(f"\nYou caught a {fish[6]}, which is worth $6!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll == 7:
            fishing_count += 1
            print(f"\nYou didn't catch anything this time! Try again!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
        elif dice_roll == 8:
            fishing_count += 1
            print(f"\nYou didn't catch anything this time! Try again!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
        else:
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
                else:
                    print(f"Invalid entry! Please enter yes or no.")
            except ValueError:
                continue

def park_river():
    global total_money, experience_points, fishing_count

    while True:
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
            fisherman_level.append(1)
            total_money += 7
            experience_points += 2
            print(f"\nYou caught a {fish[1]}, which is worth $7!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll == 2:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += 8
            experience_points += 2
            print(f"\nYou caught a {fish[2]}, which is worth $8!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll == 3:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += 9
            experience_points += 2
            print(f"\nYou caught a {fish[3]}, which is worth $9!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll == 4:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += 10
            experience_points += 2
            print(f"\nYou caught a {fish[4]}, which is worth $10!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll == 5:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += 11
            experience_points += 2
            print(f"\nYou caught a {fish[5]}, which is worth $11!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll == 6:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += 12
            experience_points += 2
            print(f"\nYou caught an {fish[6]}, which is worth $12!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
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
                    break
                elif response == "no" or response == "n":
                    options()
                else:
                    print(f"Invalid entry! Please enter yes or no.")
            except ValueError:
                continue

def county_lake():
    global total_money, experience_points, fishing_count

    while True:
        print("""
········································
:YOU ARE NOW FISHING IN THE COUNTY LAKE:
········································
    """)

        dice_roll = random.randint(1,9)
        fish = {1:"Yellowfin Tuna", 2:"Sockeye Salmon", 3:"Pink Salmon", 4:"Atlantic Mackerel", 5:"European Sardine", 6: "Haddock"}

        if dice_roll == 1:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += 13
            experience_points += 3
            print(f"\nYou caught a {fish[1]}, which is worth $13!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll == 2:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += 14
            experience_points += 3
            print(f"\nYou caught a {fish[2]}, which is worth $14!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll == 3:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += 15
            experience_points += 3
            print(f"\nYou caught a {fish[3]}, which is worth $15!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll == 4:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += 16
            experience_points += 3
            print(f"\nYou caught an {fish[4]}, which is worth $16!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll == 5:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += 17
            experience_points += 3
            print(f"\nYou caught a {fish[5]}, which is worth $17!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
        elif dice_roll == 6:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += 18
            experience_points += 3
            print(f"\nYou caught a {fish[6]}, which is worth $18!")
            print(f"You currently have ${total_money} and {experience_points} XP.")
            fishing_level()
            fishing_level_bonus()
            employee_bonus()
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
                    break
                elif response == "no" or response == "n":
                    options()
                else:
                    print(f"Invalid entry! Please enter yes or no.")
            except ValueError:
                continue

def fishing_level():
    global fisherman_level

    if len(fisherman_level) == 0:
        print(f"Your current Fisherman Level is 0.")
    elif len(fisherman_level) < 100:
        temp_1 = 100
        print(f"Your current Fisherman Level is {int(len(fisherman_level) / 100)}.")
        print("*" * len(fisherman_level), f"{temp_1 - len(fisherman_level)}% left until Fisherman Level {int(len(fisherman_level) / 100) + 1}.")
    elif len(fisherman_level) >= 100:
        temp_2 = len(fisherman_level) // 100
        temp_3 = len(fisherman_level) % 100
        print(f"Your current Fisherman Level is {temp_2}.")
        print("*" * int(temp_3), f"{100 - int(temp_3)}% left until Fisherman Level {int(temp_2) + 1}.")
    else:
        pass

def fishing_level_bonus():
    global total_money, fisherman_level
    bonus = int(len(fisherman_level) / 100)
    total_money += bonus

    if bonus > 0:
        print(f"Due to your Fisherman Level of {int(len(fisherman_level) / 100)}, you've earned an extra ${bonus} on this catch!")
    else:
        pass

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
                if experience_points < 99:
                    print("You can't fish in the park river yet! You need at least 100 XP.")
                    continue
                elif "Apprentice Fishing Rod" not in player_equipment:
                    print("You can't fish in the park river yet! You need the Apprentice Fishing Rod.")
                    continue
                elif "Apprentice Fishing Boat" not in player_equipment:
                    print("You can't fish in the park river yet! You need the Apprentice Fishing Boat.")
                    continue
                else:
                    park_river()
            elif choice_int == 3:
                if experience_points < 500:
                    print("You can't fish in the county lake yet! You need at least 500 XP.")
                    continue
                elif "Journeyman Fishing Rod" not in player_equipment:
                    print("You can't fish in the county lake yet! You need the Journeyman Fishing Rod.")
                    continue
                elif "Journeyman Fishing Boat" not in player_equipment:
                    print("You can't fish in the county lake yet! You need the Journeyman Fishing Boat.")
                    continue
                else:
                    county_lake()
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
                if "Apprentice Fishing Rod" in player_equipment:
                    print("You've already bought the Apprentice Fishing Rod!")
                    continue
                elif total_money >= 100:
                    total_money -= 100
                    player_equipment.append("Apprentice Fishing Rod")
                    print("You've bought the Apprentice Fishing Rod. Have fun!")
                    continue
                else:
                    print(f"You don't have enough money! The Apprentice Fishing Rod costs $100 and you only have ${total_money}.")
                    continue
            elif choice_int == 2:
                if "Apprentice Fishing Boat" in player_equipment:
                    print("You've already bought the Apprentice Fishing Boat!")
                    continue
                elif total_money >= 100:
                    total_money -= 100
                    player_equipment.append("Apprentice Fishing Boat")
                    print("You've bought the Apprentice Fishing Boat! Have fun!")
                    continue
                else:
                    print(f"You don't have enough money! The Apprentice Fishing Boat costs $100 and you only have ${total_money}.")
                    continue
            elif choice_int == 3:
                if "Journeyman Fishing Rod" in player_equipment:
                    print("You've already bought the Journeyman Fishing Rod!")
                    continue
                elif total_money >= 500:
                    total_money -= 500
                    player_equipment.append("Journeyman Fishing Rod")
                    print("You've bought the Journeyman Fishing Rod. Have fun!")
                    continue
                else:
                    print(f"You don't have enough money! The Journeyman Fishing Rod costs $500 and you only have ${total_money}.")
                    continue
            elif choice_int == 4:
                if "Journeyman Fishing Boat" in player_equipment:
                    print("You've already bought the Journeyman Fishing Boat!")
                    continue
                elif total_money >= 500:
                    total_money -= 500
                    player_equipment.append("Journeyman Fishing Boat")
                    print("You've bought the Journeyman Fishing Boat! Have fun!")
                    continue
                else:
                    print(f"You don't have enough money! The Journeyman Fishing Boat coasts $500 and you only have ${total_money}.")
                    continue
            elif choice_int == 0:
                options()
            else:
                print(f"Invalid entry! Please enter valid integers as your response.")
                continue
        except ValueError:
            print(f"Invalid entry! Please enter valid integers as your response.")
            continue

def employment_center():
    global total_money, employees
    print("""
······································
:YOU ARE NOW IN THE EMPLOYMENT CENTER:
······································
""")
    print("""
Here are some prospective employees you can hire:

1. Novice Fishermen ($100 for each hire; Will generate an extra $1 on each catch)
2. Apprentice Fishermen ($500 for each hire; Will generate an extra $10 on each catch)
3. Journeyman Fishermen ($1000 for each hire; Will generate an extra $20 on each catch)
""")

    while True:
        try:
            choice = input("Who would you like to hire? Enter only integers as your response. Press 0 if you want to return to the main options menu.")
            choice_int = int(choice)
            if choice_int == 1:
                if total_money < 100:
                    print("You don't have enough money! You need $100 to hire Novice Fishermen.")
                    continue
                else:
                    total_money -= 100
                    employees.append("Novice Fishermen")
                    print("You've hired a Novice Fisherman!")
                    continue
            elif choice_int == 2:
                if total_money < 500:
                    print("You don't have enough money! You need $500 to hire Apprentice Fishermen.")
                    continue
                else:
                    total_money -= 500
                    employees.append("Apprentice Fishermen")
                    print("You've hired an Apprentice Fisherman!")
                    continue
            elif choice_int == 3:
                if total_money < 1000:
                    print("You don't have enough money! You need $1000 to hire Journeyman Fishermen.")
                    continue
                else:
                    total_money -= 1000
                    employees.append("Journeyman Fishermen")
                    print("You've hired a Journeyman Fisherman!")
                    continue
            elif choice_int == 0:
                options()
            else:
                print(f"Invalid entry! Please enter valid integers as your response.")
                continue
        except ValueError:
            print(f"Invalid entry! Please enter valid integers as your response.")
            continue

def employee_bonus():
    global employees, total_money

    novice_num = employees.count("Novice Fishermen")
    apprentice_num = employees.count("Apprentice Fishermen")
    journeyman_num = employees.count("Journeyman Fishermen")

    if novice_num > 0:
        bonus_1 = 1 * novice_num
        total_money += bonus_1
        print(f"You have {novice_num} Novice Fishermen generating an extra ${bonus_1} on this catch!")
    else:
        pass
    if apprentice_num > 0:
        bonus_2 = 10 * apprentice_num
        total_money += bonus_2
        print(f"You have {apprentice_num} Apprentice Fishermen generating an extra ${bonus_2} on this catch!")
    else:
        pass
    if journeyman_num > 0:
        bonus_3 = 20 * journeyman_num
        total_money += bonus_3
        print(f"You have {journeyman_num} Journeyman Fishermen generating an extra ${bonus_3} on this catch!")
    else:
        pass

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
3. Go to the employment center and hire employees.
    """)

    while True:
        try:
            choice = input("Which option will you select? Enter only integers as your response.")
            choice_int = int(choice)
            if choice_int == 1:
                fishing_locations()
            elif choice_int == 2:
                fishing_store()
            elif choice_int == 3:
                employment_center()
            else:
                pass
        except ValueError:
            print(f"Invalid entry! Please enter valid integers as your response.")
            continue

options()