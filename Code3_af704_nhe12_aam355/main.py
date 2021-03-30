from generateBoard import generateBoard, assignTarget
from visualizeBoard import visualizeBoard

def main():
    dimension = 10
    grid = generateBoard(dimension)
    for x in grid:
        print(x)
    
    target = assignTarget(dimension)
    print("target is", target)
    visualizeBoard(grid, "tester", target)
if __name__ == "__main__":
    main()
