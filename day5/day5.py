input = open("./input.txt")
lines = list(input.readlines())

# part1
max = 0

# part2
w, h = 8, 128
matrix = [[0 for x in range(w)] for y in range(h)]

for line in lines:
    front = 0
    back = 127
    for i in range(7):
        mid = int((back - front) / 2)
        if line[i] == "F":
            back -= mid
        else:
            front = back - mid
    left = 0
    right = 7
    for i in range(7,10):
        mid = int((right - left) / 2)
        if line[i] == "L":
            right -= mid
        else:
            left = right - mid
    id = front * 8 + left
    if id > max:
        max = id
    matrix[front][left] = "X"
print("max =", max)

count = 0
for row in matrix:
    print(count, row)
    count += 1

print(72 * 8 + 7)
