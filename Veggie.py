# todo 
# Authors: Gai Li Ho, Dhruv Patel
# Date:
# Description:

from FieldInhabitant import FieldInhabitant


class Veggie(FieldInhabitant):

    def __init__(self, name, symbol, point):
        # call the init method in FieldInhabitant with Veggie text symbol
        FieldInhabitant.__init__(self,symbol)
        self.__name = name
        self.__symbol = symbol
        self.__point = point

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName


    def getSymbol(self):
        return self.__symbol


    def setSymbol(self, newSymbol):
        self.__symbol = newSymbol


    def getPoint(self):
        return self.__point

    def setPoint(self, newPoint):
        self.__point = newPoint


    def __str__(self):
        return f"{self.__symbol}: {self.__name} {self.__point} points"

