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
4. Reach the final level of the game: WHALE CENTRAL!
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
        fish_reward = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}

        if dice_roll == 1 or dice_roll <= 6:
            fishing_art(1)
            fishing_count += 1
            fisherman_level.append(1)
            total_money += fish_reward[dice_roll]
            experience_points += 1
            print(f"\nYou caught a {fish[dice_roll]}, which is worth ${fish_reward[dice_roll]}!")
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
    global total_money, experience_points, fishing_count

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
            fisherman_level.append(1)
            total_money += fish_reward[dice_roll]
            experience_points += 2
            print(f"\nYou caught a {fish[dice_roll]}, which is worth ${fish_reward[dice_roll]}!")
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
    global total_money, experience_points, fishing_count

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
            fisherman_level.append(1)
            total_money += fish_reward[dice_roll]
            experience_points += 3
            print(f"\nYou caught a {fish[dice_roll]}, which is worth ${fish_reward[dice_roll]}!")
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

def fishing_level_bonus():
    global total_money, fisherman_level
    bonus = int(len(fisherman_level) / 100)
    total_money += bonus

    if bonus > 0:
        print(f"Due to your Fisherman Level of {int(len(fisherman_level) / 100)}, you've earned an extra ${bonus} on this catch!")

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
7. WHALE CENTRAL (Items and XP required: Ultra Fishing Rod, Ultra Fishing Boat, 100000 XP)
        """)

    location = {1: "Neighborhood pond", 2: "Park river", 3: "County lake", 4: "Beach marina", 5: "Atlantic Ocean", 6: "Pacific Ocean", 7: "WHALES CENTRAL"}
    required_items = {2: ["Apprentice Fishing Rod", "Apprentice Fishing Boat"],
                      3: ["Journeyman Fishing Rod", "Journeyman Fishing Boat"],
                      4: ["Expert Fishing Rod", "Expert Fishing Boat"],
                      5: ["Master Fishing Rod", "Master Fishing Boat"],
                      6: ["Legendary Fishing Rod", "Legendary Fishing Boat"],
                      7: ["Ultra Fishing Rod", "Ultra Fishing Boat"]}
    required_experience = {2: 100, 3: 500, 4: 1000, 5: 10000, 6: 50000, 7: 100000}
    functions = {2: park_river, 3: county_lake}

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
5. Expert Fishing Rod: $10,000
6. Expert Fishing Boat: $10,000
7. Master Fishing Rod: $100,000
8. Master Fishing Boat: $100,000
9. Legendary Fishing Rod: $500,000
10. Legendary Fishing Boat: $500,000
11. Ultra Fishing Rod: $1,000,000
12. Ultra Fishing Boat: $1,000,000
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
             11: "Ultra Fishing Rod",
             12: "Ultra Fishing Boat"}

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
                    print(f"You don't have enough money! The {items[choice_int]} costs ${items_price[choice_int]}and you only have ${total_money}.")
                    continue
            elif choice_int == 0:
                options()
        except ValueError:
            print(f"Invalid entry! Please enter valid integers as your response.")

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
4. Expert Fishermen ($5000 for each hire; Will generate an extra $30 on each catch)
5. Master Fishermen ($10,000 for each hire; Will generate an extra $40 on each catch)
6. Legendary Fishermen ($50,000 for each hire; Will generate an extra $50 on each catch)
7. Ultra Fishermen ($100,000 for each hire; Will generate an extra $60 on each catch)
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
                    print(f"You've hired {fishermen[choice_int]}.")
                    continue
            elif choice_int == 0:
                options()
        except ValueError:
            print(f"Invalid entry! Please enter valid integers as your response.")

def employee_bonus():
    global employees, total_money

    fishermen = {1: "Novice Fishermen", 2: "Apprentice Fishermen", 3: "Journeyman Fishermen", 4: "Expert Fishermen",
                 5: "Master Fishermen", 6: "Legendary Fishermen", 7: "Ultra Fishermen"}
    fishermen_bonus = {1: 1, 2: 10, 3: 20, 4: 30, 5: 40, 6: 50, 7: 60}

    for key, fisherman in fishermen.items():
        count = employees.count(fisherman)
        if count > 0:
            bonus = fishermen_bonus[key]
            total_money += bonus * count
            print(f"You have {count} {fisherman} generating an extra ${bonus * count} on this catch!")

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
        except ValueError:
            print(f"Invalid entry! Please enter valid integers as your response.")

options()