from time import time
from copy import deepcopy

from module import getPuzzleInputFromFile

def play(puzzleInput):
    puzzle = puzzleInput.split('\n')

    result1 = 0
    result2 = 0

    stacks = puzzle[:8]
    stacksModel = []

    for stack in stacks:
        stackTmp = []
        for crateIdx in range(len(stack)):
            if ((crateIdx-1)%4 == 0):
                stackTmp.append(stack[crateIdx])
        stacksModel.append(stackTmp)

    stacksModel = [[stack[i] for stack in stacksModel if (stack[i] != ' ')] for i in range(len(stacksModel[-1]))]

    def solution(puzzle, stacksModelArg, isModelReversed):
        for move in [instruction.split(' ') for instruction in puzzle[10:-1]]:
            quantity = int(move[1])
            departure = int(move[3]) -1
            arrival = int(move[5]) -1
            stacksModelArg[arrival] = stacksModelArg[departure][:quantity][::-1] + stacksModelArg[arrival] if isModelReversed else stacksModelArg[departure][:quantity] + stacksModelArg[arrival]
            stacksModelArg[departure] = stacksModelArg[departure][quantity:]

        return ''.join([stack[0] for stack in stacksModelArg])

    result1 = solution(puzzle, deepcopy(stacksModel), True)
    result2 = solution(puzzle, deepcopy(stacksModel), False)
    
    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2022, 5)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()