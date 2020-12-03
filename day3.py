
input = open("day3input.txt", "r").read().splitlines()

def traverse(right, down):
    loc = 0
    trees = 0
    for lineInx in range(0,len(input),down):
        line = input[lineInx]
        if line[loc] == '#':
            trees += 1
        loc = (loc+right)%len(line)
    return trees

slope31 = traverse(3,1)

print(slope31)

slope11 = traverse(1,1)
slope51 = traverse(5,1)
slope71 = traverse(7,1)
slope12 = traverse(1,2)

print( slope11 * slope31 * slope51 * slope71 * slope12 )


