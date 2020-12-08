input = open("day5input.txt", "r").read().splitlines()

# The codes actually just boil down to a 10 bit number
# (the give away is that the last three digits cover the columns 0-7.
# Then you multiply the first 7 'bits' by 8. Sound familar? )
replaces = {
    'F' : '0',
    'B' : '1',
    'L' : '0',    
    'R' : '1'
}
allseats = []
for line in input:
    bin = ''.join([replaces[c] for c in line])
    val = int(bin, 2)
    allseats.append(val)    

allseats.sort()
print(allseats[-1])

prev = allseats[0]
for seat in allseats[1:]:
    if seat != prev + 1:
        break
    prev = seat

print(prev+1)