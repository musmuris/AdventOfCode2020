
input = open("day2input.txt", "r").read().splitlines()

validPolicy1 = 0
validPolicy2 = 0

for line in input:
    (policy,password) = line.split(': ')
    (vals, char) = policy.split()
    (v1,v2) = vals.split('-')
    (min,max) = (int(v1), int(v2))
    
    charCount = 0 
    found1 = False
    found2 = False
    loc = 1       
    for c in password:         
        if c == char:
            charCount += 1
            if loc == min:
                found1 = True
            if loc == max:
                found2 = True
        loc += 1
    if charCount >= min and charCount <= max:
        validPolicy1 += 1
    if found1 != found2:
        validPolicy2 += 1
    
print(validPolicy1)
print(validPolicy2)
