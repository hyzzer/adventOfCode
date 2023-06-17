from time import time

from module import getPuzzleInputFromFile

def play(puzzleInput): 
    puzzle = puzzleInput[:-1].split('\n')
    
    aim = 0
    depth = 0
    depth2 = 0
    horizontal = 0

    for instruction in puzzle:
        instructionValues = instruction.split(' ')
        if instructionValues[0] == 'forward':
            horizontal += int(instructionValues[1])
            depth2 += int(instructionValues[1]) * aim
        elif instructionValues[0] == 'up':
            depth += int(instructionValues[1])
            aim -= int(instructionValues[1])
        elif instructionValues[0] == 'down':
            depth -= int(instructionValues[1])
            aim += int(instructionValues[1])

    result1 = abs(horizontal * depth)
    result2 = abs(horizontal * depth2)

    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2021, 2)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()