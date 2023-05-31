from time import time

from module import getPuzzleInputFromFile

def play(puzzleInput):
    puzzle = puzzleInput.split('\n')[:-1]

    result1 = 0
    result2 = '\n'
    
    # PART 1
    cycle = 1
    X = 1

    def checkCycle(cycleArg, xArg, signalsStrengthSum):
        if (cycleArg+20)%40 == 0:
            signalsStrengthSum += (xArg*cycleArg)
        cycleArg += 1
        return cycleArg, xArg, signalsStrengthSum

    for instruction in puzzle:
        if instruction == 'noop':
            cycle, X, result1 = checkCycle(cycle, X, result1)
        else:
            for _ in range(2):
                cycle, X, result1 = checkCycle(cycle, X, result1)
            X += int(instruction.split(' ')[1])

    
    # PART 2
    cycle2 = 0
    sprite = 1
    crt = ''

    def pixelToDraw(cycleArg, spriteArg):
        if spriteArg-1 <= cycleArg <= spriteArg+1:
            return '#'
        else:
            return '.'

    def displayCrt(crtArg):
        result = ''
        for pixelIdx in range(len(crtArg)//40):
            result += crtArg[pixelIdx*40:pixelIdx*40+40] + "\n"
        return result

    for instruction in puzzle:
        numberOfSteps = 1 if instruction == 'noop' else 2
        for _ in range(numberOfSteps):
            crt += pixelToDraw(cycle2%40, sprite)
            cycle2 += 1
        if instruction != 'noop':
            sprite += int(instruction.split(' ')[1])

    result2 += displayCrt(crt)
    
    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2022, 10)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)
    
    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()