from generateBoard import generateBoard, assignTarget
from visualizeBoard import visualizeBoard
from agent1 import agent1
from agent2 import agent2
from improvedAgent import agent3

def main():
    osum1 = 0
    osum2 = 0
    osum3 = 0
    for i in range(10):
        sum1 = 0
        sum2 = 0
        sum3 = 0
        print("map:",i)
        dimension = 50
        grid = generateBoard(dimension)
        for i in range(10):
            print("iteration:",i)
            target = assignTarget(dimension)
        
            sum1 += agent1(grid, target)
            sum2 += agent2(grid, target)
            sum3 += agent3(grid, target)
        osum1 += sum1/10
        osum2 += sum2/10 
        osum3 += sum3/10
    print("Avg score for agent1 is ->", osum1/10)
    print("Avg score for agent2 is ->", osum2/10)
    print("Avg score for agent3 is ->", osum3/10)

    visualizeBoard(grid, "tester", target)
if __name__ == "__main__":
    main()
