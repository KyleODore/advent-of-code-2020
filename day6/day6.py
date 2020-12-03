input = open("./input.txt")
lines = list(input.readlines())

# part1
total = 0
s = set()
for line in lines:
    line = line.rstrip("\n")
    if len(line) != 0:
        for c in line:
            s.add(c)
    else:
        total += len(s)
        # print(line, len(s))
        s.clear()
print(total)

# part2
total2 = 0
people = 0
s = {}
for line in lines:
    line = line.rstrip("\n")
    if len(line) != 0:
        for c in line:
            if c in s.keys():
                s.update({c: s.get(c) + 1})
            else:
                s[c] = 1
        people += 1
    else:
        for key in s.keys():
            if s[key] == people:
                total2 += 1
        s.clear()
        people = 0
print(total2)