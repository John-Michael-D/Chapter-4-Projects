import random

wagers = 0
winnings = 0
starting_money = 1000

def dice_roll():
    """Simulates the rolling of two dice, adds up the total value of the roll, and determines if the sum is odd or even."""

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    sum = dice_1 + dice_2

    if sum % 2 == 0:
        print(rf"""
              _______.                                                                         
   ______    | .   . |\
  /     /\   |   .   |.\
 /  '  /  \  | .   . |.'|
/_____/. . \ |_______|.'|     You rolled {sum}, which is an even number! 
\ . . \    /  \ ' .   \'|
 \ . . \  /    \____'__\|
  \_____\/
        """)
        return sum
    elif sum % 2 != 0:
        print(rf"""
              _______.                                                                         
   ______    | .   . |\
  /     /\   |   .   |.\
 /  '  /  \  | .   . |.'|
/_____/. . \ |_______|.'|     You rolled {sum}, which is an odd number!
\ . . \    /  \ ' .   \'|
 \ . . \  /    \____'__\|
  \_____\/
        """)
        return sum

def dice_roll_ante():
    """Calculates wagers and winnings."""

    global wagers, winnings, starting_money

    while True:
        try:
            amount = input(f"\nHow much $ would you like to wager? Respond with valid integers only.").strip().lower()
            amount_int = int(amount)
            wagers += amount_int
            print(f"\nYou've wagered {amount_int} dollars. Good luck!")
            break
        except ValueError:
            print(f"\nInvalid entry! Respond with only valid integers.")
            continue

    while True:
        try:
            bet = input(f"\nWould you like to bet if the dice roll will be even or odd?").strip().lower()
            if bet == "even":
                print(f"\nYou've bet {amount_int} dollars that the dice roll will be even. Good luck!")
                roll_result = dice_roll()
                break
            elif bet == "odd":
                print(f"\nYou've bet {amount_int} dollars that the dice roll will be odd. Good luck!")
                roll_result = dice_roll()
                break
            else:
                print(f"\nInvalid entry! Respond only with even or odd.")
        except ValueError:
            continue

    if roll_result % 2 == 0 and bet == "even":
        winnings += amount_int * 2
        starting_money += amount_int * 2
        print(r"""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣴⣶⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⠟⠁⠈⠙⠻⢇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣷⣄⡀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣦⣀⠀⢀⣼⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⢿⣿⣿⣿⣷⣾⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡿⠃⠀⠙⢿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⠀⠀⠀⠀⠀⠀⢰⣿⣿⡿⠁⠀⠀⠀⠀⠙⠻⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣦⣄⠀⠀⢰⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⣿⠛⠿⣿⣿⣿⣿⣦⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⡟⠁⠀⠀⠀⠈⠙⠻⢿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⣤⠶⢤⠄⠶⢶⠶⠦⢠⡴⢦⣄⠀⣶⡀⠀⢰⠀⢰⠀⢀⡴⠂⢠⡴⠦⡄⠀⠀⠀⠀⠀⠀
⠀⡰⠃⠀⠀⠀⠀⠀⠀⠀⠀⢧⣤⣄⠀⠀⢸⠀⠀⣿⠀⠀⣿⠀⣿⠳⡄⢸⠀⢸⣠⢾⠁⠀⠻⣤⣤⡀⠀⠀⠀⠀⠀⠀
⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣀⣸⠇⠀⢸⠀⠀⢿⣀⣀⡿⠀⣿⠀⠹⣾⠀⢸⠁⠈⢧⡀⣄⣀⣀⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠈⠀⠀⠀⠉⠉⠀⠀⠉⠀⠀⠈⠀⠈⠀⠀⠈⠁⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀
        """)
        print(f"\nCongratulations! You won the bet!")
        print(f"\nYou've wagered a total of {wagers} dollars and won a total of {winnings} dollars.")
        print(f"You have {starting_money} dollars remaining.")
    elif roll_result % 2 != 0 and bet == "even":
        winnings -= amount_int
        starting_money -= amount_int
        print(f"\nOh no! You lost the bet!")
        print(f"\nYou've wagered a total of {wagers} dollars and won a total of {winnings} dollars.")
        print(f"You have {starting_money} dollars remaining.")
    elif roll_result % 2 != 0 and bet == "odd":
        winnings += amount_int * 2
        starting_money += amount_int * 2
        print(r"""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣴⣶⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⠟⠁⠈⠙⠻⢇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣷⣄⡀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣦⣀⠀⢀⣼⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⢿⣿⣿⣿⣷⣾⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡿⠃⠀⠙⢿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⠀⠀⠀⠀⠀⠀⢰⣿⣿⡿⠁⠀⠀⠀⠀⠙⠻⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣦⣄⠀⠀⢰⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⣿⠛⠿⣿⣿⣿⣿⣦⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⡟⠁⠀⠀⠀⠈⠙⠻⢿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⣤⠶⢤⠄⠶⢶⠶⠦⢠⡴⢦⣄⠀⣶⡀⠀⢰⠀⢰⠀⢀⡴⠂⢠⡴⠦⡄⠀⠀⠀⠀⠀⠀
⠀⡰⠃⠀⠀⠀⠀⠀⠀⠀⠀⢧⣤⣄⠀⠀⢸⠀⠀⣿⠀⠀⣿⠀⣿⠳⡄⢸⠀⢸⣠⢾⠁⠀⠻⣤⣤⡀⠀⠀⠀⠀⠀⠀
⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣀⣸⠇⠀⢸⠀⠀⢿⣀⣀⡿⠀⣿⠀⠹⣾⠀⢸⠁⠈⢧⡀⣄⣀⣀⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠈⠀⠀⠀⠉⠉⠀⠀⠉⠀⠀⠈⠀⠈⠀⠀⠈⠁⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀
        """)
        print(f"\nCongratulations! You won the bet!")
        print(f"\nYou've wagered a total of {wagers} dollars and won a total of {winnings} dollars.")
        print(f"You have {starting_money} dollars remaining.")
    elif roll_result % 2 == 0 and bet == "odd":
        winnings -= amount_int
        starting_money -= amount_int
        print(f"\nOh no! You lost the best!")
        print(f"\nYou've wagered a total of {wagers} dollars and won a total of {winnings} dollars.")
        print(f"You have {starting_money} dollars remaining.")

