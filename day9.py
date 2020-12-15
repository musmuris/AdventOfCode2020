input = open("day9input.txt", "r").read().splitlines()

input = [int(x) for x in input]

testinput = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]


def findResult(lookfor, values, start, end):
    for first in range(start, end):
        for second in range(start, end):
            if values[first] != values[second] and values[first] + values[second] == lookfor:
                return True
    return False

def findInvalid(values, windowSize):
    pos = windowSize
    while pos < len(values):
        if not findResult(values[pos], values, pos-windowSize, pos):
            return values[pos]
        pos += 1

def findWeakness(values, invalid):
    start = 0
    while start < len(values) - 1:
        end = start + 1
        acc = values[start]
        while end < len(values):
            acc += values[end]
            if acc == invalid:
                range = values[start:end+1] 
                return max(range) + min(range)
            if acc > invalid:
                break
            end += 1
        start += 1
    raise Exception("Didn't find a range :(")

def doBoth(values, windowSize):
    invalid = findInvalid(values, windowSize)
    print(invalid)
    print(findWeakness(values, invalid))
    
doBoth(testinput, 5)
doBoth(input, 25)
