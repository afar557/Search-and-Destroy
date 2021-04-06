from collections import deque
import random
from agent1 import manhattanDistance, getFNR, getTotalProb, normalizeCells, updateBelief

def agent2(grid, target):
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

        # caluculate agent 2 probability
        maxProb = -1
        maxInd = None
        for i in range(len(beliefMatrix)):
            for j in range(len(beliefMatrix)):
                curr = (1 - getFNR(grid[i][j])) * beliefMatrix[i][j]
                if curr > maxProb or (curr == maxProb and manhattanDistance(maxInd, (x,y)) > manhattanDistance((i,j), (x,y))):
                    maxProb = curr
                    maxInd = (i,j)

        # Pick min from belief matrix and enqueue it
        queue.append(maxInd)

        totalDistance += manhattanDistance((x,y), maxInd)
