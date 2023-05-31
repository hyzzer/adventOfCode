from time import time

from module import getPuzzleInputFromFile

def play(puzzleInput):
    puzzle = puzzleInput.split('\n')[:-1]

    result1 = 0
    result2 = 0

    H = [0, 0]
    T = [0, 0]

    # PART 1
    allTailPositions1 = [tuple(T)]

    for move in puzzle:
        for i in range(int(move[2:])):
            match move[0]:
                case 'U':
                    H[1] += 1
                case 'D':
                    H[1] -= 1
                case 'R':
                    H[0] += 1
                case 'L':
                    H[0] -= 1
            distance = [H[0] - T[0], H[1] - T[1]]
            if 2 in distance or -2 in distance:
                decision = [distanceElt//abs(distanceElt) if distanceElt != 0 else 0 for distanceElt in distance]
                T[0] += decision[0]
                T[1] += decision[1]
                allTailPositions1.append(tuple(T))


    result1 = len(list(set(allTailPositions1)))

    # PART 2
    rope = [[0, 0] for i in range(10)]
    allTailPositions2 = [tuple(rope[9])]

    for move in puzzle:
        for i in range(int(move[2:])):
            match move[0]:
                case 'U':
                    rope[0][1] += 1
                case 'D':
                    rope[0][1] -= 1
                case 'R':
                    rope[0][0] += 1
                case 'L':
                    rope[0][0] -= 1
            for j in range(9):
                distance = [rope[j][0] - rope[j+1][0], rope[j][1] - rope[j+1][1]]
                if 2 in distance or -2 in distance:
                    decision = [distanceElt//abs(distanceElt) if distanceElt != 0 else 0 for distanceElt in distance]
                    rope[j+1][0] += decision[0]
                    rope[j+1][1] += decision[1]
                    if j+1 == 9:
                        allTailPositions2.append(tuple(rope[j+1]))

    result2 = len(list(set(allTailPositions2)))
    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2022, 9)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()