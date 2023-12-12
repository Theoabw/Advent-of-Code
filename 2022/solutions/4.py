def solution():
    with open("../inputs/4") as IN:
        data = IN.read().split("\n")
        data = [[[int(num) for num in r.split("-")] for r in pair.split(",")] for pair in data if pair]

    score1 = 0
    score2 = 0

    for pair in data:
        per1 = range(pair[0][0], pair[0][1] + 1)
        per2 = range(pair[1][0], pair[1][1] + 1)
        s1 = all(elem in per2 for elem in per1)
        s2 = all(elem in per1 for elem in per2)

        if s1 or s2:
            score1 += 1

        if set(per1) & set(per2):
            score2 += 1

    return score1, score2


p1, p2 = solution()
print(p1, p2)
