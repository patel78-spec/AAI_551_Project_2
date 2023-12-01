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
        self.captain_objects = None
        self.possible_veggies = []
        self.score = 0

    # todo by cora
    def initVeggies(self):
        # continuously prompt to user for the name of veggie file until user provide non-empty string
        veggie_filename = ""
        while len(veggie_filename) == 0:
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

        # randomly initialize the NUMBEROFVEGGIES number of possible_veggies into the field
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
        pass

    # todo by cora
    def initRabbit(self):
        pass

    # todo by cora
    def initializeGame(self):
        pass

    # todo by cora
    def remainingVeggies(self):
        pass

    # todo by cora
    def printField(self):
        pass

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