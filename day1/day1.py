input = open("./input.txt")
lines = list(input.readlines())
nums = set()
numsl = list()
i = 0
while i < len(lines):
    nums.add(int(lines[i]))
    numsl.append(int(lines[i]))
    i += 1

# part1
for num in nums:
    if (2020 - num) in nums:
        print(num * (2020 - num))
        break

# part2
length = len(numsl)
i = 0
j = i
k = j
while i < length:
    j = i
    while j < length:
        k = j
        while k < length:
            if (numsl[i] + numsl[j] + numsl[k] == 2020):
                print(numsl[i] * numsl[j] * numsl[k])
            k += 1
        j += 1
    i += 1

