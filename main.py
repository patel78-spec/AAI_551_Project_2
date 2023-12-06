# Authors: Gai Li Ho, Dhruv Patel
# Date: 12/05/2023
# Description:

from GameEngine import GameEngine

# todo by dhruv
def main():
    game = GameEngine()
    game.initializeGame()
    game.intro()
    
    while game.remainingVeggies():
        game.printField()
        game.moveRabbits()
        game.moveCaptain()
        if game.remainingVeggies() == 0:
            break
        game.moveSnake()
    
    game.gameOver()
    game.highScore()
    
if __name__ == '__main__':
    main()