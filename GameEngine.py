# todo 
# Authors: {Your Name}, Dhruv Patel
# Date:
# Description:

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
    pass
  
  # todo by cora
  def initVeggies():
    pass
  
  # todo by cora
  def initCaptain():
    pass
  
  # todo by cora
  def initRabbit():
    pass
  
  # todo by cora
  def initializeGame():
    pass
  
  # todo by cora
  def remainingVeggies():
    pass
  
  # todo by cora
  def printField():
    pass
  
  # todo by dhruv
  def getScore(self):
    return self.score
  
  # todo by dhruv
  def moveRabbits(self):
    for rabbit in self._rabbits:
      directions = [[0,0], [0,1], [0, -1], [-1, 0], [1,0], [-1, 1], [1, 1], [-1, -1], [1, -1]]
      new_direction = random.randint(0, len(directions)-1)
      
      rabbit_x = rabbit.getX()
      rabbit_y = rabbit.getY()
      rabbit_x += new_direction[0]
      rabbit_y += new_direction[1]
      
      rabbit.setX(rabbit_x)
      rabbit.setY(rabbit_y)
    pass
  
  # todo by dhruv
  def moveCptVertical():
    pass
  
  # todo by dhruv
  def moveCptHorizontal():
    pass
  
  # todo by dhruv
  def moveCaptain():
    pass
  
  # todo by dhruv
  def gameOver():
    pass
  
  # todo by dhruv
  def highScore():
    pass