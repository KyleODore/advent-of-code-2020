input = open("./input.txt")
lines = list(input.readlines())
for line in lines:
    line = line.rstrip('\n')
height = len(lines)
width = len(lines[0])
# print(height, width, lines[0])

def slope(x, y):
    h = 0
    w = 0
    count = 0
    while h < height - 1:
        w = (w + x) % (width - 1)
        h += y
        if lines[h][w] == "#":
            count += 1
    return count

# part1
print(slope(3,1))

# part2
print(slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2))