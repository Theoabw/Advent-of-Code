with open('../inputs/8', 'r') as raw:
    rawread = raw.read()
    # split the input on the right side of the | into lists and sort it
    Linstr = [[(y.split()) for y in [x[0] for x in [i.split('|') for i in rawread.splitlines()]]]][0]
    Linstr = [[''.join(sorted(y)) for y in z] for z in Linstr]
    Rinstr = [[(y.split()) for y in [x[1] for x in [i.split('|') for i in rawread.splitlines()]]]][0]
    Rinstr = [[''.join(sorted(y)) for y in z] for z in Rinstr]


def part1():
    countdict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0}

    for row in Rinstr:
        for number in row:
            if len(number) == 2:
                countdict[1] += 1

            elif len(number) == 3:
                countdict[7] += 1

            elif len(number) == 4:
                countdict[4] += 1

            elif len(number) == 7:
                countdict[8] += 1

    countsum = 0
    for x in range(10):
        countsum += countdict[x]

    print(f"sum of the numbers is: {countsum}")


# This took a while..
def part2():
    numdict = {  # dictonary to keep track of the mapping
        0: '',
        1: '',
        2: '',
        3: '',
        4: '',
        5: '',
        6: '',
        7: '',
        8: '',
        9: ''}

    def decrypter(inline: list):

        for string in sorted(inline, key=len):
            if len(string) == 2:
                numdict[1] = string
            elif len(string) == 3:
                numdict[7] = string
            elif len(string) == 4:
                numdict[4] = string
            elif len(string) == 7:
                numdict[8] = string

            # ''.join(sorted([x for x in numdict[4] if x not in numdict[1]])) means 4 - 1 letterwise
            # ''.join([x for x in string if x in numdict[1]]) filters out all other letters which aren't in the num 1
            # primarily used to see if string contains num 1's pattern
            # The following code isn't very readable, but at least it works
            # TODO: make the following more readable..

            elif len(string) == 5:
                includedin5or9 = ''.join(sorted([x for x in numdict[4] if x not in numdict[1]]))
                if includedin5or9 == ''.join([x for x in string if x in includedin5or9]):
                    numdict[5] = string
                else:
                    if numdict[1] == ''.join([x for x in string if x in numdict[1]]):
                        numdict[3] = string
                    else:
                        numdict[2] = string
            elif len(string) == 6:
                if numdict[1] == ''.join([x for x in string if x in numdict[1]]):
                    if includedin5or9 == ''.join([x for x in string if x in includedin5or9]):
                        numdict[9] = string
                    else:
                        numdict[0] = string
                else:
                    numdict[6] = string

    partsum = 0
    for leftline, rightline in zip(Linstr, Rinstr):
        decrypter(leftline)
        numstring = ''
        for Resultstring in rightline:
            for i in range(10):
                if ''.join(sorted(Resultstring)) == ''.join(sorted(numdict[i])):
                    numstring += f'{i}'

        partsum += int(numstring)
    print(f"sum of all results is: {partsum}")


part1()
part2()
