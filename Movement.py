# Movement.py

import time
import SystemHelper as sh
from GameBoard import GameBoard
from getch import getch


def swipeCurrentElement(object):
    sh.flushScreen()
    GameBoard.drawGameBoard(GameBoard,object)
    time.sleep(.3)
    GameBoard.placeRandomElement(GameBoard, object)
    sh.flushScreen()
    GameBoard.drawGameBoard(GameBoard, object)

def movementSwipeUp(gameBoard):
    swiped = False

    for y in range(len(gameBoard)):
        for x in range(len(gameBoard)):
            objectAtXY = GameBoard.getObject(x, y, gameBoard)
            elementAbove = GameBoard.getObject(x, y - 1, gameBoard)

            if objectAtXY == "*":
                continue

            elif elementAbove == None:
                continue

            swiped = GameBoard.moveElement(x, y, "UP", gameBoard) or swiped

    if swiped:
        swipeCurrentElement(gameBoard)
    else:
        sh.flushScreen()
        GameBoard.drawGameBoard(GameBoard,gameBoard)
        time.sleep(.3)


def movementSwipeDown(gameBoard):
    swiped = False

    for y in range(len(gameBoard)):
        y = len(gameBoard) - 1 - y

        for x in range(len(gameBoard)):
            objectAtXY = GameBoard.getObject(x, y, gameBoard)
            elementBelow = GameBoard.getObject(x, y + 1, gameBoard)

            if objectAtXY == "*":
                continue
            elif elementBelow == None:
                continue

            swiped = GameBoard.moveElement(x, y, "DOWN", gameBoard) or swiped
    if swiped:
        swipeCurrentElement(gameBoard)
    else:
        sh.flushScreen()
        GameBoard.drawGameBoard(GameBoard,gameBoard)
        time.sleep(.3)

def movementSwipeLeft(gameBoard):
    swiped = False

    for y in range(len(gameBoard)):
        for x in range(len(gameBoard)):
            objectAtXY = GameBoard.getObject(x, y, gameBoard)
            elementOnTheLeft = GameBoard.getObject(x - 1, y, gameBoard)

            if objectAtXY == "*":
                continue
            elif elementOnTheLeft == None:
                continue

            swiped = GameBoard.moveElement(x, y, "LEFT", gameBoard) or swiped

    if swiped:
        swipeCurrentElement(gameBoard)
    else:
        sh.flushScreen()
        GameBoard.drawGameBoard(GameBoard,gameBoard)
        time.sleep(.3)

def movementSwipeRight(gameBoard):
    swiped = False

    for y in range(len(gameBoard)):
        for x in range(len(gameBoard)):
            x = len(gameBoard) - 1 - x

            objectAtXY = GameBoard.getObject(x, y, gameBoard)
            elementOnTheRight = GameBoard.getObject(x + 1, y, gameBoard)

            if objectAtXY == "*":
                continue
            elif elementOnTheRight == None:
                continue

            swiped = GameBoard.moveElement(x, y, "RIGHT", gameBoard) or swiped


    if swiped:
        swipeCurrentElement(gameBoard)
    else:
        sh.flushScreen()
        GameBoard.drawGameBoard(GameBoard,gameBoard)
        time.sleep(.3)



def gameOver(gameBoard):
    for y in range(len(gameBoard)):
        for x in range(len(gameBoard)):
            if GameBoard.isItPossibleToSwipe(x, y, gameBoard):
                return False
    return True

def getPressedKey():
    return ord(getch())
