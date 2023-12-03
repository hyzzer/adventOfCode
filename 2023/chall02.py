from time import time

from module import getPuzzleInputFromFile

def play(puzzleInput): 
    puzzle = puzzleInput[:-1].split('\n')

    result1 = 0
    result2 = 0

    numberOfCubes = [12, 13, 14]

    # PART 1
    sortedPuzzle = []
    for gameIdx, game in enumerate(puzzle):
        isGood = True
        games = [set.split(', ') for set in game.split(': ')[1].split(';')]
        gameTmp = []
        for sets in games:
            setTmp = [0, 0, 0]
            for set in sets:
                splittedSet = set.strip().split(' ')
                if splittedSet[1] == 'red':
                    setTmp[0] = int(splittedSet[0])
                    if setTmp[0] > numberOfCubes[0]:
                        isGood = False
                elif splittedSet[1] == 'green':
                    setTmp[1] = int(splittedSet[0])
                    if setTmp[1] > numberOfCubes[1]:
                        isGood = False
                else:
                    setTmp[2] = int(splittedSet[0])
                    if setTmp[2] > numberOfCubes[2]:
                        isGood = False
            gameTmp.append(setTmp)
        sortedPuzzle.append(gameTmp)
        if isGood:
            result1 += gameIdx + 1        

    # PART 2
    for game in sortedPuzzle:
        redPower = 0
        greenPower = 0
        bluePower = 0
        for set in game:
            if set[0] > redPower:
                redPower = set[0]
            if set[1] > greenPower:
                greenPower = set[1]            
            if set[2] > bluePower:
                bluePower = set[2]
        result2 += redPower * greenPower * bluePower

            
    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2023, 2)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()