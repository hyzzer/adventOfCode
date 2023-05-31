from time import time

from module import getPuzzleInputFromFile

def play(puzzleInput):

    # PART 1 & 2
    def solution(numberOfDistinctChars):
        result = 0
        letterIdx = 0
        while (result == 0):
            if (len(set(puzzleInput[letterIdx:letterIdx+numberOfDistinctChars])) == numberOfDistinctChars):
                    result = letterIdx+numberOfDistinctChars
            letterIdx += 1
        return result
    
    result1 = solution(4)
    result2 = solution(14)

    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2022, 6)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()