with open("../inputs/3") as input_data:
    instructions = [instr for instr in input_data.read()]


def delta_coords(instr):
    delta = [0, 0]
    match instr:

        case ">":
            delta[0] += 1
        case "<":
            delta[0] -= 1
        case "^":
            delta[1] += 1
        case "v":
            delta[1] -= 1

    return delta


def house_tracker(instr):
    x = 0
    y = 0
    tracker = set({})

    for instruction in instr:
        current_coordinate = [x, y]
        hashable_coordinate = f"{tuple(current_coordinate)}"

        if hashable_coordinate not in tracker:
            tracker.add(hashable_coordinate)
        delta_x, delta_y = delta_coords(instruction)
        x += delta_x
        y += delta_y

    return tracker


def part1():
    return len(house_tracker(instructions))


def part2():
    tracker = house_tracker(instructions[0::2])
    tracker.update(house_tracker(instructions[1::2]))
    return len(tracker)


print(part1())
print(part2())
