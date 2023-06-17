from time import time

from module import getPuzzleInputFromFile

def play(puzzleInput): 
    puzzle = puzzleInput[:-1].split('\n')
    
    result1 = 0
    result2 = 0

    for measurementIdx in range(1, len(puzzle)):
        if int(puzzle[measurementIdx]) > int(puzzle[measurementIdx - 1]):
            result1 += 1
    
    windowSize = 3

    for windowIdx in range (windowSize, len(puzzle)):
        firstWindow = sum([int(measurement) for measurement in puzzle[windowIdx - windowSize:windowIdx]])
        secondWindow = sum([int(measurement) for measurement in puzzle[windowIdx - windowSize + 1: windowIdx + 1]])
        if secondWindow > firstWindow:
            result2 += 1

    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2021, 1)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()