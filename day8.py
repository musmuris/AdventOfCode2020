import re

input = open("day8input.txt", "r").read().splitlines()

testinput = [
"nop +0",
"acc +1",
"jmp +4",
"acc +3",
"jmp -3",
"acc -99",
"acc +1",
"jmp -4",
"acc +6",
]


def executeProgram(instructions):
    def nop(arg, pc, accum):
        return (pc,accum)

    def acc(arg, pc, accum):
        accum = accum + int(arg)
        return (pc,accum)

    def jmp(arg, pc, accum):    
        pc += int(arg) - 1
        return (pc,accum)

    instructionSet = {
        "nop" : nop,
        "acc" : acc,
        "jmp" : jmp
    }

    instRex = re.compile(r"(\w\w\w) (.\d+)")
    hit = set()
    (pc,accum) = (0,0)
    while not pc in hit and pc < len(instructions):
        hit.add(pc)
        inst, arg = instRex.findall(instructions[pc])[0]
        (pc,accum) = instructionSet[inst](arg, pc, accum)
        pc = pc + 1
    return (pc,accum)

print(executeProgram(testinput))
print(executeProgram(input))

# part 2
# Brute force approach - change one at a time and run it
# Did wonder about a branching model - i.e. each time you hit a nop or jmp
# clone the list and state at that point onto a queue and carry on.
# Then just work down the queue, adding more clones until you find one that works.
# But this works quick enough! 
for i in range(0,len(input)):
    if input[i].startswith('acc'):
        continue
    modifiedInput = input[:]
    if input[i].startswith('nop'):
        modifiedInput[i] = modifiedInput[i].replace('nop','jmp')
    else:
        modifiedInput[i] = modifiedInput[i].replace('jmp','nop')
    (pc,accum) = executeProgram(modifiedInput)
    if pc >= len(modifiedInput):
        print((pc,accum))
        break

    


    
