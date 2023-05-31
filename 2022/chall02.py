from time import time

from module import getPuzzleInputFromFile

def play(puzzleInput): 
    puzzle = puzzleInput.split('\n')[:-1]

    result1 = 0
    result2 = 0

    # PART 1
    referencePoint1 = [1, 2, 3, 1]

    for fight in puzzle:
        opponent = ord(fight[0])-64
        me = ord(fight[2])-87
        if me == opponent:
            result1 += 3 + me
        elif (referencePoint1[me] == opponent):
            result1 += me
        else:
            result1 += 6 + me

    # PART 2
    referencePoint2 = [3, 1, 2, 3]

    for fight in puzzle:
        opponent2 = ord(fight[0])-64
        me2 = ord(fight[2])-87
        if me2 == 1:
            result2 += referencePoint2[opponent2-1]
        elif me2 == 2:
            result2 += 3 + referencePoint2[opponent2]
        else:
            result2 += 6 + referencePoint2[(opponent2+1)%3]

    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2022, 2)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()