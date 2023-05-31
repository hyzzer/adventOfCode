import numpy as np
import sys
from time import time
import curses

from module import getPuzzleInputFromFile

np.set_printoptions(threshold=sys.maxsize)

def consoleDisplay(stdscr, nodesMatrix, finalPath):
    shape = np.shape(nodesMatrix)
    for rowIdx in range(shape[0]):
        for columnIdx in range(shape[1]):
            node = chr(nodesMatrix[rowIdx][columnIdx])
            if [rowIdx, columnIdx] in finalPath:
                stdscr.addstr(rowIdx, columnIdx*3, node, curses.color_pair(1))
            else:
                stdscr.addstr(rowIdx, columnIdx*3, node)

def getFinalPath(predecessorMatrixArg, startPosition, endPosition):
    finalPath = []
    predecessor = endPosition
    while predecessor != startPosition:
        predecessor = predecessorMatrixArg[predecessor[0]][predecessor[1]]
        finalPath.append(predecessor)
    return finalPath

def hasBNeighboor(puzzle, aPosition):
    if aPosition[0] != 0 and puzzle[aPosition[0] - 1][aPosition[1]] == 'b':
        return True
    if aPosition[0] != len(puzzle) - 1 and puzzle[aPosition[0] + 1][aPosition[1]] == 'b':
        return True
    if aPosition[1] != 0 and puzzle[aPosition[0]][aPosition[1] - 1] == 'b':
        return True
    if aPosition[1] != len(puzzle[0]) - 1 and puzzle[aPosition[0]][aPosition[1] + 1] == 'b':
        return True

def dijkstra(puzzle, startPosition, endPosition, stdscr = None):
    N, M = np.shape(puzzle)

    distanceMatrix = np.ones((N, M), dtype=int) * np.inf
    predecessorsMatrix = np.empty((N, M), dtype=list)
    availableNodesMatrix = np.ones((N, M), dtype=int) * np.inf

    distanceMatrix[startPosition[0]][startPosition[1]] = 0
    availableNodesMatrix[startPosition[0]][startPosition[1]] = 0

    count = N * M

    while count != 0:
        currentNode = np.nanargmin(availableNodesMatrix)
        currentNode = [currentNode // M, currentNode % M]

        # UP
        if currentNode[0] != 0:
            if puzzle[currentNode[0] - 1][currentNode[1]] <= puzzle[currentNode[0]][currentNode[1]] + 1:
                if distanceMatrix[currentNode[0]][currentNode[1]] + 1 < distanceMatrix[currentNode[0] - 1][currentNode[1]]:
                    distanceMatrix[currentNode[0] - 1][currentNode[1]] = distanceMatrix[currentNode[0]][currentNode[1]] + 1
                    availableNodesMatrix[currentNode[0] - 1][currentNode[1]] = distanceMatrix[currentNode[0]][currentNode[1]] + 1
                    predecessorsMatrix[currentNode[0] - 1][currentNode[1]] = currentNode

        # DOWN
        if currentNode[0] != N - 1:
            if puzzle[currentNode[0] + 1][currentNode[1]] <= puzzle[currentNode[0]][currentNode[1]] + 1:
                if distanceMatrix[currentNode[0]][currentNode[1]] + 1 < distanceMatrix[currentNode[0] + 1][currentNode[1]]:
                    distanceMatrix[currentNode[0] + 1][currentNode[1]] = distanceMatrix[currentNode[0]][currentNode[1]] + 1
                    availableNodesMatrix[currentNode[0] + 1][currentNode[1]] = distanceMatrix[currentNode[0]][currentNode[1]] + 1
                    predecessorsMatrix[currentNode[0] + 1][currentNode[1]] = currentNode

        # LEFT
        if currentNode[1] != 0:
            if puzzle[currentNode[0]][currentNode[1] - 1] <= puzzle[currentNode[0]][currentNode[1]] + 1:
                if distanceMatrix[currentNode[0]][currentNode[1]] + 1 < distanceMatrix[currentNode[0]][currentNode[1] - 1]:
                    distanceMatrix[currentNode[0]][currentNode[1] - 1] = distanceMatrix[currentNode[0]][currentNode[1]] + 1
                    availableNodesMatrix[currentNode[0]][currentNode[1] - 1] = distanceMatrix[currentNode[0]][currentNode[1]] + 1
                    predecessorsMatrix[currentNode[0]][currentNode[1] - 1] = currentNode

        # RIGHT
        if currentNode[1] != M - 1:
            if puzzle[currentNode[0]][currentNode[1] + 1] <= puzzle[currentNode[0]][currentNode[1]] + 1:
                if distanceMatrix[currentNode[0]][currentNode[1]] + 1 < distanceMatrix[currentNode[0]][currentNode[1] + 1]:
                    distanceMatrix[currentNode[0]][currentNode[1] + 1] = distanceMatrix[currentNode[0]][currentNode[1]] + 1
                    availableNodesMatrix[currentNode[0]][currentNode[1] + 1] = distanceMatrix[currentNode[0]][currentNode[1]] + 1
                    predecessorsMatrix[currentNode[0]][currentNode[1] + 1] = currentNode

        availableNodesMatrix[currentNode[0]][currentNode[1]] = np.nan
        count -= 1

    result = distanceMatrix[endPosition[0]][endPosition[1]] - 2

    if stdscr:
        finalPath = getFinalPath(predecessorsMatrix, startPosition, endPosition)
        consoleDisplay(stdscr, puzzle, finalPath)
        stdscr.addstr(N + 5, M * 3 - 20, "Result : {}".format(result))
        stdscr.getkey()

    return result

def play(puzzleInput, stdscr = None):
    if stdscr:
        stdscr.clear()
        curses.start_color()
        curses.use_default_colors()
        for i in range(0, curses.COLORS):
            curses.init_pair(i, i, -1)

    N = len(puzzleInput)
    M = len(puzzleInput[0])
    puzzle = np.array([[ord(puzzleInput[rowIdx][columnIdx]) for columnIdx in range(M)] for rowIdx in range(N)], dtype = int)

    startPosition1 = []
    startPosition2 = []
    endPosition = []

    for columnIdx in range(M):
        for rowIdx in range(N):
            if puzzleInput[rowIdx][columnIdx] == 'S':
                puzzle[rowIdx][columnIdx] = ord('a')
                startPosition1.extend([rowIdx, columnIdx])
                startPosition2.append([rowIdx, columnIdx])
            if puzzleInput[rowIdx][columnIdx] == 'a' and hasBNeighboor(puzzleInput, [rowIdx, columnIdx]):
                startPosition2.append([rowIdx, columnIdx])
            if puzzleInput[rowIdx][columnIdx] == 'E':
                puzzle[rowIdx][columnIdx] = 123
                endPosition = [rowIdx, columnIdx]   

    result1 = dijkstra(puzzle, startPosition1, endPosition, stdscr)
    result2 = []
    for startPosition in startPosition2:
        dijkstraResult = dijkstra(puzzle, startPosition, endPosition)
        result2.append(dijkstraResult)
    bestStartPosition = np.argmin(result2)
    result2 = result2[bestStartPosition]

    if stdscr:
        dijkstra(puzzle, startPosition2[bestStartPosition], endPosition, stdscr)

    return result1, result2
    

def main(stdscr=None):
    start = time()
    
    puzzle = getPuzzleInputFromFile(2022, 12).split('\n')[:-1]
    result1, result2 = play(puzzle, stdscr)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    # To show graphics :
    # curses.wrapper(main)
    main()
