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

