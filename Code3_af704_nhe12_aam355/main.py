from generateBoard import generateBoard, assignTarget
from visualizeBoard import visualizeBoard
from agent1 import agent1
from agent2 import agent2
from improvedAgent import agent3

def main():
    dimension = 50
    grid = generateBoard(dimension)
    # for x in grid:
    #     print(x)

    target = assignTarget(dimension)
    # print("target is", target)

    print("Final score for agent1 is ->", agent1(grid, target))
    print("Final score for agent2 is ->", agent2(grid, target))
    print("Final score for agent3 is ->", agent3(grid, target))

    visualizeBoard(grid, "tester", target)
if __name__ == "__main__":
    main()
