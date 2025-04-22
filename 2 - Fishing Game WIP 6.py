import random

class bodyOfWater:

    def __init__(self,commonFish,uncommonFish,rareFish,legendaryFish,equipment,prizeMultiplier):
        self.commonFish = commonFish
        self.uncommonFish = uncommonFish
        self.rareFish = rareFish
        self.legendaryFish = legendaryFish
        self.equipment = equipment
        self.prizeMultiplier = prizeMultiplier
        self.commonFish_prize = random.randint(1,12)
        self.uncommonFish_prize = random.randint(1,12) * 2
        self.rareFish_prize = random.randint(1,12) * 3
        self.legendaryFish_prize = random.randint(1, 12) * 4


class fisherman:

    def __init__(self,carryingCapacity,equipment,fishInventory,money):
        self.carryingCapacity = carryingCapacity
        self.equipment = equipment
        self.fishInventory = fishInventory
        self.money = money

    def addEquipment(self,items):
        self.equipment.append(items)

default_capacity = 10

player = fisherman(default_capacity, ["Novice Fishing Rod", "Novice Fishing Boat"], [], 0)

neighborhoodPond = bodyOfWater(["Grass Carp"],["Peruvian Anchoveta", "Silver Carp"],
                               ["Reed Carp", "Alaska Pollock"],["Nile Tilapia"],
                               ["Novice Fishing Rod", "Novice Fishing Boat"],1)

def gameLoop():
    while True:
        print("\nYou're fishing in the neighborhood pond!")
        dice_roll = random.randint(1,12)
        dice_roll_index = random.randint(0,1)
        amount_caught = random.randint(1, player.carryingCapacity)

        if dice_roll >= 1 and dice_roll <= 4:
            player.fishInventory.extend([neighborhoodPond.commonFish[0]] * amount_caught)
            player.carryingCapacity -= amount_caught
            print(f"You caught {amount_caught} Common {neighborhoodPond.commonFish[0]}!")
            print(f"You currently have enough space in your icebox for {player.carryingCapacity} more fish.")
        elif dice_roll >= 5 and dice_roll <= 7:
            player.fishInventory.extend([neighborhoodPond.uncommonFish[dice_roll_index]] * amount_caught)
            player.carryingCapacity -= amount_caught
            print(f"You caught {amount_caught} Uncommon {neighborhoodPond.uncommonFish[dice_roll_index]}!")
            print(f"You currently have enough space in your icebox for {player.carryingCapacity} more fish.")
        elif dice_roll >= 8 and dice_roll <= 10:
            player.fishInventory.extend([neighborhoodPond.rareFish[dice_roll_index]] * amount_caught)
            player.carryingCapacity -= amount_caught
            print(f"You caught {amount_caught} Rare {neighborhoodPond.rareFish[dice_roll_index]}!")
            print(f"You currently have enough space in your icebox for {player.carryingCapacity} more fish.")
        elif dice_roll >= 11 and dice_roll <= 12:
            player.fishInventory.extend([neighborhoodPond.legendaryFish[0]] * amount_caught)
            player.carryingCapacity -= amount_caught
            print(f"You caught {amount_caught} LEGENDARY {neighborhoodPond.legendaryFish[0]}!")
            print(f"You currently have enough space in your icebox for {player.carryingCapacity} more fish.")

        while True:
            try:
                response = input("Would you like to fish again? Yes or no?").strip().lower()

                if player.carryingCapacity == 0:
                    print(f"\nYou have to sell your fish before fishing again! Your icebox is full.")
                    sellingFish()
                elif response == "yes" or response == "y":
                    break
                elif response == "no" or response == "n":
                    print(f"Too bad! The rest of the game hasn't been programmed yet so you're fishing again WHETHER YOU LIKE IT OR NOT!!!")
                    break
            except ValueError:
                print("Invalid entry! Only enter yes or no!")

def sellingFish():
    while True:
        if player.fishInventory.count(neighborhoodPond.commonFish[0]) > 0:
            player.money += neighborhoodPond.commonFish_prize * neighborhoodPond.prizeMultiplier * player.fishInventory.count(neighborhoodPond.commonFish[0])
            print(f"You've sold {player.fishInventory.count(neighborhoodPond.commonFish[0])} Common {neighborhoodPond.commonFish[0]} for ${neighborhoodPond.commonFish_prize * neighborhoodPond.prizeMultiplier}!")

        if player.fishInventory.count(neighborhoodPond.uncommonFish[0]) > 0:
            player.money += neighborhoodPond.uncommonFish_prize * neighborhoodPond.prizeMultiplier * player.fishInventory.count(neighborhoodPond.uncommonFish[0])
            print(f"You've sold {player.fishInventory.count(neighborhoodPond.uncommonFish[0])} Uncommon {neighborhoodPond.uncommonFish[0]} for ${neighborhoodPond.uncommonFish_prize * neighborhoodPond.prizeMultiplier}!")

        if player.fishInventory.count(neighborhoodPond.uncommonFish[1]) > 0:
            player.money += neighborhoodPond.uncommonFish_prize * neighborhoodPond.prizeMultiplier * player.fishInventory.count(neighborhoodPond.uncommonFish[1])
            print(f"You've sold {player.fishInventory.count(neighborhoodPond.uncommonFish[1])} Uncommon {neighborhoodPond.uncommonFish[1]} for ${neighborhoodPond.uncommonFish_prize * neighborhoodPond.prizeMultiplier}!")

        if player.fishInventory.count(neighborhoodPond.rareFish[0]) > 0:
            player.money += neighborhoodPond.rareFish_prize * neighborhoodPond.prizeMultiplier * player.fishInventory.count(neighborhoodPond.rareFish[0])
            print(f"You've sold {player.fishInventory.count(neighborhoodPond.rareFish[0])} Rare {neighborhoodPond.rareFish[0]} for ${neighborhoodPond.rareFish_prize * neighborhoodPond.prizeMultiplier}!")

        if player.fishInventory.count(neighborhoodPond.rareFish[1]) > 0:
            player.money += neighborhoodPond.rareFish_prize * neighborhoodPond.prizeMultiplier * player.fishInventory.count(neighborhoodPond.rareFish[1])
            print(f"You've sold {player.fishInventory.count(neighborhoodPond.rareFish[1])} Rare {neighborhoodPond.rareFish[1]} for ${neighborhoodPond.rareFish_prize * neighborhoodPond.prizeMultiplier}!")

        if player.fishInventory.count(neighborhoodPond.legendaryFish[0]) > 0:
            player.money += neighborhoodPond.legendaryFish_prize * neighborhoodPond.prizeMultiplier * player.fishInventory.count(neighborhoodPond.legendaryFish[0])
            print(f"You've sold {player.fishInventory.count(neighborhoodPond.legendaryFish[0])} Legendary {neighborhoodPond.legendaryFish[0]} for ${neighborhoodPond.legendaryFish_prize * neighborhoodPond.prizeMultiplier}!")

        print(f"You currently have ${player.money} in total.")
        player.fishInventory = []
        player.carryingCapacity = default_capacity

        while True:
            try:
                response = input("You've finished selling and your icebox is empty. Would you like to fish again?").strip().lower()

                if response == "yes" or response == "y":
                    gameLoop()
                elif response == "no" or response == "n":
                    print(f"Too bad! The rest of the game hasn't been programmed yet so you're fishing again WHETHER YOU LIKE IT OR NOT!!!")
                    gameLoop()
            except ValueError:
                print("Invalid entry! Only enter yes or no!")

gameLoop()