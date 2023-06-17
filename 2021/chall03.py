from time import time

from module import getPuzzleInputFromFile

def calculateRating(report, numberOfBits, isOxygen):
    currentList = report
    for position in range(numberOfBits):
        tmpListOnes = []
        tmpListZeros =[]
        for reportValue in currentList:
            if reportValue[position] == '1':
                tmpListOnes.append(reportValue)
            else:
                tmpListZeros.append(reportValue)
        if len(currentList) == 2:
            return tmpListOnes[0] if isOxygen else tmpListZeros[0]
        if isOxygen:
            currentList = tmpListOnes if len(tmpListOnes) > len(tmpListZeros) else tmpListZeros
        else:
            currentList = tmpListOnes if len(tmpListOnes) < len(tmpListZeros) else tmpListZeros


def play(puzzleInput): 
    puzzle = puzzleInput[:-1].split('\n')
    
    numberOfBits = len(puzzle[0])
    half = len(puzzle) // 2

    gammaRate = ''
    epsilon = ''

    for position in range(numberOfBits):
        numberOfOnes = 0
        for reportValue in puzzle:
            if reportValue[position] == '1':
                numberOfOnes += 1
        if numberOfOnes > half:
            gammaRate += '1'
            epsilon += '0'
        else:
            gammaRate += '0'
            epsilon += '1'
    
    result1 = int(gammaRate, 2) * int(epsilon, 2)

    oxygenGeneratorRating = calculateRating(puzzle, numberOfBits, True)
    co2ScrubberRating = calculateRating(puzzle, numberOfBits, False)

    result2 = int(oxygenGeneratorRating, 2) * int(co2ScrubberRating, 2)

    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2021, 3)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()