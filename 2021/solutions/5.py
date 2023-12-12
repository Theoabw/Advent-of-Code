from collections import Counter

with open('../inputs/5') as raw:
    coordintr = raw.readlines()

coordlist = []

#TODO: fix this whole thing

for row in coordintr:
    x1, y1 = tuple(map(int, (row.strip('\n').split(' -> ')[0].split(','))))
    x2, y2 = tuple(map(int, (row.strip('\n').split(' -> ')[1].split(','))))

    if x1 == x2 and y1 < y2:
        for coord in range(y1, y2 + 1):
            coordlist.append((x1, coord))

    elif x1 == x2 and y2 < y1:
        for coord in range(y2, y1 + 1):
            coordlist.append((x1, coord))

    elif y1 == y2 and x1 < x2:
        for coord in range(x1, x2 + 1):
            coordlist.append((coord, y1))

    elif y1 == y2 and x2 < x1:
        for coord in range(x2, x1 + 1):
            coordlist.append((coord, y1))

    elif x1 != x2 and y1 != y2:
        if x1 < x2 and y1 < y2:
            for x, y in zip(range(x1, x2 + 1), range(y1, y2 + 1)):
                coordlist.append((x, y))

        elif x2 < x1 and y2 < y1:
            for x, y in zip(range(x2, x1 + 1), range(y2, y1 + 1)):
                coordlist.append((x, y))

        elif x1 < x2 and y2 < y1:
            for x, y in zip(range(x1, x2 + 1), range(y2, y1 + 1)):
                coordlist.append((x, y))

        elif x2 < x1 and y1 < y2:
            for x, y in zip(range(x2, x1 + 1), range(y1, y2 + 1)):
                coordlist.append((x, y))

print(Counter(coordlist))
print(len([x for x in Counter(coordlist).values() if x > 1]))

# TODO: fix this
# 21766 is too high
