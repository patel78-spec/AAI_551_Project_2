# todo 
# Authors: Gai Li Ho, Dhruv Patel
# Date:
# Description:

from Creature import Creature


class Captain(Creature):

    def __init__(self, x, y):
        Creature.__init__("V", x, y)
        self.__allVeggies = []


    def addVeggie(self, veggie):
        self.__allVeggies.append(veggie)

    def getAllVeggies(self):
        return self.__allVeggies

    def setAllVeggies(self, newVeggieList):
        self.__allVeggies = newVeggieList
