input = open("./input.txt")
lines = list(input.readlines())

# part1
def valid(string):
    return "byr:" in string and \
        "iyr:" in string and \
        "eyr:" in string and \
        "hgt:" in string and \
        "hcl:" in string and \
        "ecl:" in string and \
        "pid:" in string

# part2
def superValid(string):
    validItems = True
    splitStr = string.split(" ")
    # print(splitStr)
    for field in splitStr[1:]:
        items = field.split(":")
        # print(len(items), len(items) == 2)
        if len(items) == 2:
            if items[0] == "byr":
                if int(items[1]) > 2002 or int(items[1]) < 1920:
                    # print("byr")
                    validItems = False
            if items[0] == "iyr":
                if int(items[1]) > 2020 or int(items[1]) < 2010:
                    # print("iyr")
                    validItems = False
            if items[0] == "eyr":
                if int(items[1]) > 2030 or int(items[1]) < 2020:
                    # print("eyr")
                    validItems = False
            if items[0] == "hgt":
                if ("in" in items[1]) or ("cm" in items[1]):
                    val = int(items[1][:-2])
                    if "in" in items[1]:
                        if val > 76 or val < 59:
                            # print("hgt1")
                            validItems = False
                    if "cm" in items[1]:
                        if val > 193 or val < 150:
                            # print("hgt2")
                            validItems = False
                else:
                    # print("hgt3")
                    validItems = False 
            if items[0] == "hcl":
                if items[1][0] == "#":
                    letters = 0
                    numbers = 0
                    total = 0
                    for i in range(1, len(items[1])):
                        if items[1][i].isdigit():
                            numbers += 1
                        else:
                            if ord(items[1][i]) >= ord('a') and ord(items[1][i]) <= ord('f'):
                                letters += 1
                        total += 1
                    if total > 6 or letters + numbers - total > 0:
                        # print("hcl1")
                        validItems = False
                else:
                    validItems = False
                    # print("hcl2")
            if items[0] == "ecl":
                colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                if items[1] not in colors:
                    # print("ecl")
                    validItems = False
            if items[0] == "pid":
                if len(items[1]) != 9 or not items[1].isdigit:
                    # print("pid")
                    validItems = False
        else:
            print("length")
            validItems = False
    return validItems

validCount = 0
superValidCount = 0
passport = ""
for line in lines:
    line = line.rstrip('\n')
    if len(line) == 0:
        # print(passport, count)
        if valid(passport):
            validCount += 1
            if superValid(passport):
                superValidCount += 1
        passport = ""
    else:
        passport += " " + line
print(validCount)
print(superValidCount)