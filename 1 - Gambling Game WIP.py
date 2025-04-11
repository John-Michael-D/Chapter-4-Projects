import random

wagers = 0
winnings = 0

def dice_roll():
    """Simulates the rolling of two dice, adds up the total value of the roll, and determines if the sum is odd or even."""

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    sum = dice_1 + dice_2

    if sum % 2 == 0:
        print(f"\nYou rolled {sum}, which is an even number!")
        return sum
    elif sum % 2 != 0:
        print(f"\nYou rolled {sum}, which is an odd number!")
        return sum

def dice_roll_ante():
    """Calculates wagers and winnings."""

    global wagers, winnings

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
        print(f"\nCongratulations! You won the bet!")
        print(f"\nYou've wagered a total of {wagers} dollars and won a total of {winnings} dollars.")
    elif roll_result % 2 != 0 and bet == "even":
        winnings -= amount_int
        print(f"\nOh no! You lost the bet!")
        print(f"\nYou've wagered a total of {wagers} dollars and won a total of {winnings} dollars.")
    elif roll_result % 2 != 0 and bet == "odd":
        winnings += amount_int * 2
        print(f"\nCongratulations! You won the bet!")
        print(f"\nYou've wagered a total of {wagers} dollars and won a total of {winnings} dollars.")
    elif roll_result % 2 == 0 and bet == "odd":
        winnings -= amount_int
        print(f"\nOh no! You lost the best!")
        print(f"\nYou've wagered a total of {wagers} dollars and won a total of {winnings} dollars.")

while True:
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