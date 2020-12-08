
input = open("day6input.txt", "r").read().splitlines()

anyone = set()
everyone = set()
anyYeses = []
allYeses = []
for line in input:
    if len(line) == 0:
        anyYeses.append(len(anyone))
        allYeses.append(len(everyone))
        anyone = set()
        everyone = set()
    else:
        chars = [c for c in line]
        # Part 1
        anyone.update(chars)
        # Part 2
        if len(anyone) == 0:
            everyone.update(chars)
        else:
            everyone = everyone.intersection(set(chars))        

if len(anyone) != 0:
    anyYeses.append(len(anyone))

if len(everyone) != 0:
    allYeses.append(len(everyone))

print(sum(anyYeses))
print(sum(allYeses))