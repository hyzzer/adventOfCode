from time import time

from module import getPuzzleInputFromFile

def play(puzzleInput):    
    result1 = 0
    result2 = 0

    # Data parsing
    puzzle = [[coordinates.split('=')[1] for coordinates in line.split(' ') if coordinates[0] in ['x', 'y']] for line in puzzleInput.split('\n')[:-1]]
    for line in puzzle:
        for valueIdx in range(4):
            if valueIdx <= 2:
                line[valueIdx] = line[valueIdx][:-1]
            line[valueIdx] = int(line[valueIdx])

    for line in puzzle:
        line.append(abs(line[0] - line[2]) + abs(line[1] - line[3]))
    
    # PART 1
    yReference = 2000000
    beaconsOnReferenceRow = []
    for line in puzzle:
        if line[3] == yReference:
            beaconsOnReferenceRow.append(line[2])
    impossibleBeacons = []
    for line in puzzle:
        if line[1] - line[4] <= yReference <= line[1] + line[4]:
            delta = line[4] - abs(line[1] - yReference)
            leftOnReference = line[0] - delta
            rightOnReference = line[0] + delta
            for beaconIdx in range(leftOnReference, rightOnReference + 1):
                if beaconIdx not in beaconsOnReferenceRow:
                    impossibleBeacons.append(beaconIdx)
    result1 = len(set(impossibleBeacons))

    # PART 2
    maxCoordinate = 4000000
    def hasEmptyPosition(intervalsList):
        intervalsList.sort()
        if intervalsList[0][0] != 0:
            return 0
        right = 1
        for intervalIdx in range(len(intervalsList)):
            if intervalsList[intervalIdx][1] > right:
                if intervalsList[intervalIdx][0] <= right:
                    right = intervalsList[intervalIdx][1]
                else:
                    return intervalsList[intervalIdx][0] - 1
        return None

    yReference2 = 0
    while result2 == 0 and yReference2 != maxCoordinate:
        signalsIntervals = []
        for line in puzzle:
            if line[1] - line[4] <= yReference2 <= line[1] + line[4]:
                delta = line[4] - abs(line[1] - yReference2)
                leftOnReference2 = line[0] - delta
                leftOnReference2 = 0 if leftOnReference2 < 0 else leftOnReference2
                rightOnReference2 = line[0] + delta
                rightOnReference2 = maxCoordinate if rightOnReference2 > maxCoordinate else rightOnReference2
                signalsIntervals.append([leftOnReference2, rightOnReference2])
        resultX = hasEmptyPosition(signalsIntervals)
        if resultX:
            result2 = resultX * 4000000 + yReference2
        yReference2 += 1
    return result1, result2

def main():
    start = time()
    
    puzzle = getPuzzleInputFromFile(2022, 15)
    result1, result2 = play(puzzle)
    print("Result 1 :", result1)
    print("Result 2 :", result2)

    end = time()
    print("Execution time : ", end - start)

if __name__ == "__main__":
    main()