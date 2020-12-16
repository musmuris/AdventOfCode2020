from functools import reduce
from operator import mul


input = open("day10input.txt", "r").read().splitlines()
input = [int(x) for x in input]

testinput = [
    28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 
    38, 39, 11,  1, 32, 25, 35,  8, 17,  7,  9,  4,  2, 34, 10, 3 
]

def findAnswer(values):
    prev = 0
    diff3 = 0
    diff1 = 0
    for v in sorted(values):
        if prev + 1 == v:
            diff1 += 1
        elif prev + 3 == v:
            diff3 += 1
        else:
            raise Exception(f"Diff of {v-prev} + found")
        prev = v
    diff3 += 1
    return diff1 * diff3



# The numvbers are split into blocks of contignous numbers, separated
# by ones where it's +3 (we know from part 1 there are no +2 deltas)
# When it's +3 there is only 1 choice, so if we work out all permutations
# of each contiguous block then multiply
def findArrangemnts(values):

    # Given a sequence of N numbers, recurse down tres of possible arrangements
    # It actually gives out "tribonacci" numbers so 0 1 1 2 4 7 13 24 for 
    # n = 0,1,2,3,4,5,5,7 etc. but I had never heard of these till I saw other solutions
    # And I haven't understood (or even looked into) why that is the case
    def countContiguousArrangements(numContiguousVals):
        def recurse(values):
            if len(values) == 1:
                return 1
            subTrees = 0
            inx = 1    
            while inx < len(values) and values[inx] <= values[0] + 3:    
                subTrees += recurse(values[inx:])
                inx += 1
            return subTrees
        return recurse(list(range(1,numContiguousVals+1)))

    # Store the recursion reults 
    contigLookup = {}
    def handleBlock(size):
        if size not in contigLookup:
            contigLookup[size] = countContiguousArrangements(size)
        return contigLookup[size]        

    acc = 1
    prev = 0
    contigCount = 1  
    values.append(max(values) + 3)
    for v in sorted(values):        
        if prev + 1 == v:
            contigCount += 1
        elif prev + 3 == v:
            acc *= handleBlock(contigCount)
            contigCount = 1
        else:
            raise Exception(f"Diff of {v-prev} + found")
        prev = v
    acc *= handleBlock(contigCount)
    return acc
    
print(findAnswer(testinput))
print(findAnswer(input))

print(findArrangemnts(testinput))
print(findArrangemnts(input))

