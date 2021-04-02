from generateBoard import generateBoard, assignTarget
from visualizeBoard import visualizeBoard
from agent1 import agent1

def main():
    dimension = 5
    grid = generateBoard(dimension)
    for x in grid:
        print(x)

    target = assignTarget(dimension)
    print("target is", target)

    print("Final score is ->", agent1(grid, target))
    visualizeBoard(grid, "tester", target)
if __name__ == "__main__":
    main()
