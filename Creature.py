# Authors: Gai Li Ho, Dhruv Patel
# Date: 12/05/2023
# Description: This is the Creature class

from FieldInhabitant import FieldInhabitant


class Creature(FieldInhabitant):

    def __init__(self, x, y, symbol):
        FieldInhabitant.__init__(self,symbol)
        self.__x = x
        self.__y = y


    def getX(self):
        return self.__x

    def setX(self, newX):
        self.__x = newX


    def getY(self):
        return self.__y


    def setY(self, newY):
        self.__y = newY



