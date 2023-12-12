inp = [x.split(' ') for x in open('../inputs/2').read().split('\n') if x]
# draw, win, loss, points dicts
# A, X = rock, B, Y = paper, C, Z = scissors
table = ({'A': 'X', 'B': 'Y', 'C': 'Z'},
         {'A': 'Y', 'B': 'Z', 'C': 'X'},
         {'A': 'Z', 'B': 'X', 'C': 'Y'},
         {'X': 1, 'Y': 2, 'Z': 3})


def part1(i, t):

    win, loss, points = t[1], t[2], t[3]
    score = 0

    for me, move in i:
        if loss[me] == move:
            score += points[move]
        elif win[me] == move:
            score += 6 + points[move]
        else:
            score += 3 + points[move]

    return score


def part2(i, t):

    draw, win, loss, points = t[0], t[1], t[2], t[3]
    score = 0

    for me, move in i:
        if move == 'X':
            score += points[loss[me]]
        elif move == 'Z':
            score += 6 + points[win[me]]
        else:
            score += 3 + points[draw[me]]

    return score


print(f"P1 Ans: {part1(inp,table)}")
print(f"P2 Ans: {part2(inp,table)}")
