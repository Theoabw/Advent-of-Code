with open("../inputs/2") as raw:
    instructions = [
        [[color.strip().split(" ") for color in item.strip().split(",")] for item in line.split(":")[1].split(";")] for
        line in raw.read().split("\n") if line]

counter = []
for game in instructions:
    sublist = [[0], [0], [0]]
    for game_round in game:
        for color in game_round:
            if color[1] == "red":
                sublist[0].append(int(color[0]))
            elif color[1] == "green":
                sublist[1].append(int(color[0]))
            elif color[1] == "blue":
                sublist[2].append(int(color[0]))

    counter.append([max(color) for color in sublist])


def part1():
    # 12 13 14
    valid_games = []
    for game in list(enumerate(counter, 1)):
        if game[1][0] <= 12 and game[1][1] <= 13 and game[1][2] <= 14:
            valid_games.append(game)

    return sum([game[0] for game in valid_games])


def part2():
    power_list = [color[0] * color[1] * color[2] for color in counter]

    return sum(power_list)


print(f"part 1: {part1()}")
print(f"part 2: {part2()}")
