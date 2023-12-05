# todo 
# Authors: Gai Li Ho, Dhruv Patel
# Date:
# Description:

from Creature import Creature


class Rabbit(Creature):


    def __init__(self, x, y):
        Creature.__init__(self, x, y, "R")
