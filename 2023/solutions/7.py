with open("../inputs/7") as raw:
    input_list = [[line.split(" ")[0], int(line.split(" ")[1])] for line in raw.read().splitlines()]


print(input_list)
