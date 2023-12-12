with open('../inputs/2') as raw:
    Instr = [x.strip().split(' ') for x in raw.readlines()]


def part1():
    yval = 0
    xval = 0

    for instruction in Instr:
        match instruction[0]:
            case 'down':
                yval += int(instruction[1])
            case 'up':
                yval -= int(instruction[1])
            case 'forward':
                xval += int(instruction[1])

    print(f"\nPart 1\nanswer is: {xval * yval}\n")


def part2():
    xval = 0
    yval = 0
    aim = 0

    for instruction in Instr:
        dirval = int(instruction[1])
        match instruction[0]:
            case 'down':
                aim += dirval
            case 'up':
                aim -= dirval
            case 'forward':
                xval += dirval
                yval += aim * dirval

    print(f"Part 2\nanswer is: {xval * yval}\n")


if __name__ == '__main__':
    part1()
    part2()
