# todo 
# Authors: Gai Li Ho, Dhruv Patel
# Date:
# Description:

import os
import random
import pickle
from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit

class GameEngine:
    NUMBEROFVEGGIES = 30
    NUMBEROFRABBITS = 5
    HIGHSCOREFILE = 'highscore.data'


    # todo constructor by cora
    def __init__(self):
        self.field = []
        self.rabbits_in_filed = []
        self.captain = None
        self.possible_veggies = []
        self.score = 0


    # todo by cora
    def initVeggies(self):
        # continuously prompt to user for the name of veggie file until user provide non-empty string
        veggie_filename = ""
        while veggie_filename == "":
            veggie_filename = input("Please enter the name of the vegetable point file: ").strip()

        # continuously prompt to user for the valid name of veggie file until the file name does exist in the path
        while not os.path.exist(veggie_filename):
            veggie_filename = input(f"{veggie_filename} does not exist, please enter a valid name of the vegetable point file: ")
        # open the file in read mode
        veggie_file = open(veggie_filename, "r")

        # read the first line of the file to initialize the field list
        field_size = veggie_file.readline().strip().split(",")
        # initialize the field basd on the information in field_size
        self.field =[[None for i in range(field_size[2])] for j in range(field_size[1])]

        # read left lines to initialize the possible_veggie list
        line = veggie_file.readline().strip().split(",")
        while len(line) > 0:
            # initialize the Veggie object based on information in line
            v1 = Veggie(line[0], line[1], line[2])
            # add the Veggie object into possible_veggies list
            self.possible_veggies.append(v1)
            # read the next line
            line = veggie_file.readline().strip().split(",")

        # randomly initialize the {NUMBEROFVEGGIES} number of possible_veggies into the field
        veggies_plant = []
        for i in range(self.NUMBEROFVEGGIES):
            # get a random number between 0 and the size of possible_veggies -1, inclusively
            random_no = random.randint(0, len(self.possible_veggies)-1)
            # get the symbol of the Veggie object and add it to veggies_plant
            veggies_plant.append(self.possible_veggies[random_no].getSymbol())

        # plant these vegetables into fields at a random position
        for v in veggies_plant:
            # get a random number between 0 and x-axis of the field for x position
            x = random.randint(0, field_size[2]-1)
            # get a random number between 0 and y-axis of the field for y position
            y = random.randint(0, field_size[1]-1)
            # continuously generate random x and y until the (x,y) position is not None
            while self.field[x][y] is not None:
                # get the random x y position again
                x = random.randint(0, field_size[2] - 1)
                y = random.randint(0, field_size[1] - 1)
            # put the Veggie symbol into the (x, y) position
            self.field[x][y] = v

        # close the file
        veggie_file.close()


    # todo by cora
    def initCaptain(self):
        # choose a random position for captain
        # get a random number between 0 and x-axis of the field for x position
        x = random.randint(0, len(self.field) - 1)
        # get a random number between 0 and y-axis of the field for y position
        y = random.randint(0, len(self.field[0]) - 1)
        # continuously generate random x and y until the (x,y) position is not None
        while self.field[x][y] is not None:
            # get the random x y position again
            x = random.randint(0, len(self.field) - 1)
            y = random.randint(0, len(self.field[0]) - 1)
        # initialize the captain object
        self.captain = Captain(x, y)
        # put the captain symbol into field
        self.field[x][y] = "V"


    # todo by cora
    def initRabbit(self):
        # arrange the {NUMBEROFRABBITS} number of rabbits into the field
        for i in range(self.NUMBEROFRABBITS):
            # get a random number between 0 and x-axis of the field for x position
            x = random.randint(0, len(self.field) - 1)
            # get a random number between 0 and y-axis of the field for y position
            y = random.randint(0, len(self.field[0]) - 1)
            # continuously generate random x and y until the (x,y) position is not None
            while self.field[x][y] is not None:
                # get the random x y position again
                x = random.randint(0, len(self.field) - 1)
                y = random.randint(0, len(self.field[0]) - 1)
            # put the Rabbit symbol into the (x, y) position
            self.field[x][y] = "R"
            # initialize a Rabbit object
            r1 = Rabbit(x, y)
            # and put it into Rabbits_in_field list
            self.rabbits_in_filed.append(r1)


    # todo by cora
    def initializeGame(self):
        # calling initialization methods
        self.initVeggies()
        self.initCaptain()
        self.initRabbit()


    # todo by cora
    def remainingVeggies(self):
        # variable to save how mang vegetables in the field
        count_veggies = 0
        # iterate the filed
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                # when the current location is not neither rabbit nor captain nor none
                if self.field[i][j] != "R" and self.field[i][j] != "V" and self.field[i][j] is not None:
                    # increase count_veggies by 1
                    count_veggies += 1
        return count_veggies


    # todo by cora
    def intro(self):
        # print welcome
        print("Welcome to Captain Veggie!")
        # explain the game
        print("The rabbits have invaded your garden and you must harvest "
              "as many vegetables as possible before the rabbits eat them "
              "all! Each vegetable is worth a different number of points"
              "so go for the high score!\n")

        # list all possible vegetables in the field
        print("The vegetables are:")
        for v in self.possible_veggies:
            # print the information of vegetable one by one
            print(f"{v.getSymbol()}: {v.getName()} {v.getPoint()} points")

        # print the symbol for captain and rabbits
        print("\nCaptain Veggie is V, and the rabbits are R's.\n")
        print("Good luck!")


    # todo by cora
    def printField(self):
        remaining_veggies = self.remainingVeggies()
        # print remaining vegetables in the field, and total score user gets so far
        print(f"{remaining_veggies} veggies remaining. Current score: {self.score}")
        width = 2*len(self.field)+2

        # print up border
        for i in range(width):
            print("#")
        # print the field line by line
        for i in range(len(self.field)):
            # print the left border
            print("#", end="")
            for j in range(len(self.field[0])):
                print(f" {self.field[i][j]}", end=" ")
            # print right border
            print("#\n")
        # print lower border
        for i in range(width):
            print("#")

    # todo by dhruv
    def getScore(self):
        return self.score

    # todo by dhruv
    def moveRabbits(self):
        pass

    # todo by dhruv
    def moveCptVertical(self):
        pass

    # todo by dhruv
    def moveCptHorizontal(self):
        pass

    # todo by dhruv
    def moveCaptain(self):
        pass

    # todo by dhruv
    def gameOver(self):
        pass

    # todo by dhruv
    def highScore(self):
        pass