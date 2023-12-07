# Authors: Gai Li Ho, Dhruv Patel
# Date: 12/05/2023
# Description:

from Creature import Creature


class Snake(Creature):


    def __init__(self, x, y):
        Creature.__init__(self, x, y, "S")
