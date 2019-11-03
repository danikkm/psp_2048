# Main.py
from GameBoard import GameBoard
from Score import Score
import SystemHelper as sh
import Movement as mv

def main():

    Board = GameBoard()

    newBoardMatrix = Board.createGameBoard(4)

    Board.placeRandomElement(newBoardMatrix)

    print("Controls: capital/non-capital WSAD letter or arrows")
    print("To exit the game press: q")
    Board.drawGameBoard(newBoardMatrix)

    keyStrokes = {
        "W": 87,
        "S": 83,
        "A": 65,
        "D": 68,
        "w": 119,
        "s": 115,
        "a": 97,
        "d": 100,
        "q": 113,
        "upArrow": 65,
        "downArrow": 66,
        "leftArrow": 68,
        "rightArrow": 67
    }

    print("Your current score is: ", Score.getScore())

    while True:
        pressedKey = mv.getPressedKey()

        if pressedKey == list(keyStrokes.values())[0] or \
                pressedKey == list(keyStrokes.values())[4] or \
                pressedKey == list(keyStrokes.values())[9]:
            mv.movementSwipeUp(newBoardMatrix)
            print("Your current score is: ", Score.getScore())
        elif pressedKey == list(keyStrokes.values())[1] or \
                pressedKey == list(keyStrokes.values())[5] or \
                pressedKey == list(keyStrokes.values())[10]:
            mv.movementSwipeDown(newBoardMatrix)
            print("Your current score is: ", Score.getScore())
        elif pressedKey == list(keyStrokes.values())[2] or \
                pressedKey == list(keyStrokes.values())[6] or \
                pressedKey == list(keyStrokes.values())[11]:
            mv.movementSwipeLeft(newBoardMatrix)
            print("Your current score is: ", Score.getScore())
        elif pressedKey == list(keyStrokes.values())[3] or \
                pressedKey == list(keyStrokes.values())[7] or \
                pressedKey == list(keyStrokes.values())[12]:
            mv.movementSwipeRight(newBoardMatrix)
            print("Your current score is: ", Score.getScore())
        elif pressedKey == list(keyStrokes.values())[8]:
            quit()
        else:
            sh.flushScreen()
            print("Wrong key")
            Board.drawGameBoard(newBoardMatrix)


        if mv.gameOver(newBoardMatrix):
            print("Restart game? (y/n)")
            if(input()) == 'y':
                print("goto main")
                main()
            else:
                quit()

if __name__ == '__main__':
    sh.flushScreen()
    main()
