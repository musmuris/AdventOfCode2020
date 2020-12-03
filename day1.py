
input = [int(l) for l in open("day1input.txt", "r").readlines()]

def part1():
    for n in input:
        for n2 in input:
            if n != n2 and n + n2 == 2020:
                return n*n2
                
def part2():
    for n in input:
        for n2 in input:
            for n3 in input:
                if n + n2 + n3 == 2020:
                    return n*n2*n3

print(part1())
print(part2())