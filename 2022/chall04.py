from time import time

from module import getPuzzleInputFromFile

def play(puzzleInput):
    puzzle = [[section.split('-') for section in pair.split(',')] for pair in puzzleInput.split('\n')[:-1]]

    result1 = 0
    result2 = 0

    # PART 1
    for elvesPair in puzzle:
        plusOne = False
        if (int(elvesPair[0][0]) <= int(elvesPair[1][0]) and int(elvesPair[0][1]) >= int(elvesPair[1][1])):
            plusOne = True
        if (int(elvesPair[0][0]) >= int(elvesPair[1][0]) and int(elvesPair[0][1]) <= int(elvesPair[1][1])):
            plusOne = True
        if(plusOne):
            result1 += 1

    # PART 2
    for elvesPair in puzzle:
        plusOne = False
        if (int(elvesPair[0][0]) < int(elvesPair[1][0]) and int(elvesPair[0][1]) < int(elvesPair[1][0])):
            plusOne = True
        if (int(elvesPair[0][0]) > int(elvesPair[1][1]) and int(elvesPair[0][1]) > int(elvesPair[1][1])):
            plusOne = True
        if(plusOne):
            result2 += 1

    # I don't know how to read correctly (:
    result2 = len(puzzle) - result2

    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2022, 4)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()