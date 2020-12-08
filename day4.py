import re

input = open("day4input.txt", "r").read().splitlines()

def readPassports(input):
    passport  = {}
    passports = []
    for line in input:
        if len(line) == 0 and len(passport) > 0:
            passports.append(passport)
            passport = {}
            continue
        entries = line.split(" ")
        for entry in entries:
            (key,val) = entry.split(":")
            passport[key] = val

    if len(passport) > 0:
        passports.append(passport)

    return passports


## Check functions (for part 2)
def chkInt(val, min, max):
    intval = int(val)
    return intval >= min and intval <= max

def chkYear(val, min, max):
    m = re.findall(r"^\d\d\d\d$", val)
    return False if len(m) != 1 else chkInt(m[0], min, max)


def chkByr(val):    
    return chkYear(val, 1920, 2002)

def chkIyr(val):
    return chkYear(val, 2010, 2020)

def chkEyr(val):
    return chkYear(val, 2020, 2030)
    
def chkHgt(val):
    m = re.findall(r"^(\d+)(in|cm)$", val)
    if len(m) != 1 or len(m[0]) != 2: return False
    return chkInt(m[0][0],59,76) if m[0][1] == 'in' else chkInt(m[0][0], 150,193)

def chkHcl(val):    
    return True if re.match(r"^#[0-9a-f]{6}$", val) else False

eyeColours = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
def chkEcl(val):
    return val in eyeColours

def chkPid(val):
    return True if re.match(r"^\d{9}$", val) else False


## Part 1
requiredFields = {"byr","iyr","eyr","hgt","hcl","ecl","pid"}
def checkPassport(passport):
    passfields = set([ k for k in passport.keys() if k != "cid"])
    return len(requiredFields.difference(passfields)) == 0

### Part 2
fieldChecks = {
    "byr" : chkByr,
    "iyr" : chkIyr,
    "eyr" : chkEyr,
    "hgt" : chkHgt,
    "hcl" : chkHcl,
    "ecl" : chkEcl,
    "pid" : chkPid    
}

def checkPassportHarder(passport):
    chkCount = 0
    for k,v in passport.items():
        if k != "cid" and fieldChecks[k](v):
            chkCount = chkCount + 1 
    return chkCount == len(fieldChecks)

passports = readPassports(input)
valids = [p for p in passports if checkPassport(p)]
reallyValids = [p for p in passports if checkPassportHarder(p)]

print( len(valids) )
print( len(reallyValids) )



