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
    xValue = random.randint(0,dimension-1)
    yValue = random.randint(0,dimension-1)
    
    return (xValue, yValue)

def moveTarget(prevTarget, dimension):
    x,y = prevTarget
    while(True):
        direction = random.randint(1,4)
        if direction == 1:
            x+=1
        elif direction == 2:
            x-=1
        elif direction == 3:
            y+=1
        elif direction == 4:
            y-=1
        
        if x>0 and y<dimension-1:
            break
    return (x,y)
    
