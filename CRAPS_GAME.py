# For random numbers between 1 and 6
import random

class Player():
    def __init__(self, name):
        self.__name = name
        self.__score = 0

    def getName(self):
        return self.__name

    def update_Score(self, result):
        if result == "win":
            self.__score += 1
        elif result == "lose":
            if self.__score > 0:
                self.__score - +-1
            return result

    def getScore(self):  # Gets the score of the Player
        input(f" Press Enter to see your score")
        print(f" The Player Score is: {self.__score}")

    def reset_score(self):
        self.__score = 0
        return f" The Score is set back to 0"

class Dice:
    def __init__(self, numberOfSides):
        self.numberOfSides = numberOfSides

#self_numberofSides can be flexable with other dice object types

    def Roll(self):
        redRoll = random.randint(1, self.numberOfSides)
        blueRoll = random.randint(1, self.numberOfSides)
        dice_total = redRoll + blueRoll
        print(f" Red dice rolled: {redRoll}")
        print(f" Blue dice rolled: {blueRoll}\n")
        print(f" The total of the two dice is: {dice_total}\n")
        return dice_total


class PlayGame:

# dice object, only need one object

    dice = Dice(6)
    name = input(f" Please type your name: ")
    player1 = Player(name)
    print(f" Hello {name}! Welcome to the game of Craps! \n")

# the game goes on for 10 rolls
    for dice_turns in range(3):
        print(f"\n turn: {dice_turns + 1}")

        input(f" Press Enter to Roll the Dice!\n")  # gives a pause before the dice roll

        dice_total = dice.Roll()

# First rolls 7, 11 = win and then an update score. If rolls 2, 3, 12 = lose and then update score

        if dice_total in [7, 11]:
            print(f"\n First Roll was {dice_total}, {name} wins!\n")
            player1.update_Score("win")

        elif dice_total in [2, 3, 12]:
            print(f"\n First Roll was {dice_total}, {name} loses!\n")
            player1.update_Score("lose")

# Dice total become a point!

        elif dice_total in [4, 5, 6, 8, 9, 10]:
            point = dice_total
            print(f" First Roll was a {point}, {name} created a point!\n Watch out for 7 this time!\n")

# loop for the point roll

            while True:
                input(f"\n Press Enter to roll the dice!\n")

                dice_total = dice.Roll()
            

                if dice_total == point:
                    print(f" You rolled the {point}, you win!")
                    player1.update_Score("win")
                    break

                elif dice_total == 7:
                    print(f" {name} rolled a 7, {name} Loses!!")
                    player1.update_Score("lose")
                    break

                else:
                    point != dice_total
                    print(f" Rolled a {dice_total}! Keep Rolling!!")
                    
    player1.getScore()   
PlayGame()


