with open('../inputs/9') as raw:
    depthlist = raw.read().split("\n")
    depthlist = [[int(y) for y in x] for x in depthlist]


def part1():
    numlist = []
    for di, line in enumerate(depthlist):
        for ni, num in enumerate(line):
            try:
                up = depthlist[di - 1][ni]
            except IndexError:
                pass
            try:
                down = depthlist[di + 1][ni]
            except IndexError:
                pass
            try:
                left = line[ni - 1]
            except IndexError:
                pass
            try:
                right = line[ni + 1]
            except IndexError:
                pass

            if di != 0 and di != (len(depthlist) - 1) and ni != 0 and ni != (len(line) - 1):
                if num < up and num < down and num < left and num < right:
                    numlist.append(num + 1)

            # edges and corners
            # up side
            elif di == 0 and ni == 0:
                if num < down and num < right:
                    numlist.append(num + 1)
            elif di == 0 and ni != 0 and ni != (len(line) - 1):
                if num < down and num < left and num < right:
                    numlist.append(num + 1)
            elif di == 0 and ni == (len(line) - 1):
                if num < down and num < left:
                    numlist.append(num + 1)
            # down side
            elif di == (len(depthlist) - 1) and ni == 0:
                if num < up and num < right:
                    numlist.append(num + 1)
            elif di == (len(depthlist) - 1) and ni != 0 and ni != (len(line) - 1):
                if num < up and num < left and num < right:
                    numlist.append(num + 1)
            elif di == (len(depthlist) - 1) and ni == (len(line) - 1):
                if num < up and num < left:
                    numlist.append(num + 1)
            # left and right side
            elif di != 0 and di != (len(depthlist) - 1) and ni == 0:
                if num < up and num < down and num < right:
                    numlist.append(num + 1)
            elif di != 0 and di != (len(depthlist) - 1) and ni == (len(line) - 1):
                if num < up and num < down and num < left:
                    numlist.append(num + 1)

    print(sum(numlist))


part1()

# I'll return to part 2 at some point
