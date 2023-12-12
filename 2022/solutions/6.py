with open('../inputs/6') as IN:
    data = IN.read().split('\n')[0]


def part1(data_in):
    mem = [letter for letter in data_in[:4]]
    ans = 0

    for index, letter in enumerate(data_in[4:]):
        a = len(set(mem))
        b = len(mem)
        if a == b:
            ans = index + 4
            break
        else:
            mem.append(letter)
            mem = mem[1:]
    return ans


def part2(data_in):
    mem = [letter for letter in data_in[:14]]
    ans = 0

    for index, letter in enumerate(data_in[14:]):
        a = len(set(mem))
        b = len(mem)
        if a == b:
            ans = index + 14
            break
        else:
            mem.append(letter)
            mem = mem[1:]
    return ans


print(part1(data))
print(part2(data))
