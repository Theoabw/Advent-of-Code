from math import prod

with open("../inputs/6") as raw:
    full_inp = raw.read().splitlines()
    # time and distance
    t = list(map(int, [foo for foo in full_inp[0].split(":")[1].split(" ") if foo]))
    d = list(map(int, [foo for foo in full_inp[1].split(":")[1].split(" ") if foo]))
    races = tuple(zip(t, d))
    t2 = int("".join([foo for foo in full_inp[0].split(":")[1].split(" ") if foo]))
    d2 = int("".join([foo for foo in full_inp[1].split(":")[1].split(" ") if foo]))
    p2_race = (t2, d2)


def part1():
    countlist = []

    for race in races:
        speed = range(1, race[0])
        distance = []
        for v in speed:
            achieved_distance = v * (race[0] - v)
            if achieved_distance > race[1]:
                distance.append(v * (race[0] - v))

        countlist.append(len(distance))

    return prod(countlist)

def part2():
    count = 0
    speed = range(1, p2_race[0])
    for v in speed:
        achieved_distance = v * (p2_race[0] - v)
        if achieved_distance > p2_race[1]:
            count += 1

    return count


print(part1())
print(part2())
