from time import time
import numpy as np

from module import getPuzzleInputFromFile

def play(puzzleInput):
    puzzle = puzzleInput.split('\n')[:-1]
    
    result1 = 0
    result2 = 0
    
    puzzle = np.array([[int(tree) for tree in treeRow] for treeRow in puzzle])

    # PART 1
    result1 = 2 * len(puzzle[0]) + 2 * (len(puzzle) - 2)

    for rowIdx, treeRow in enumerate(puzzle):
        if rowIdx != 0 and rowIdx != len(puzzle)-1:
            for columnIdx, tree in enumerate(treeRow):
                if columnIdx != 0 and columnIdx != (len(treeRow))-1:
                    if (max(treeRow[:columnIdx]) < tree):
                        result1 += 1
                    elif (max(treeRow[columnIdx+1:]) < tree):
                        result1 += 1
                    elif (max(puzzle[:rowIdx, columnIdx]) < tree):
                        result1 += 1
                    elif (max(puzzle[rowIdx+1:, columnIdx]) < tree):
                        result1 += 1

    # PART 2
    def findSup(targetArg, sideList):
        i = 0
        while (True):
            if sideList[i] >= targetArg or i == len(sideList)-1:
                return i + 1
            i += 1
            
    result2 = 0
    for rowIdx in range(1, len(puzzle) -1):
        for columnIdx in range(1, len(puzzle[:, 0]) -1):
            target = puzzle[rowIdx, columnIdx]
            leftList = puzzle[rowIdx, :columnIdx][::-1]
            rightList = puzzle[rowIdx, columnIdx+1:]
            topList = puzzle[:rowIdx, columnIdx][::-1]
            bottomList = puzzle[rowIdx+1:, columnIdx]
            scenicScore =  findSup(target, leftList) * findSup(target, rightList) * findSup(target, topList) * findSup(target, bottomList)
            result2 = scenicScore if scenicScore > result2 else result2
    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2022, 8)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()