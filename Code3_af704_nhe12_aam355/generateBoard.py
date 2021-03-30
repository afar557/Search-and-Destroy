import random

def generateBoard(dimension):
    board = []
    for x in range(dimension):
        col =[]
        for y in range(dimension):
            randomInt = random.randint(0,3)
            col.append(randomInt)
        board.append(col)
    return board

def assignTarget(dimension):
    xValue = random.randint(0,dimension)
    yValue = random.randint(0,dimension)
    
    return (xValue, yValue)
