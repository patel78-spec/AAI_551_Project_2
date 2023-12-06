# Authors: Gai Li Ho, Dhruv Patel
# Date: 12/05/2023
# Description: This is the Field Inhabitant class

class FieldInhabitant:

    def __init__(self, inhabitant):
        self._inhabitant = inhabitant


    def getInhabitant(self):
        return self._inhabitant

    def setInhabitant(self, newInhabitant):
        self._inhabitant = newInhabitant