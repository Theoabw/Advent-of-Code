with open("../inputs/2") as input_data:
    dimensions = [tuple(map(int, foo.split("x"))) for foo in input_data.read().split("\n") if foo]


def part1():
    area_list = []
    for box in dimensions:
        sides = [box[0] * box[1], box[0] * box[2], box[1] * box[2]]
        extra_area = min(sides)
        area = 2 * sides[0] + 2 * sides[1] + 2 * sides[2]
        area_list.append(area + extra_area)
    return sum(area_list)


def part2():
    ribbon_list = []
    for box in dimensions:
        sides = [box[0] + box[1], box[0] + box[2], box[1] + box[2]]
        perimeter = 2*min(sides)
        bow = box[0] * box[1] * box[2]
        ribbon_list.append(perimeter + bow)
    return sum(ribbon_list)


print(part1())
print(part2())
