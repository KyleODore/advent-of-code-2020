passwords = open("./input.txt")
lines = list(passwords.readlines())

# part1
valid = 0
for line in lines:
    line = line.rstrip('\n')
    main = line.split(": ")
    nums = main[0].split(" ")
    individualNums = nums[0].split("-")
    char = nums[1]
    mini = int(individualNums[0])
    maxi = int(individualNums[1])
    count = 0
    for c in main[1]:
        if c == nums[1]:
            count += 1
    if count <= maxi and count >= mini:
        valid += 1
# print(valid)

# part2
valid2 = 0
for line in lines:
    line = line.rstrip('\n')
    main = line.split(": ")
    nums = main[0].split(" ")
    individualNums = nums[0].split("-")
    char = nums[1]
    mini = int(individualNums[0]) - 1
    maxi = int(individualNums[1]) - 1
    if mini >= 0 and maxi < len(main[1]):
        left = (main[1][mini] == char) and (main[1][maxi] != char)
        right = (main[1][maxi] == char) and (main[1][mini] != char)
        if left or right:
            valid2 += 1
print(valid2)