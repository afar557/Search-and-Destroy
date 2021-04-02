from collections import deque
import random

# Function that calculates the Manhattan distance from one point to the other
def manhattanDistance(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Function to get the false negative rate depending on the grid
def getFNR(number):
    if number==0:
        FNR = 0.1
    elif number==1:
        FNR = 0.3
    elif number==2:
        FNR = 0.9
    elif number==3:
        FNR = 0.7
    return FNR

# Function to get the total probability in the belief matrix
def getTotalProb(beliefMatrix):
    totalProb=0 
    for row in beliefMatrix:
        for cell in row:
            totalProb+=cell
    return totalProb

# Function to normalize all cells in the belief matrix
def normalizeCells(beliefMatrix, totalProb):
    for x in range(len(beliefMatrix)):
        for y in range(len(beliefMatrix)):
            beliefMatrix[x][y] /= totalProb
    return beliefMatrix

# Function to update the belief matrix
def updateBelief(beliefMatrix, cell, grid):
    x,y = cell[0],cell[1]
    
    # Find the new probability for the cell you just queried
    newCellProb = getFNR(grid[x][y]) * beliefMatrix[x][y]
    # print("New Cell Prob is ->", newCellProb)
    # print()

    # Update belief state for the current cell
    beliefMatrix[x][y] = newCellProb
    # print("Updated belief matrix is->")
    # for x in beliefMatrix:
    #     print(x)
    # print()

    # Find the new total probability
    newtotalProb = getTotalProb(beliefMatrix)
    # print("New Total Prob is ->", newtotalProb)
    # print()

    # Normalize all cells
    beliefMatrix = normalizeCells(beliefMatrix, newtotalProb)
    # print("Normalized belief matrix is->")
    # for x in beliefMatrix:
    #     print(x)
    return beliefMatrix

# Function to get cell with max probability
def getMaxCell(beliefMatrix, currentCell):
    maxCell = -1
    for row in beliefMatrix:
        for cell in row:
            if cell>maxCell:
                maxCell=cell
    
    minDist = len(beliefMatrix)**2
    ansCell = None
    for i in range(len(beliefMatrix)):
        for j in range(len(beliefMatrix)):
            manhattanDist = manhattanDistance((i,j), currentCell)
            if beliefMatrix[i][j]==maxCell and manhattanDist<minDist:
                minDist = manhattanDist
                ansCell = (i,j)
    return ansCell

def agent1(grid, target):
    dimension = len(grid)
    # Number of searches
    searches = 0
    # Distance traveled
    totalDistance = 0

    # Calculate the initial probability of each cell
    initProb = 1 / (dimension*dimension)

    # Create the belief matrix
    beliefMatrix = [[initProb for i in range(dimension)] for j in range(dimension)]
    # print("Belief Matrix ->")
    # for x in beliefMatrix:
    #     print(x)

    # Create queue to store cells
    queue = deque()
    # Pick random cell to enqueue
    xValue = random.randint(0,dimension-1)
    yValue = random.randint(0,dimension-1)
    # Enqueue random coordinates
    queue.append((xValue,yValue))

    # Iterate through the queue
    while queue:
        x,y = queue.popleft()

        # increments number of searhces
        searches+=1

        # Check if the dequeued cell is the target
        if (x,y) == target:
            # Generate a random number between 
            rand = random.uniform(0,1)
            if rand>getFNR(grid[x][y]):
                print("Success")
                print("Searches is ->", searches)
                print("Total Distance is ->", totalDistance)
                return totalDistance+searches

        # Update the belief matrix
        beliefMatrix = updateBelief(beliefMatrix, (x,y), grid)

        # Pick min from belief matrix and enqueue it
        nextCell = getMaxCell(beliefMatrix, (x,y))
        queue.append(nextCell)

        totalDistance += manhattanDistance((x,y), nextCell)
