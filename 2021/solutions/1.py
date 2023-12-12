with open('../inputs/1') as raw:
    List = [int(num) for num in raw.readlines()]


def part1():
    z = 0

    for i, j in enumerate(List[:-1]):
        if j < List[i + 1]:
            z += 1

    return z


def part2():
    List3 = []
    z = 0

    for i, j in enumerate(List[:-2]):
        List3.append(int(j) + int(List[i + 1]) + int(List[i + 2]))

    for k, l in enumerate(List3[:-1]):
        if l < List3[k + 1]:
            z += 1
    return z


if __name__ == '__main__':
    print('Answer for part 1:', part1())
    print('Answer for part 2:', part2())
