with open("../inputs/8") as raw:
    parsed_inp = raw.read().split("\n\n")
    instructions = parsed_inp[0]
    instructions = instructions.translate(str.maketrans("LR", "01"))
    nodes = [[line.split(" = ")[0], (line.split(" = ")[1].split(", ")[0][1:], line.split(" = ")[1].split(", ")[1][:-1])]
             for line in parsed_inp[1].splitlines()]
    nodes = dict(nodes)

def part1():

    global instructions
    curval = nodes["AAA"]
    lastkey = "ZZZ"
    count = 0

    while True:
        side = instructions[0]
        curkey = curval[int(side)]
        curval = nodes[curkey]
        count += 1
        if curkey == lastkey:
            return count

        instructions += instructions[0]
        instructions = instructions[1:]

#TODO: fix part2 since it takes forever. Use lcm
#TODO: fix instructions variable so that I can run part 1 and 2

def part2():

    global instructions
    curkey_list = []
    curval_list = []
    count = 0
    for key in nodes.keys():
        if key[-1] == "A":
            curkey_list.append(key)
    for key in curkey_list:
        curval_list.append(nodes[key])


    while True:
        side = instructions[0]
        for i, entry in enumerate(curkey_list):
            # replace the current key in the list with the next one according to side
            curkey_list[i] = curval_list[i][int(side)]
            curval_list[i] = nodes[curkey_list[i]]
        count += 1
        tcount = 0
        for entry in curkey_list:
            if entry[-1] == "Z":
                tcount += 1
        if tcount == len(curkey_list):
            return count

        if not count % 1000000:
            print(count)

        instructions += instructions[0]
        instructions = instructions[1:]


# print(part1())
print(part2())


