from generateBoard import generateBoard
from visualizeBoard import visualizeBoard

def main():

    grid = generateBoard(10)
    for x in grid:
        print(x)
    
    visualizeBoard(grid, "tester")
if __name__ == "__main__":
    main()
