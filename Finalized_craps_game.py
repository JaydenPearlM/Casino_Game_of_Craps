# For random numbers between 1 and 6
import random


class Player:
    def __init__(self, name):
        self.__name = name
        self.__score = 0

    def getName(self):
        return self.__name

    # took out losing a point
    def update_Score(self, result):
        self.__score += 1

    # removed logic from getScore, does not need to interact with user
    def getScore(self):
        return self.__score


class Dice:
    def __init__(self, numberOfSides):
        self.numberOfSides = numberOfSides

    # self_numberofSides can be flexable with other dice object types

    def Roll(self):
        redRoll = random.randint(1, self.numberOfSides)
        blueRoll = random.randint(1, self.numberOfSides)
        dice_total = redRoll + blueRoll
        print(f" Red dice rolled: {redRoll}")
        print(f" Blue dice rolled: {blueRoll}\n")
        print(f" The total of the two dice is: {dice_total}\n")
        return dice_total


def play_again():

    while True:
        answer = input(" Do you want to play another round? (y/n): ").lower().strip()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print(f" Please enter 'y' or 'n'")


def main():

    dice = Dice(6)
    name = input(" Please type your name: ")
    player1 = Player(name)
    print(f"\n Hello {name}!! Welcome to the game of Craps!!\n")

    dice_turns = 0

    while True:
        dice_turns += 1
        print(f" \n turn {dice_turns}")
        input(f" Press enter to roll the Dice!\n")
        dice_total = dice.Roll()

        if dice_total in [7, 11]:
            print(f"\n First Roll was {dice_total}, {name} wins!\n")
            player1.update_Score("win")
            if not play_again():
                print(f"\n{name}, your final score is: {player1.getScore()}")
                input("Press Enter to Exit.")
                breaK

        # Took out the losing score
        elif dice_total in [2, 3, 12]:
            print(f"\n First Roll was {dice_total}, {name} loses!\n")

        # Dice total become a point!

        elif dice_total in [4, 5, 6, 8, 9, 10]:
            point = dice_total
            print(f" First Roll was a {point}, {name} created a point!")

        # Dice Point rolls

        while True:

            input(f"\n Press Enter to roll the dice again!\n")
            dice_total = dice.Roll()

            if dice_total == point:
                print(f" You rolled the {point}, you win!")
                player1.update_Score("win")
                if not play_again():
                    print(f"\n{name}, your final score is: {player1.getScore()}")
                    print("Press Enter to Exit")
                    return
                else:
                    break

            elif dice_total == 7:
                print(f" {name} rolled a 7, {name} Loses!!")
                if not play_again():
                    print(f"\n{name}, your final score is: {player1.getScore()}")
                    input("press Enter to Exit.")
                    return
                else:
                    break

            else:
                print(f" Rolled a {dice_total}! Keep Rolling!!")


if __name__ == "__main__":
    main()
