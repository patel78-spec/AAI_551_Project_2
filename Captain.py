# Authors: Gai Li Ho, Dhruv Patel
# Date: 12/05/2023
# Description: This is the captain class

from Creature import Creature


class Captain(Creature):

    def __init__(self, x, y):
        """Constructor for captain

        Args:
            x (int): x-cordinate
            y (int): y-cordinate
        """
        Creature.__init__(self, x, y, "V")
        self.__allVeggies = []


    def addVeggie(self, veggie):
        self.__allVeggies.append(veggie)

    def getAllVeggies(self):
        return self.__allVeggies

    def setAllVeggies(self, newVeggieList):
        self.__allVeggies = newVeggieList
