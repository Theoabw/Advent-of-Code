with open('../inputs/4') as raw:
    read = raw.read().split('\n\n')
    numbers = tuple([int(x) for x in read[0].split(',')])
    boards = [[[int(num) for num in line.split()] for line in board.split('\n')] for board in read[1:]]


def marker(num, board):
    for row in board:
        for rownum in range(len(row)):
            if row[rownum] == num:
                row[rownum] = 'x'


def wincheck(board):
    Win = False

    for row in board:  # row/horizontal check
        if all([(elem == 'x') for elem in row]):
            Win = True

    collist = []
    for icol, col in enumerate(board):  # Vertical check
        for irow, row in enumerate(col):
            collist.append(board[irow][icol])

        if all([(elem == 'x') for elem in collist]):
            Win = True
        else:
            collist.clear()

    return Win


def bsum(board):
    sum = 0
    for row in board:
        for num in row:
            if num != 'x':
                sum += num
    return sum


def part1():
    bcopy = boards
    for num in numbers:
        for board in bcopy:
            marker(num, board)
            if wincheck(board):
                print(f"Part 1\nboard {bcopy.index(board) + 1} wins and the answer is {bsum(board) * num}\n")
                return True


def part2():
    boardscopy = list(enumerate(boards))
    for num in numbers:
        for board in boardscopy.copy():
            marker(num, board[1])
            if wincheck(board[1]):
                if len(boardscopy) < 2:
                    boardsum = bsum(board[1])
                    print(f"Part 2\nboard {board[0] + 1} is the last board to win and the answer is "
                          f"{boardsum * num} where {boardsum = } and {num = } ")
                    return True
                else:
                    boardscopy.remove(board)


if __name__ == '__main__':
    part1()
    part2()
