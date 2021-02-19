input = open("day12input.txt", "r").read().splitlines()

testInput = [
'F10',
'N3',
'F7',
'R90',
'F11'
]

def North(pos, val):
    return(pos[0]+val, pos[1], pos[2])

def South(pos, val):
    return(pos[0]-val, pos[1], pos[2])

def East(pos, val):
    return(pos[0], pos[1]+val, pos[2])

def West(pos, val):
    return(pos[0], pos[1]-val, pos[2])

def Right(pos, val):
    newDir = pos[2] + val
    if newDir > 359:
        newDir = newDir % 360
    return(pos[0], pos[1], newDir)

def Left(pos, val):
    newDir = pos[2] - val
    if newDir < 0:
        newDir = newDir + 360
    return(pos[0], pos[1], newDir)


faceMap = {
    0 : North,
    90 : East,
    180 : South,
    270 : West,
}

def Forward(pos, val):
    return(faceMap[pos[2]](pos,val))

opCodes = {
    'N' : North,
    'S' : South,
    'E' : East,
    'W' : West,
    'L' : Left,
    'R' : Right,
    'F' : Forward
}


def run(pos, input):
    for line in input:
        inst = line[0]
        val = int(line[1:])
        pos = opCodes[inst](pos, val)
    print(abs(pos[0])+abs(pos[1]))

run((0,0,90), testInput)
run((0,0,90), input)


### PART 2

def NorthWp(pos, val):
    return(pos[0]+val, pos[1])

def SouthWp(pos, val):
    return(pos[0]-val, pos[1])

def EastWp(pos, val):
    return(pos[0], pos[1]+val)

def WestWp(pos, val):
    return(pos[0], pos[1]-val)

def RightWp(pos, val):
    if val == 90:
        return(-pos[1], pos[0])
    elif val == 180:
        return(-pos[0], -pos[1])
    else:
        return(pos[1], -pos[0])

def LeftWp(pos, val):
    if val == 90:
        return(pos[1], -pos[0])
    elif val == 180:
        return(-pos[0], -pos[1])
    else:
        return(-pos[1], pos[0])

opCodesWp = {
    'N' : NorthWp,
    'S' : SouthWp,
    'E' : EastWp,
    'W' : WestWp,
    'L' : LeftWp,
    'R' : RightWp,
}

def runWp(input):
    wayp = (1,10)
    pos = (0,0)
    for line in input:
        inst = line[0]
        val = int(line[1:])
        if inst == 'F':
            pos = (pos[0] + wayp[0]*val, pos[1]+wayp[1]*val)
        else:
            wayp = opCodesWp[inst](wayp, val)
        #print(f'{inst}{val} {wayp} {pos}')
    print(abs(pos[0])+abs(pos[1]))

runWp(testInput)
runWp(input)
