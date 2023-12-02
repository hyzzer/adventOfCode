from time import time

from module import getPuzzleInputFromFile

def findFirstInteger(lineArg, fromLeftToRight=True):
    result = -1
    direction = 1 if fromLeftToRight else -1
    letterIdx = 0
    while (result == -1):
        if (48 <= ord(lineArg[::direction][letterIdx]) <= 57):
            result = int(lineArg[::direction][letterIdx])
        letterIdx += 1
    return result

def replaceNumbers(lineArg):    
    numbersDict = {
        'oneight' : '18',
        'fiveight' : '58',
        'eighthree' : '83',
        'threeight' : '38',
        'eightwo' : '82',
        'twone' : '21',
        'sevenine' : '79',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    newLine = lineArg
    for spelled, digit in numbersDict.items():
        newLine = newLine.replace(spelled, digit)
    return newLine

def play(puzzleInput): 
    puzzle = puzzleInput[:-1].split('\n')

    result1 = 0
    result2 = 0

    # PART 1
    for line in puzzle:
        combinationValueLeft = findFirstInteger(line)
        combinationValueRight = findFirstInteger(line, False)
        
        combinationValue = int("{}{}".format(combinationValueLeft, combinationValueRight))
        result1 += combinationValue

    # PART 2
    for line2 in puzzle:
        newLine = replaceNumbers(line2)
        combinationValueLeft2 = findFirstInteger(newLine)
        combinationValueRight2 = findFirstInteger(newLine, False)

        combinationValue2 = int("{}{}".format(combinationValueLeft2, combinationValueRight2))
        print(newLine, ' : ', combinationValue2)
        result2 += combinationValue2

    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2023, 1)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()