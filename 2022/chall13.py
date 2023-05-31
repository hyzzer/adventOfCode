from time import time
from enum import Enum

from module import getPuzzleInputFromFile

class Comparison(Enum):
    LESS = 1
    EQUAL = 2
    GREATER = 3

def compare(leftArg, rightArg):
    left = [leftArg] if type(leftArg) == int else leftArg
    right = [rightArg] if type(rightArg) == int else rightArg
    
    leftLen = len(left)
    rightLen = len(right)

    for eltIdx in range(leftLen if leftLen <= rightLen else rightLen):

        if type(left[eltIdx]) == list or type(right[eltIdx]) == list:
            tmp = compare(left[eltIdx] if type(left[eltIdx]) == list else [left[eltIdx]], right[eltIdx] if type(right[eltIdx]) == list else [right[eltIdx]])
            if tmp != Comparison.EQUAL:
                return tmp
        else:
            if left[eltIdx] < right[eltIdx]:
                return Comparison.LESS
            if left[eltIdx] > right[eltIdx]:
                return Comparison.GREATER

    if leftLen < rightLen:
        return Comparison.LESS
    if leftLen > rightLen:
        return Comparison.GREATER
    return Comparison.EQUAL

def bubbleSort(listArg):
    sorted = False
    firstPacketIdx = 0
    secondPacketIdx = 1
    while sorted == False:
        sorted = True
        for eltIdx in range(len(listArg) - 1):
            if compare(listArg[eltIdx], listArg[eltIdx + 1]) == Comparison.GREATER:
                listArg[eltIdx], listArg[eltIdx + 1] = listArg[eltIdx + 1], listArg[eltIdx]
                sorted = False
                if eltIdx == firstPacketIdx:
                    firstPacketIdx += 1
                elif eltIdx + 1 == firstPacketIdx:
                    firstPacketIdx -= 1
                if eltIdx == secondPacketIdx:
                    secondPacketIdx += 1
                elif eltIdx + 1 == secondPacketIdx:
                    secondPacketIdx -= 1   
    return (firstPacketIdx + 1) * (secondPacketIdx + 1)


def play(puzzleInput):
    puzzle = puzzleInput.split('\n')

    result1 = 0
    result2 = 0

    numberOfPairs = len(puzzle) // 3

    puzzle2 = [[[2]], [[6]]]

    # PART 1
    for pairIdx in range(numberOfPairs):
        left = eval(puzzle[pairIdx * 3])
        right = eval(puzzle[pairIdx * 3 + 1])
        puzzle2.extend([left, right])

        comparisonResult = compare(left, right)
        if comparisonResult == Comparison.LESS:
            result1 += pairIdx + 1
    
    # PART 2
    result2 = bubbleSort(puzzle2)

    return result1, result2

def main():
    start = time()

    puzzle = getPuzzleInputFromFile(2022, 13)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()
