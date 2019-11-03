# GameBoard.py

import random
import termcolor
from Score import Score

sessionScore = Score(0)

class GameBoard():
    boardColors = {
        '*': None,
        '2': 'red',
        '4': 'yellow',
        '8': 'green',
        '16': 'magenta',
        '32': 'cyan',
        '64': 'blue',
        '128': 'grey',
        '256': 'white',
        '512': 'green',
        '1024': 'blue',
        '2048': 'red'
    }

    def __init__(self):
        pass

    def getGameBoard(self, gameBoard):
        return gameBoard

    def createGameBoard(self, size):
        assert size > 1, "Wrong number, must be: > 1"
        assert type(size) == int, "Argument must be an int type"
        return [["*" for x in range(size)] for x in range(size)]

    def drawGameBoard(self, gameBoard):

        verticalBorder = ""
        for i in range(len(gameBoard) + 2):
            verticalBorder += "-\t"
        print(verticalBorder)
        for y in range(len(gameBoard)):
            row = ""
            for x in gameBoard[y]:

                if termcolor is not None:
                    row += termcolor.colored(x, self.boardColors[x]);
                else:
                    row += x
                row += "\t"

            print("|\t" + row + "|")
            if y is not len(gameBoard) - 1:
                print("")
        print(verticalBorder)

    def placeRandomElement(self, gameBoard):
        if (self.boardIsFull(gameBoard)):
            print("not supposed to be here")
            return False

        randomlyGeneratedNumber = random.random() * 100

        if randomlyGeneratedNumber < 60:
            digitToPlace = "2"

        elif randomlyGeneratedNumber < 90 and randomlyGeneratedNumber >= 60:
            digitToPlace = "4"

        else:
            digitToPlace = "8"


        foundPlace = False


        while not foundPlace:

            randomlyGeneratedNumberX = random.random() * len(gameBoard)
            randomlyGeneratedNumberY = random.random() * len(gameBoard)

            randomlyGeneratedNumberX = int(randomlyGeneratedNumberX)
            randomlyGeneratedNumberY = int(randomlyGeneratedNumberY)

            foundPlace = self.getObject(randomlyGeneratedNumberX, randomlyGeneratedNumberY, gameBoard) == '*'

        self.setObject(digitToPlace, randomlyGeneratedNumberX, randomlyGeneratedNumberY, gameBoard)


        return True


    @classmethod
    def boardIsFull(cls, gameBoard):

        for row in gameBoard:
            for element in row:
                if element == "*":
                    return False
        return True

    @classmethod
    def getObject(cls, xCoordinate, yCoordinate, gameBoard):
        assert type(xCoordinate) == type(yCoordinate), "Values must be an int type"

        if xCoordinate >= len(gameBoard) or yCoordinate >= len(gameBoard) or xCoordinate < 0 or yCoordinate < 0:
            return None

        return gameBoard[yCoordinate][xCoordinate]

    @classmethod
    def setObject(cls, objectToPlace, xCoordinate, yCoordinate, gameBoard):
        assert type(xCoordinate) == type(yCoordinate) == int, "Values must be an int types"

        if xCoordinate >= len(gameBoard) or yCoordinate >= len(gameBoard) or xCoordinate < 0 or yCoordinate < 0:
            return False

        gameBoard[yCoordinate][xCoordinate] = objectToPlace
        return True

    @classmethod
    def moveElement(cls, xCoordinate, yCoordinate, directionToSwipe, gameBoard):
        objectAtXY = cls.getObject(xCoordinate, yCoordinate, gameBoard)

        assert objectAtXY != "*", "Error in logic"

        validSwipeDirection = (directionToSwipe == "UP" or
                               directionToSwipe == "DOWN" or
                               directionToSwipe == "LEFT" or
                               directionToSwipe == "RIGHT")

        assert validSwipeDirection, "Invalid swipe direction"

        if directionToSwipe == "UP":
            adjacentObject = (cls.getObject(xCoordinate, yCoordinate - 1, gameBoard),
                                 xCoordinate, yCoordinate - 1)
            #debug
            #print("Swiped", directionToSwipe, "supposed to swipe:", "up")

        elif directionToSwipe == "DOWN":
            adjacentObject = (cls.getObject(xCoordinate, yCoordinate + 1, gameBoard),
                                 xCoordinate, yCoordinate + 1)
            # debug
            #print("Swiped", directionToSwipe, "supposed to swipe:", "down")

        elif directionToSwipe == "LEFT":
            adjacentObject = (cls.getObject(xCoordinate - 1, yCoordinate, gameBoard),
                                 xCoordinate - 1, yCoordinate)
            # debug
            #print("Swiped", directionToSwipe, "supposed to swipe:", "left")

        elif directionToSwipe == "RIGHT":
            adjacentObject = (cls.getObject(xCoordinate + 1, yCoordinate, gameBoard),
                                 xCoordinate + 1, yCoordinate)
            # debug
            #print("Swiped", directionToSwipe, "supposed to swipe:", "right")

        if adjacentObject[0] == None: # edge of the board
            return False
        elif objectAtXY != adjacentObject[0] and adjacentObject[0] != "*": # cant combine 2 numbers
            return False

        elif adjacentObject[0] == "*":
            cls.setObject("*", xCoordinate, yCoordinate, gameBoard)
            cls.setObject(objectAtXY, adjacentObject[1], adjacentObject[2], gameBoard)
            cls.moveElement(adjacentObject[1], adjacentObject[2], directionToSwipe, gameBoard)
            return True
        elif objectAtXY == adjacentObject[0]:
            cls.setObject("*", xCoordinate, yCoordinate, gameBoard)
            cls.setObject(str(int(adjacentObject[0]) * 2), adjacentObject[1], adjacentObject[2], gameBoard)
            cls.moveElement(adjacentObject[1], adjacentObject[2], directionToSwipe, gameBoard)

            Score.addScore(int(adjacentObject[0]) * 2)

            return True
        else:
            assert False, "No way"

        return False


    @classmethod
    def isItPossibleToSwipe(cls, xCoordinate, yCoordinate, gameBoard):
        objectAtXY = cls.getObject(xCoordinate, yCoordinate, gameBoard)

        if objectAtXY == None:
            return False
        elif objectAtXY == "*":
            return True

        return (
                objectAtXY == cls.getObject(xCoordinate, yCoordinate - 1, gameBoard) or
                objectAtXY == cls.getObject(xCoordinate, yCoordinate + 1, gameBoard) or
                objectAtXY == cls.getObject(xCoordinate - 1, yCoordinate, gameBoard) or
                objectAtXY == cls.getObject(xCoordinate + 1, yCoordinate, gameBoard)
        )
