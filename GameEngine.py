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
from Snake import Snake

class GameEngine:
    NUMBEROFVEGGIES = 30
    NUMBEROFRABBITS = 5
    HIGHSCOREFILE = 'highscore.data'


    # todo constructor by cora
    def __init__(self):
        self.field = []
        self.field_size = None
        self.rabbits_in_filed = []
        self.captain = None
        self.possible_veggies = []
        self.score = 0
        self.snake = None
    
    def __get_random_coordinates(self):
        # get a random number between 0 and x-axis of the field for x position
        x = random.randint(0, self.field_size[0] - 1)
        # get a random number between 0 and y-axis of the field for y position
        y = random.randint(0, self.field_size[1] - 1)
        # continuously generate random x and y until the (x,y) position is not None
        while self.field[x][y] is not None:
            # get the random x y position again
            x = random.randint(0, self.field_size[0] - 1)
            y = random.randint(0, self.field_size[1] - 1)
        return x, y
        


    # todo by cora
    def initVeggies(self):
        # continuously prompt to user for the name of veggie file until user provide non-empty string
        veggie_filename = ""
        while veggie_filename == "":
            veggie_filename = input("Please enter the name of the vegetable point file: ").strip()

        # continuously prompt to user for the valid name of veggie file until the file name does exist in the path
        while not os.path.exists(veggie_filename):
            veggie_filename = input(f"{veggie_filename} does not exist, please enter a valid name of the vegetable point file: ")
        # open the file in read mode
        veggie_file = open(veggie_filename, "r")

        # read the first line of the file to initialize the field list
        self.field_size = list(map(int,veggie_file.readline().strip().split(",")[1:]))
        # initialize the field basd on the information in field_size
        self.field =[[None for i in range(self.field_size[1])] for j in range(self.field_size[0])]

        # read left lines to initialize the possible_veggie list
        line = veggie_file.readline().strip().split(",")
        while len(line) > 1:
            # initialize the Veggie object based on information in line
            # add the Veggie object into possible_veggies list
            self.possible_veggies.append(Veggie(line[0], line[1], int(line[2])))
            # read the next line
            line = veggie_file.readline().strip().split(",")

        # randomly initialize the {NUMBEROFVEGGIES} number of possible_veggies into the field
        veggies_plant = []
        for i in range(self.NUMBEROFVEGGIES):
            # get a random number between 0 and the size of possible_veggies -1, inclusively
            random_no = random.randint(0, len(self.possible_veggies)-1)
            # get the symbol of the Veggie object and add it to veggies_plant
            veggies_plant.append(self.possible_veggies[random_no])

        # plant these vegetables into fields at a random position
        for v in veggies_plant:
            x, y = self.__get_random_coordinates()
            # put the Veggie symbol into the (x, y) position
            self.field[x][y] = v

        # close the file
        veggie_file.close()


    # todo by cora
    def initCaptain(self):
        # choose a random position for captain
        x, y = self.__get_random_coordinates()
        # initialize the captain object
        self.captain = Captain(x, y)
        # put the captain symbol into field
        self.field[x][y] = self.captain


    # todo by cora
    def initRabbit(self):
        # arrange the {NUMBEROFRABBITS} number of rabbits into the field
        for i in range(self.NUMBEROFRABBITS):
            x, y = self.__get_random_coordinates()
            # initialize a Rabbit object
            r1 = Rabbit(x, y)
            # put the Rabbit symbol into the (x, y) position
            self.field[x][y] = r1
            # and put it into Rabbits_in_field list
            self.rabbits_in_filed.append(r1)
    
    def initSnake(self):
        # choose a random position for captain
        x, y = self.__get_random_coordinates()
        # initialize the captain object
        self.snake = Snake(x, y)
        # put the captain symbol into field
        self.field[x][y] = self.snake


    # todo by cora
    def initializeGame(self):
        # calling initialization methods
        self.initVeggies()
        self.initCaptain()
        self.initRabbit()
        self.initSnake()


    # todo by cora
    def remainingVeggies(self):
        # variable to save how mang vegetables in the field
        count_veggies = 0
        # iterate the filed
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                # when the current location is not neither rabbit nor captain nor none
                if self.field[i][j] is not None and self.field[i][j].getInhabitant() != "R" and self.field[i][j].getInhabitant() != "V" and self.field[i][j].getInhabitant() != "S":
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
            print(v)

        # print the symbol for captain and rabbits
        print("\nCaptain Veggie is V, and the rabbits are R's.\n")
        print("Good luck!")


    # todo by cora
    def printField(self):
        remaining_veggies = self.remainingVeggies()
        # print remaining vegetables in the field, and total score user gets so far
        print(f"{remaining_veggies} veggies remaining. Current score: {self.score}")
        width = 3*len(self.field)+4

        # print up border
        for i in range(width):
            print("#",end="")
        print()
        # print the field line by line
        for i in range(len(self.field)):
            # print the left border
            print("#  ", end="")
            for j in range(len(self.field[0])):
                if self.field[i][j]:
                    print(f"{self.field[i][j].getInhabitant()}", end="  ")
                else:
                    print(" ",end = "  ")
            # print right border
            print("#")
        # print lower border
        for i in range(width):
            print("#",end="")

    # todo by dhruv
    def getScore(self):
        return self.score
    
    def __check_move(self,x,y):
        return x >= self.field_size[0] or x < 0 or y >= self.field_size[1] or y < 0
        

    # todo by dhruv
    def moveRabbits(self):
        for r in self.rabbits_in_filed:
            x,y = r.getX(), r.getY()
            p = [(x,y),(x,y+1),(x,y-1),(x+1,y),(x,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)]
            p = random.sample(p,1)[0]
            if p == (x,y):
                continue
            if not self.__check_move(*p):
                if not self.field[p[0]][p[1]]:
                    r.setX(p[0])
                    r.setY(p[1])
                    self.field[p[0]][p[1]] = r
                    self.field[x][y] = None
                # elif self.field[p[0]][p[1]].getInhabitant() != "V" and self.field[p[0]][p[1]].getInhabitant() != "R" and self.field[p[0]][p[1]].getInhabitant() != "S":
                elif type(self.field[p[0]][p[1]]) is Veggie:    
                    r.setX(p[0])
                    r.setY(p[1])
                    self.field[p[0]][p[1]] = r
                    self.field[x][y] = None
    
    def moveSnake(self):
        v_x, v_y = self.captain.getX(), self.captain.getY()
        s_x, s_y = self.snake.getX(), self.snake.getY()
        d_x, d_y = s_x - v_x, s_y - v_y
        p = (s_x - int((d_x) / abs(d_x)), s_y) if abs(d_x) > abs(d_y) else (s_x, s_y - int((d_y) / abs(d_y)))
        if not self.field[p[0]][p[1]]:
            self.snake.setX(p[0])
            self.snake.setY(p[1])
            self.field[p[0]][p[1]] = self.snake
            self.field[s_x][s_y] = None
        elif self.field[p[0]][p[1]].getInhabitant() == "V":
            print("Oops! The Snake bite you. You lost last 5 Veggies")
            veggies = self.captain.getAllVeggies()[:-5]
            self.score = 0
            self.captain.setAllVeggies(veggies)
            for v in veggies:
                self.score += v.getPoint()
            self.field[s_x][s_y] = None
            self.initSnake()

    # todo by dhruv
    def moveCptVertical(self,up=True):
        x,y = self.captain.getX(),self.captain.getY()
        if up:
            if self.field[x-1][y] and self.field[x-1][y].getInhabitant() == 'R':
                print("Don't step on the bunnies!")
                return
            else:
                if self.field[x-1][y] and type(self.field[x-1][y]) is Veggie:
                    self.captain.addVeggie(self.field[x-1][y])
                    self.score += self.field[x-1][y].getPoint()
                    print(f"Yummy! A delicious {self.field[x-1][y].getName()}")
                self.captain.setX(x-1)
                self.captain.setY(y)
                self.field[x-1][y] = self.captain
                self.field[x][y] = None
        else:
            if self.field[x+1][y] and self.field[x+1][y].getInhabitant() == 'R':
                print("Don't step on the bunnies!")
                return
            else:
                if self.field[x+1][y] and type(self.field[x+1][y]) is Veggie:
                    self.captain.addVeggie(self.field[x+1][y])
                    self.score += self.field[x+1][y].getPoint()
                    print(f"Yummy! A delicious {self.field[x+1][y].getName()}")
                self.captain.setX(x+1)
                self.captain.setY(y)
                self.field[x+1][y] = self.captain
                self.field[x][y] = None
        

    # todo by dhruv
    def moveCptHorizontal(self,left=True):
        x,y = self.captain.getX(),self.captain.getY()
        if left:
            if self.field[x][y-1] and self.field[x][y-1].getInhabitant() == 'R':
                print("Don't step on the bunnies!")
                return
            else:
                if self.field[x][y-1] and type(self.field[x][y-1]) is Veggie:
                    self.captain.addVeggie(self.field[x][y-1])
                    self.score += self.field[x][y-1].getPoint()
                    print(f"Yummy! A delicious {self.field[x][y-1].getName()}")
                self.captain.setX(x)
                self.captain.setY(y-1)
                self.field[x][y-1] = self.captain
                self.field[x][y] = None
        else:
            if self.field[x][y+1] and self.field[x][y+1].getInhabitant() == 'R':
                print("Don't step on the bunnies!")
                return
            else:
                if self.field[x][y+1] and type(self.field[x][y+1]) is Veggie:
                    self.captain.addVeggie(self.field[x][y+1])
                    self.score += self.field[x][y+1].getPoint()
                    print(f"Yummy! A delicious {self.field[x][y+1].getName()}")
                self.captain.setX(x)
                self.captain.setY(y+1)
                self.field[x][y+1] = self.captain
                self.field[x][y] = None

    # todo by dhruv
    def moveCaptain(self):
        move = input("\nWould you like to move up(W), down(S), left(A), or right(D): ").lower()
        if move == 'w':
            if self.captain.getX() - 1 < 0:
                print("You can't move that way!")
            else:
                self.moveCptVertical(True)
        elif move == 's':
            if self.captain.getX() + 1 >= self.field_size[0]:
                print("You can't move that way!")
            else:
                self.moveCptVertical(False)
        elif move == 'a':
            if self.captain.getY() - 1 < 0:
                print("You can't move that way!")
            else:
                self.moveCptHorizontal(True)
        elif move == 'd':
            if self.captain.getY() + 1 >= self.field_size[1]:
                print("You can't move that way!")
            else:
                self.moveCptHorizontal(False)
        else:
            print(f"{move} is not a valid option")

    # todo by dhruv
    def gameOver(self):
        print("Game Over")
        print("You managed to harvest the following vegetables:")
        for v in self.captain.getAllVeggies():
            print(v.getName())
        print(f"Your score was: {self.score}")

    # todo by dhruv
    def highScore(self):
        initials = input("Please enter your three initials to go on the scoreboard: ").upper()[:3]
        print("HIGH SCORES")
        print("Name\tScore")
        high_score_list = []
        if not os.path.exists(self.HIGHSCOREFILE):
            high_score_list.append((initials,self.score))
            with open(self.HIGHSCOREFILE,"wb") as f:
                pickle.dump(high_score_list,f)
            print(f"{initials}\t{self.score}")
            return
        
        with open(self.HIGHSCOREFILE,"rb") as f:
            high_score_list = pickle.load(f)
        
        for i,data in enumerate(high_score_list):
            if data[1] < self.score:
                break
        
        high_score_list.insert(i, (initials,self.score))
        
        for data in high_score_list:
            print(f"{data[0]}\t{data[1]}")
        
        with open(self.HIGHSCOREFILE, "wb") as f:
            pickle.dump(high_score_list,f)
            
        