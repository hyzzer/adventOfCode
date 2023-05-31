from time import time

from module import getPuzzleInputFromFile

def play(puzzleInput): 
    puzzle = puzzleInput[:-1].split('\n\n')

    for oneElfIdx in range(len(puzzle)):
        puzzle[oneElfIdx] = sum([int(food) for food in puzzle[oneElfIdx].split('\n')])

    result1 = max(puzzle)
    result2 = sum(sorted(puzzle)[-3:])

    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2022, 1)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()