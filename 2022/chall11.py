from time import time
from math import prod

from module import getPuzzleInputFromFile

def operation(a, b, sign):
    if b == 'old':
        b = a
    match sign:
        case '*':
            return a * b
        case '+':
            return a + b

def setup(data, numberOfMonkeysArg):
    monkeysInstructions = []
    for instructionIdx in range(numberOfMonkeysArg):
        items = [int(item) for item in data[instructionIdx*7+1].split(':')[1].split(', ')]
        [sign, b] = data[instructionIdx*7+2].split('= ')[1].split(' ')[1:]
        b = int(b) if b != 'old' else b
        divisibleBy = int(data[instructionIdx*7+3].split('by ')[1])
        choices = (int(data[instructionIdx*7+4][-1]), int(data[instructionIdx*7+5][-1]))
        monkeysInstructions.append([items, sign, b, divisibleBy, choices])
    return monkeysInstructions


def findResult(numberOfRoundsArg, monkeysInstructionsArg, isDividedByThree, numberOfMonkeys, monkeysInstructions):
    numberOfInspectedItemsByMonkey = [0 for _ in range(numberOfMonkeys)]
    listOfItemsByMonkey = [monkey[0][:] for monkey in monkeysInstructions]
    moduloOfEverything = prod([monkey[3] for monkey in monkeysInstructions])
    for _ in range(numberOfRoundsArg):
        for monkeyIdx in range(len(monkeysInstructionsArg)):
            for itemIdx in range(len(listOfItemsByMonkey[monkeyIdx])):
                newItem = operation(listOfItemsByMonkey[monkeyIdx][itemIdx], monkeysInstructionsArg[monkeyIdx][2], monkeysInstructionsArg[monkeyIdx][1])
                if isDividedByThree:
                    newItem = newItem // 3
                newItem = newItem % moduloOfEverything
                choice = monkeysInstructionsArg[monkeyIdx][4][0] if newItem % monkeysInstructionsArg[monkeyIdx][3] == 0 else monkeysInstructionsArg[monkeyIdx][4][1]
                listOfItemsByMonkey[choice].append(newItem)
                numberOfInspectedItemsByMonkey[monkeyIdx] += 1
            listOfItemsByMonkey[monkeyIdx] = []
    numberOfInspectedItemsByMonkey.sort()
    return numberOfInspectedItemsByMonkey[-1] * numberOfInspectedItemsByMonkey[-2]

def play(puzzleInput):
    puzzle = puzzleInput.split('\n')[:-1]
    numberOfMonkeys = 8
    monkeysInstructions = setup(puzzle, numberOfMonkeys)
    result1 = findResult(20, monkeysInstructions, True, numberOfMonkeys, monkeysInstructions)
    result2 = findResult(10000, monkeysInstructions, False, numberOfMonkeys, monkeysInstructions)
    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2022, 11)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()