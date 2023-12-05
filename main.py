# todo 
# Authors: {Your Name}, Dhruv Patel
# Date:
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
    
    game.gameOver()
    game.highScore()
    
if __name__ == '__main__':
    main()