with open("../inputs/1") as foo:
    data = foo.read()


def part1():

    floor = 0

    for x in data:
        if x == "(":
            floor += 1
        elif x == ")":
            floor -= 1

    return floor


def part2():

    floor = 0

    for i, x in enumerate(data):
        if x == "(":
            floor += 1
        elif x == ")":
            floor -= 1

        if floor == -1:
            return i+1


print(part1())
print(part2())



