from time import time
from math import inf
from random import randint

from module import getPuzzleInputFromFile

def play(puzzleInput):    
    result1 = 0
    result2 = 0

    # Data parsing
    puzzle = [line.split(' ') for line in puzzleInput.split('\n')[:-1]]
    flowRatesDict = {}
    connectionsDict = {}
    for lineIdx in range(len(puzzle)):
        flowRatesDict[puzzle[lineIdx][1]] = int(puzzle[lineIdx][4].split('=')[1][:-1])
        connectionsDict[puzzle[lineIdx][1]] = [valve[:2] for valve in puzzle[lineIdx][9:]]

    # PART 1
    def bfs(connectionsDictArg, start, end):
        distances = {node:inf for node in connectionsDictArg}
        predecessors = {node:'' for node in connectionsDictArg}
        distances[start] = 0
        predecessors[start] = start
        queue = [start]
        while queue != 0 and distances[end] == inf:
            for node in connectionsDictArg[queue[0]]:
                if distances[node] > distances[queue[0]] + 1:
                    distances[node] = distances[queue[0]] + 1
                    predecessors[node] = queue[0]
                    queue.append(node)
            queue.pop(0)
        path = [end]
        while path[-1] != start:
            path.append(predecessors[path[-1]])
        return path[::-1]

    nonZeroValves = [valve for valve, flowRate in flowRatesDict.items() if flowRate != 0]
    pathsDict = {}
    for A in nonZeroValves + ['AA']:
        for B in nonZeroValves:
            pathsDict["{}.{}".format(A, B)] = bfs(connectionsDict, A, B)

    class MaxFlowRate():
        value = 0

    def getTotalFlowRate1(flowRatesDictArg, pathsDictArg, pathArg):
        minutes = 30
        totalFlowRate = 0
        valveIdx = 0
        while minutes != 0 and valveIdx != len(pathArg) - 1:
            timeToFly = len(pathsDictArg["{}.{}".format(pathArg[valveIdx], pathArg[valveIdx + 1])])
            if timeToFly > minutes:
                minutes = 0
                valveIdx += 2
            else:
                minutes -= timeToFly
                valveIdx += 1 if minutes != 0 else 2
                totalFlowRate += flowRatesDictArg[pathArg[valveIdx]] * minutes
        if totalFlowRate > MaxFlowRate.value:
            MaxFlowRate.value = totalFlowRate
        return valveIdx
    
    def getTotalFlowRate2(flowRatesDictArg, pathsDictArg, pathArg):
        totalFlowRate = 0
        pathLen = len(pathArg)
        pathLen += pathLen % 2
        minutesA = 26
        minutesB = 26
        pathArg.insert(pathLen // 2, 'AA')
        pathArgA = pathArg[:pathLen // 2]
        pathArgB = pathArg[pathLen // 2:]
        valveIdxA = 0
        valveIdxB = 0

        while minutesA != 0 and valveIdxA != len(pathArgA) - 1:
            timeToFlyA = len(pathsDictArg["{}.{}".format(pathArgA[valveIdxA], pathArgA[valveIdxA + 1])])
            if timeToFlyA > minutesA:
                minutesA = 0
                valveIdxA += 2
            else:
                minutesA -= timeToFlyA
                valveIdxA += 1 # if minutesA != 0 else 2
                totalFlowRate += flowRatesDictArg[pathArgA[valveIdxA]] * minutesA

        while minutesB != 0 and valveIdxB != len(pathArgB) - 1:
            timeToFlyB = len(pathsDictArg["{}.{}".format(pathArgB[valveIdxB], pathArgB[valveIdxB + 1])])
            if timeToFlyB > minutesB:
                minutesB = 0
                valveIdxB += 2
            else:
                minutesB -= timeToFlyB
                valveIdxB += 1 if minutesB != 0 else 2
                totalFlowRate += flowRatesDictArg[pathArgB[valveIdxB]] * minutesB    
        print(pathArg)
        print(pathArgA)
        print(pathArgB)
        print("---------")
        if totalFlowRate > MaxFlowRate.value:
            MaxFlowRate.value = totalFlowRate
        return len(pathArgA) + valveIdxB
    
    def getAllCombinations(listArg):
        allCombinations = []
        def innerProcess(listArg, blockedElements=[]):
            if len(listArg) == 1:
                return getTotalFlowRate2(flowRatesDict, pathsDict, ['AA'] + blockedElements + listArg)

            for eltIdx in range(len(listArg)):
                chosenElt = listArg.pop(eltIdx)
                blockedElements.append(chosenElt)
                level = innerProcess(listArg, blockedElements)
                listArg.insert(eltIdx, chosenElt)
                blockedElements.pop(-1)
                if len(blockedElements) > level - 2:
                    return level
            return inf
        innerProcess(listArg)
        return allCombinations

    getAllCombinations(nonZeroValves)
    result1 = MaxFlowRate.value

    # PART 2
    # TODO

    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2022, 16)
    # puzzle = getPuzzleInputFromFile(2022, 16, './inputs/example16.txt')
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()