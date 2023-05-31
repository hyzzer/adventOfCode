import numpy as np
from time import time
from operator import itemgetter

from module import getPuzzleInputFromFile

def play(puzzleInput):
    puzzle = [[tuple([int(coordinate) for coordinate in coordinates.split(',')])for coordinates in line.split(' -> ') ]for line in puzzleInput.split('\n')[:-1]]
    
    result1 = 0
    result2 = 0
    
    xMax = 0
    yMax = 0

    # Find max
    for line in puzzle:
        xMaxLine = max(line, key = itemgetter(0))[0]
        xMax = xMaxLine if xMaxLine > xMax else xMax
        yMaxLine = max(line, key = itemgetter(1))[1]
        yMax = yMaxLine if yMaxLine > yMax else yMax
    
    # Create the map
    puzzleMap = np.array([[b'.' for y in range(yMax + 3)] for x in range(xMax + xMax // 4)], dtype = np.string_)

    # Add the rock
    for line in puzzle:
        for coordIdx in range(len(line) - 1):
            rangeX = sorted([line[coordIdx][0], line[coordIdx + 1][0]])
            rangeX[1] += 1
            for rockX in range(*rangeX):
                rangeY = sorted([line[coordIdx][1], line[coordIdx + 1][1]])
                rangeY[1] += 1
                for rockY in range(*rangeY):
                    puzzleMap[rockX][rockY] = b'#'

    # Additional row for bottom
    for rockX in range(xMax + xMax // 4):
        puzzleMap[rockX][-1] = b'#'
    
    count = 0
    isFinished = False
    while not isFinished:
        sandTmp = [500, 0]
        isSandRested = False 
        while not isSandRested:
            if sandTmp[1] == yMax and result1 == 0:
                result1 = count
                isSandRested = True
            else:
                if puzzleMap[sandTmp[0]][sandTmp[1] + 1] == b'.':
                    sandTmp[1] = sandTmp[1] + 1
                elif puzzleMap[sandTmp[0] - 1][sandTmp[1] + 1] == b'.':
                    sandTmp = [sandTmp[0] - 1, sandTmp[1] + 1]
                elif puzzleMap[sandTmp[0] + 1][sandTmp[1] + 1] == b'.':
                    sandTmp = [sandTmp[0] + 1, sandTmp[1] + 1]
                else:
                    puzzleMap[sandTmp[0], sandTmp[1]] = b'X'
                    isSandRested = True
                    count += 1
        if sandTmp == [500, 0]:
            result2 = count
            isFinished = True

    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2022, 14)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()
