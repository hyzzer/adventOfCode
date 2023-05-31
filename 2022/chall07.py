from time import time

from module import getPuzzleInputFromFile

def play(puzzleInput):
    puzzle = puzzleInput.split('\n')
    
    result1 = 0
    result2 = 0

    puzzle[-1] = '$'

    def changeDir(currentDir, argDir):
        if (argDir[0] == '/'):
            return argDir
        if (argDir == '..'):
            return '/'.join(currentDir.split('/')[:-2]) + '/'
        return currentDir + argDir + '/'

    def dirSizeCalculation(listOfCommands, lsCommandIdx):
        idx = lsCommandIdx +1
        result = 0
        while (listOfCommands[idx][0] != '$'):
            if (listOfCommands[idx][0] != 'd'):
                result += int(listOfCommands[idx].split(' ')[0])
            idx += 1
        return result

    currentDir = ''
    dirsSizeDict = {}
    for commandIdx, command in enumerate(puzzle):
        if command[0] == '$':
            if command[2:4] == 'cd':
                currentDir = changeDir(currentDir, command[5:])
            if command[2:4] == 'ls':
                dirsSizeDict.update({currentDir: dirSizeCalculation(puzzle, commandIdx)})

    # PART 1
    realDirSizeDict = {}
    for dir1Key in dirsSizeDict.keys():
        totalForOneDir = 0
        for dir2Key, dir2Value in dirsSizeDict.items():
            if dir2Key[:len(dir1Key)] == dir1Key:
                totalForOneDir += dir2Value
        realDirSizeDict.update({ dir1Key : totalForOneDir})
        if totalForOneDir <= 100000:
            result1 += totalForOneDir

    # PART 2
    freeSpace = 70000000 - realDirSizeDict.get('/')
    targetSpace = 30000000 - freeSpace
    result2 = realDirSizeDict.get('/')

    for dirValue in realDirSizeDict.values():
        if dirValue > targetSpace and dirValue < result2:
            result2 = dirValue
    
    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2022, 7)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()
