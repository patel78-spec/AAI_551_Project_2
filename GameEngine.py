# Authors: Gai Li Ho, Dhruv Patel
# Date: 12/05/2023
# Description: This is the gameengine class

import os
import random
import pickle
from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit
from Snake import Snake

class GameEngine:

    __NUMBEROFVEGGIES = 30
    __NUMBEROFRABBITS = 5
    __HIGHSCOREFILE = 'highscore.data'


    # todo constructor by cora
    def __init__(self):
        """This is the constructor class
        """
        self.__field = []
        self.__field_size = None
        self.__rabbits_in_filed = []
        self.__captain = None
        self.__possible_veggies = []
        self.__score = 0
        self.__snake = None
    
    def __get_random_coordinates(self):
        # get a random number between 0 and x-axis of the field for x position
        x = random.randint(0, self.__field_size[0] - 1)
        # get a random number between 0 and y-axis of the field for y position
        y = random.randint(0, self.__field_size[1] - 1)
        # continuously generate random x and y until the (x,y) position is not None
        while self.__field[x][y] is not None:
            # get the random x y position again
            x = random.randint(0, self.__field_size[0] - 1)
            y = random.randint(0, self.__field_size[1] - 1)
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
        self.__field_size = list(map(int,veggie_file.readline().strip().split(",")[1:]))
        # initialize the field basd on the information in field_size
        self.__field =[[None for i in range(self.__field_size[1])] for j in range(self.__field_size[0])]

        # read left lines to initialize the possible_veggie list
        line = veggie_file.readline().strip().split(",")
        while len(line) > 1:
            # initialize the Veggie object based on information in line
            # add the Veggie object into possible_veggies list
            self.__possible_veggies.append(Veggie(line[0], line[1], int(line[2])))
            # read the next line
            line = veggie_file.readline().strip().split(",")

        # randomly initialize the {__NUMBEROFVEGGIES} number of possible_veggies into the field
        veggies_plant = []
        for i in range(self.__NUMBEROFVEGGIES):
            # get a random number between 0 and the size of possible_veggies -1, inclusively
            random_no = random.randint(0, len(self.__possible_veggies)-1)
            # get the symbol of the Veggie object and add it to veggies_plant
            veggies_plant.append(self.__possible_veggies[random_no])

        # plant these vegetables into fields at a random position
        for v in veggies_plant:
            x, y = self.__get_random_coordinates()
            # put the Veggie symbol into the (x, y) position
            self.__field[x][y] = v

        # close the file
        veggie_file.close()


    # todo by cora
    def initCaptain(self):
        # choose a random position for captain
        x, y = self.__get_random_coordinates()
        # initialize the captain object
        self.__captain = Captain(x, y)
        # put the captain symbol into field
        self.__field[x][y] = self.__captain


    # todo by cora
    def initRabbit(self):
        # arrange the {__NUMBEROFRABBITS} number of rabbits into the field
        for i in range(self.__NUMBEROFRABBITS):
            x, y = self.__get_random_coordinates()
            # initialize a Rabbit object
            r1 = Rabbit(x, y)
            # put the Rabbit symbol into the (x, y) position
            self.__field[x][y] = r1
            # and put it into Rabbits_in_field list
            self.__rabbits_in_filed.append(r1)
    
    def initSnake(self):
        if not self.__snake:
            snake_check = input("Do you want a snake in your game Yes(y) or No(n): ").lower()
        if self.__snake or snake_check == 'y':
            # choose a random position for captain
            x, y = self.__get_random_coordinates()
            # initialize the captain object
            self.__snake = Snake(x, y)
            # put the captain symbol into field
            self.__field[x][y] = self.__snake


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
        for i in range(len(self.__field)):
            for j in range(len(self.__field[0])):
                # when the current location is not neither rabbit nor captain nor none
                if self.__field[i][j] is not None and self.__field[i][j].getInhabitant() != "R" and self.__field[i][j].getInhabitant() != "V" and self.__field[i][j].getInhabitant() != "S":
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
        for v in self.__possible_veggies:
            # print the information of vegetable one by one
            print(v)

        # print the symbol for captain and rabbits
        print("\nCaptain Veggie is V, and the rabbits are R's.")
        if self.__snake:
            print("Snake is S.\n")
        print("Good luck!")


    # todo by cora
    def printField(self):
        remaining_veggies = self.remainingVeggies()
        # print remaining vegetables in the field, and total score user gets so far
        print(f"{remaining_veggies} veggies remaining. Current score: {self.__score}")
        width = 3*len(self.__field)+4

        # print up border
        for i in range(width):
            print("#",end="")
        print()
        # print the field line by line
        for i in range(len(self.__field)):
            # print the left border
            print("#  ", end="")
            for j in range(len(self.__field[0])):
                if self.__field[i][j]:
                    print(f"{self.__field[i][j].getInhabitant()}", end="  ")
                else:
                    print(" ",end = "  ")
            # print right border
            print("#")
        # print lower border
        for i in range(width):
            print("#",end="")

    # todo by dhruv
    def getScore(self):
        """this functions returns the score

        Returns:
            int: current score
        """
        return self.__score
    
    def __check_move(self,x,y):
        """check if the random movement for rabbit is inside the bounds

        Args:
            x (int): x-cordinate
            y (int): y-cordinate

        Returns:
            Boolean: True or False
        """
        return x >= self.__field_size[0] or x < 0 or y >= self.__field_size[1] or y < 0
        

    # todo by dhruv
    def moveRabbits(self):
        """This function is used to move the rabbits
        """
        for r in self.__rabbits_in_filed:
            x,y = r.getX(), r.getY()
            p = [(x,y),(x,y+1),(x,y-1),(x+1,y),(x,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)]
            p = random.sample(p,1)[0]
            # if random selected movement comes out to be same then rabbit doesn't move
            if p == (x,y):
                continue
            if not self.__check_move(*p):
                if not self.__field[p[0]][p[1]]:
                    r.setX(p[0])
                    r.setY(p[1])
                    self.__field[p[0]][p[1]] = r
                    self.__field[x][y] = None
                # elif self.__field[p[0]][p[1]].getInhabitant() != "V" and self.__field[p[0]][p[1]].getInhabitant() != "R" and self.__field[p[0]][p[1]].getInhabitant() != "S":
                elif type(self.__field[p[0]][p[1]]) is Veggie:    
                    r.setX(p[0])
                    r.setY(p[1])
                    self.__field[p[0]][p[1]] = r
                    self.__field[x][y] = None
    
    def moveSnake(self):
        """this function is used to move the snake
        """
        if self.__snake:
            v_x, v_y = self.__captain.getX(), self.__captain.getY()
            s_x, s_y = self.__snake.getX(), self.__snake.getY()
            d_x, d_y = s_x - v_x, s_y - v_y
            # which movement will make the sanke closer to the captain
            p = (s_x - int((d_x) / abs(d_x)), s_y) if abs(d_x) > abs(d_y) else (s_x, s_y - int((d_y) / abs(d_y)))
            if not self.__field[p[0]][p[1]]:
                self.__snake.setX(p[0])
                self.__snake.setY(p[1])
                self.__field[p[0]][p[1]] = self.__snake
                self.__field[s_x][s_y] = None
            elif self.__field[p[0]][p[1]].getInhabitant() == "V":
                print("Oops! The Snake bite you. You lost last 5 Veggies")
                veggies = self.__captain.getAllVeggies()[:-5]
                self.__score = 0
                self.__captain.setAllVeggies(veggies)
                for v in veggies:
                    self.__score += v.getPoint()
                self.__field[s_x][s_y] = None
                self.initSnake()

    # todo by dhruv
    def moveCptVertical(self,up=True):
        """This function is used to move the captain in vertical directions

        Args:
            up (bool, optional): _description_. Defaults to True.
        """
        x,y = self.__captain.getX(),self.__captain.getY()
        if up:
            if self.__field[x-1][y] and self.__field[x-1][y].getInhabitant() == 'R':
                print("Don't step on the bunnies!")
                return
            elif self.__field[x-1][y] and self.__field[x-1][y].getInhabitant() == 'S':
                print("There is a snake!!!")
                return
            else:
                if self.__field[x-1][y] and type(self.__field[x-1][y]) is Veggie:
                    self.__captain.addVeggie(self.__field[x-1][y])
                    self.__score += self.__field[x-1][y].getPoint()
                    print(f"Yummy! A delicious {self.__field[x-1][y].getName()}")
                self.__captain.setX(x-1)
                self.__captain.setY(y)
                self.__field[x-1][y] = self.__captain
                self.__field[x][y] = None
        else:
            if self.__field[x+1][y] and self.__field[x+1][y].getInhabitant() == 'R':
                print("Don't step on the bunnies!")
                return
            elif self.__field[x+1][y] and self.__field[x+1][y].getInhabitant() == 'S':
                print("There is a snake!!!")
                return
            else:
                if self.__field[x+1][y] and type(self.__field[x+1][y]) is Veggie:
                    self.__captain.addVeggie(self.__field[x+1][y])
                    self.__score += self.__field[x+1][y].getPoint()
                    print(f"Yummy! A delicious {self.__field[x+1][y].getName()}")
                self.__captain.setX(x+1)
                self.__captain.setY(y)
                self.__field[x+1][y] = self.__captain
                self.__field[x][y] = None
        

    # todo by dhruv
    def moveCptHorizontal(self,left=True):
        """Used to move the captain in horizontal direction

        Args:
            left (bool, optional): _description_. Defaults to True.
        """
        x,y = self.__captain.getX(),self.__captain.getY()
        if left:
            if self.__field[x][y-1] and self.__field[x][y-1].getInhabitant() == 'R':
                print("Don't step on the bunnies!")
                return
            elif self.__field[x][y-1] and self.__field[x][y-1].getInhabitant() == 'S':
                print("There is a snake!!!")
                return
            else:
                # checking for veggie
                if self.__field[x][y-1] and type(self.__field[x][y-1]) is Veggie:
                    self.__captain.addVeggie(self.__field[x][y-1])
                    self.__score += self.__field[x][y-1].getPoint()
                    print(f"Yummy! A delicious {self.__field[x][y-1].getName()}")
                self.__captain.setX(x)
                self.__captain.setY(y-1)
                self.__field[x][y-1] = self.__captain
                self.__field[x][y] = None
        else:
            if self.__field[x][y+1] and self.__field[x][y+1].getInhabitant() == 'R':
                print("Don't step on the bunnies!")
                return
            elif self.__field[x][y+1] and self.__field[x][y+1].getInhabitant() == 'S':
                print("There is a snake!!!")
                return
            else:
                if self.__field[x][y+1] and type(self.__field[x][y+1]) is Veggie:
                    self.__captain.addVeggie(self.__field[x][y+1])
                    self.__score += self.__field[x][y+1].getPoint()
                    print(f"Yummy! A delicious {self.__field[x][y+1].getName()}")
                self.__captain.setX(x)
                self.__captain.setY(y+1)
                self.__field[x][y+1] = self.__captain
                self.__field[x][y] = None

    # todo by dhruv
    def moveCaptain(self):
        """This function takes the input from the player for the movement of captain. 
            If movement is inside the bound it will call the appropriate movement function
        """
        move = input("\nWould you like to move up(W), down(S), left(A), or right(D): ").lower()
        if move == 'w':
            if self.__captain.getX() - 1 < 0:
                print("You can't move that way!")
            else:
                self.moveCptVertical(True)
        elif move == 's':
            if self.__captain.getX() + 1 >= self.__field_size[0]:
                print("You can't move that way!")
            else:
                self.moveCptVertical(False)
        elif move == 'a':
            if self.__captain.getY() - 1 < 0:
                print("You can't move that way!")
            else:
                self.moveCptHorizontal(True)
        elif move == 'd':
            if self.__captain.getY() + 1 >= self.__field_size[1]:
                print("You can't move that way!")
            else:
                self.moveCptHorizontal(False)
        else:
            print(f"{move} is not a valid option")

    # todo by dhruv
    def gameOver(self):
        """This if the function for when the game ends
        """
        print("Game Over")
        print("You managed to harvest the following vegetables:")
        for v in self.__captain.getAllVeggies():
            print(v.getName())
        print(f"Your score was: {self.__score}")

    # todo by dhruv
    def highScore(self):
        """This function is used to sabve the highscore.
        """
        initials = input("Please enter your three initials to go on the scoreboard: ").upper()[:3]
        print("HIGH SCORES")
        print("Name\tSnake\tScore")
        high_score_list = []
        if not os.path.exists(self.__HIGHSCOREFILE):
            high_score_list.append((initials,'Yes' if self.__snake else 'No',self.__score))
            with open(self.__HIGHSCOREFILE,"wb") as f:
                pickle.dump(high_score_list,f)
            print(f"{initials}\t{'Yes' if self.__snake else 'No'}\t{self.__score}")
            return
        
        with open(self.__HIGHSCOREFILE,"rb") as f:
            high_score_list = pickle.load(f)
        
        high_score_list.append((initials,'Yes' if self.__snake else 'No',self.__score))    
        # sorting the highscore in des=cending order
        high_score_list = sorted(high_score_list, key=lambda x: x[2],reverse=True)
        
        for data in high_score_list:
            print(f"{data[0]}\t{data[1]}\t{data[2]}")
        
        with open(self.__HIGHSCOREFILE, "wb") as f:
            pickle.dump(high_score_list,f)
            
        