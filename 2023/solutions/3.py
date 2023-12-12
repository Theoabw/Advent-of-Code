with open("../inputs/3") as raw:
    txt_in = raw.read().splitlines()

numslist = []
symlist = []

for y, line in enumerate(txt_in):
    num = ""
    start_x = 0
    for x, char in enumerate(line):
        char: str
        # booleans for if the previous, current, and the next char are digits
        prev_digit = line[x - 1].isdigit() if x >= 1 else False
        digit = char.isdigit()
        next_digit = line[x + 1].isdigit() if x < (len(line) - 1) else False
        # shortest digit first
        if not prev_digit and digit and not next_digit:
            numslist.append((x, x, y, int(char)))
        # start recording
        elif not prev_digit and digit and next_digit:
            num += char
            start_x = x
        # keep recording
        elif prev_digit and digit and next_digit:
            num += char
        # end recording
        elif prev_digit and digit and not next_digit:
            num += char
            numslist.append((start_x, x, y, int(num)))
            num = ""
        # record pos of symbols to a list
        elif not digit and char != ".":
            symlist.append((x, y))


def matrixcreator(x, y):
    # create an area of coordinates to check if a number is within range
    valid_coords = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            valid_coords.append((i, j))
    return valid_coords


def part1():
    relevantnums = []

    for sym in symlist:
        area = matrixcreator(sym[0], sym[1])
        for num in numslist:
            if ((num[0], num[2]) in area or (num[1], num[2]) in area) and num not in relevantnums:
                relevantnums.append(num)

    return sum([foo[3] for foo in relevantnums])


def part2():
    relevantnums = []
    gear_ratios = []

    for sym in symlist:
        area = matrixcreator(sym[0], sym[1])
        num_amount = 0
        for num in numslist:
            if ((num[0], num[2]) in area or (num[1], num[2]) in area) and num not in relevantnums:
                relevantnums.append(num[3])
                num_amount += 1
        if num_amount == 2:
            gear_ratios.append(relevantnums[-1]*relevantnums[-2])
        elif num_amount == 1:
            relevantnums = relevantnums[:-1]
        elif num_amount > 2:
            relevantnums = relevantnums[:-num_amount]

    return sum(gear_ratios)


print(f"part 1: {part1()}")
print(f"part 2: {part2()}")
