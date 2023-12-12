with open("../inputs/5") as inp:
    raw_matrix, instr = inp.read().split('\n\n')
    instr = [[int(baz) for baz in bar[1::2]] for bar in
             [foo.split(' ') for foo in instr.split('\n') if foo]]


def parsed_data(matrix):
    size = max([int(foo) for foo in matrix.split('\n')[-1:][0].strip().split('   ')])
    matrix = [[bar for bar in foo[1::4]] for foo in matrix.split('\n')[:-1]]
    # add the missing blanks so that the matrix is easier to rotate
    for index, row in enumerate(matrix):
        if len(row) < size:
            for missing in range(size - len(row)):
                matrix[index].append(' ')

    # rotate the list so that it's easier to work with it
    rlist = []

    for column in range(len(matrix[0])):
        rlist.append([])
        for i, x in enumerate(matrix):
            rlist[column].append(matrix[i][column])

    return [[y for y in x if y != ' '] for x in rlist]


def part1(data, instruction_list):
    for row in instruction_list:
        amount = row[0]
        from_col = row[1] - 1
        to_col = row[2] - 1
        for elem in range(amount):
            data[to_col].insert(0, data[from_col][0])
            data[from_col].pop(0)

    return ''.join([str(col[0]) for col in data])


def part2(data, instruction_list):
    for row in instruction_list:
        amount = row[0]
        from_col = row[1] - 1
        to_col = row[2] - 1
        data[to_col] = data[from_col][:amount] + data[to_col]
        for elem in range(amount):
            data[from_col].pop(0)

    return ''.join([str(col[0]) for col in data])


indata = parsed_data(raw_matrix)
cindata = parsed_data(raw_matrix)

print(part1(indata, instr))
print(part2(cindata, instr))
