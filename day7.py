import re

input = open("day7input.txt", "r").read().splitlines()

# input = [
# "light red bags contain 1 bright white bag, 2 muted yellow bags.",
# "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
# "bright white bags contain 1 shiny gold bag.",
# "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
# "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
# "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
# "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
# "faded blue bags contain no other bags.",
# "dotted black bags contain no other bags."
# ]

# input = [
# "shiny gold bags contain 2 dark red bags.",
# "dark red bags contain 2 dark orange bags.",
# "dark orange bags contain 2 dark yellow bags.",
# "dark yellow bags contain 2 dark green bags.",
# "dark green bags contain 2 dark blue bags.",
# "dark blue bags contain 2 dark violet bags.",
# "dark violet bags contain no other bags."
# ]

contains = {}
reversed = {}

rex = re.compile(r"([\d]*) ?(\w* \w*) bags?")
for line in input:
    matches = rex.findall(line)
    outerBag = matches[0][1]
    contains[outerBag] = {}
    for match in matches[1:]:
        num = match[0]
        col = match[1]
        if col != "no other":
            contains[outerBag][col] = int(num)
            if col not in reversed:
                reversed[col] = set()
            reversed[col].add(outerBag) 
    
toCheck = ["shiny gold"]
canContain = set()
while len(toCheck) > 0:
    next = toCheck.pop()
    if next in reversed:
        for outer in reversed[next]:
            if outer not in canContain:
                canContain.add(outer)
                toCheck.append(outer)

print(len(canContain))

def recurseBags(color):
    if color not in contains:
        return 1
    count = 1
    for col,num in contains[color].items():
        count = count + num * recurseBags(col)
    return count

# -1 as we already "own" the shiny gold bag!
print(recurseBags("shiny gold")-1)