def gambling_intializer():
    while True:
        if starting_money <= 0:
            print(f"\nYou've run out of money! Game over!")
            break
        try:
            question = input(f"\nWould you like to gamble? Yes or no?").strip().lower()

            if question == "yes":
                dice_roll_ante()
            elif question == "no":
                print(f"\nEnjoy your day!")
                break
            else:
                print(f"\nInvalid entry! Only respond with yes or no.")
        except ValueError:
            continue

print("""
__        _______ _     ____ ___  __  __ _____   _____ ___  
\ \      / / ____| |   / ___/ _ \|  \/  | ____| |_   _/ _ \ 
 \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|     | || | | |
  \ V  V / | |___| |__| |__| |_| | |  | | |___    | || |_| |
 __\_/\_/  |_____|_____\____\___/|_|__|_|_____| _ |_|_\___/ 
|_   _| | | | ____|  / ___|  / \  / ___|_ _| \ | |/ _ \| |  
  | | | |_| |  _|   | |     / _ \ \___ \| ||  \| | | | | |  
  | | |  _  | |___  | |___ / ___ \ ___) | || |\  | |_| |_|  
  |_| |_| |_|_____|  \____/_/   \_\____/___|_| \_|\___/(_)  
  
  This is a gambling game where you roll two dice and have to wager a certain amount of money to bet if the dice roll will be even or odd.
  The rules of the game are simple:
  
  1. If you win a bet, you'll get back TWICE the amount of money you wagered in winnings.
  2. You start the game with $1000. If you run out of money, you lose the game.
  
  Good luck, high roller!
""")

gambling_intializer()