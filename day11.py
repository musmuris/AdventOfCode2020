input = open("day11input.txt", "r").read().splitlines()

testInput = [
'L.LL.LL.LL',
'LLLLLLL.LL',
'L.L.L..L..',
'LLLL.LL.LL',
'L.LL.LL.LL',
'L.LLLLL.LL',
'..L.L.....',
'LLLLLLLLLL',
'L.LLLLLL.L',
'L.LLLLL.LL'
]

def countAdjancent(layout, x, y):
    count = 0
    for dy in range(-1,2):
        for dx in range(-1,2):
            if dy == 0 and dx == 0 : continue
            if y+dy < 0 or y+dy >= len(layout) : continue
            if x+dx < 0 or x+dx >= len(layout[y]): continue
            if layout[y+dy][x+dx] == '#':
                count += 1
    return count

def itterate(layout):    
    change = False
    newLayout = []
    for y in range(0,len(layout)):
        newRow=""
        for x in range(0, len(layout[y])):
            if layout[y][x] == '.':
                newRow += '.'
                continue
            adj = countAdjancent(layout, x, y)
            if adj >= 4 and layout[y][x]=='#':
                newRow += ('L')
            elif adj == 0 and layout[y][x]=='L':
                newRow += ('#')
            else:
                newRow += layout[y][x]

            if newRow[-1] != layout[y][x]:
                change = True
        newLayout.append(newRow)
    return (change, newLayout)

def fillSeats(layout):            
    while True:
        (changes,layout) = itterate(layout)
        if not changes:
            return "".join(layout).count('#')

print(fillSeats(testInput))
print(fillSeats(input))


