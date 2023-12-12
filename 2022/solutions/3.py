import string


def solution():
    with open("../inputs/3") as IN:
        data = [foo for foo in IN.read().split("\n") if foo]
        data1 = [(x[:len(x)//2], x[len(x)//2:]) for x in data]
        data2 = [data[i:i+3] for i in range(0, len(data), 3)]

    scoring = list(string.ascii_letters)
    priority = dict(zip(scoring, range(1, len(scoring) + 1)))

    processed1 = [''.join(set(line[0]) & set(line[1])) for line in data1]
    processed2 = [''.join(set(x[0]) & set(x[1]) & set(x[2])) for x in data2]

    is1 = sum(priority[item] for item in processed1)
    is2 = sum(priority[item] for item in processed2)

    return is1, is2


p1, p2 = solution()
print(f"Answer for part 1: {p1}")
print(f"Answer for part 2: {p2}")
