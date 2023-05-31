from time import time

from module import getPuzzleInputFromFile

def play(puzzleInput):
    puzzle = puzzleInput.split('\n')[:-1]
    
    result1 = 0
    result2 = 0

    # PART 1
    def itemToPoint(item):
        item = ord(item)
        if item <= 90:
            return item - 64 + 26
        return item - 96

    for rucksack in puzzle:
        halfRucksack = len(rucksack) // 2
        firstHalf = rucksack[:halfRucksack]
        secondHalf = rucksack[halfRucksack:]

        isPriorityItem = -1
        itemIdx = 0

        while (isPriorityItem == -1):
            isPriorityItem = secondHalf.find(firstHalf[itemIdx])
            if isPriorityItem != -1:
                result1 += itemToPoint(secondHalf[isPriorityItem])
            itemIdx += 1

    # PART 2
    for rucksackIdx in range(0, len(puzzle), 3):
        firstRucksack = puzzle[rucksackIdx]
        secondRucksack = puzzle[rucksackIdx+1]
        thirdRucksack = puzzle[rucksackIdx+2]

        itemIdx1 = 0
        isPriorityItem1 = -1
        isPriorityItem2 = -1

        while (isPriorityItem2 == -1):
            isPriorityItem1 = secondRucksack.find(firstRucksack[itemIdx1])
            if isPriorityItem1 != -1:
                isPriorityItem2 = thirdRucksack.find(firstRucksack[itemIdx1])
                if isPriorityItem2 != -1:
                    result2 += itemToPoint(firstRucksack[itemIdx1])
            itemIdx1 += 1
    return result1, result2

def main():
    start = time()
    puzzle = getPuzzleInputFromFile(2022, 3)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()