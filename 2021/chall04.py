from time import time
import numpy as np

from module import getPuzzleInputFromFile

def play(puzzleInput): 
    puzzle = puzzleInput[:-1].split('\n')

    result1 = 0
    result2 = 0

    gridSize = 5
    
    chosenNumbers = [int(number) for number in puzzle[0].split(",")]
    grids = np.array([list(filter(None, numbersList.split(' '))) for numbersList in puzzle[1:] if numbersList != ''], int)
    numberOfBoards = len(grids) // gridSize

    winningLine = np.zeros(5)
    winningBoards = []

    for chosenNumbersIdx in range(len(chosenNumbers)):
        for rowIdx in range(len(grids)):
            for columnIdx in range(gridSize):
                if grids[rowIdx][columnIdx] == chosenNumbers[chosenNumbersIdx]:
                    boardIdx = rowIdx - rowIdx % gridSize
                    grids[rowIdx, columnIdx] = 0
                    if (grids[rowIdx] == winningLine).all() or (grids[boardIdx: boardIdx + gridSize, columnIdx] == winningLine).all():
                        if result1 == 0:
                            result1 = np.sum(grids[boardIdx: boardIdx + gridSize]) * chosenNumbers[chosenNumbersIdx]
                        if boardIdx not in winningBoards:
                            winningBoards.append(boardIdx)
                            if len(winningBoards) == numberOfBoards:
                                result2 = np.sum(grids[boardIdx: boardIdx + gridSize]) * chosenNumbers[chosenNumbersIdx]            
    
    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2021, 4)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()