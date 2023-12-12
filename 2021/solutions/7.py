with open('../inputs/7', 'r') as raw:
    positions = [int(pos) for pos in raw.read().split(',')]  # list comp to read input

#TODO: look at this

def part1():
    sumlist = []
    for pos in range(min(positions), max(positions)):  # check every number between the lowest and highest num
        fuelcost = 0  # var to keep track of fuelcost
        for crab in positions:  # check fuelcost
            fuelcost += abs(crab - pos)
        sumlist.append(fuelcost)  # append to list to keep track

    print(f"\nPart 1\n"
          f"minimum fuel required: {min(sumlist)}\n"
          f"the position is: {sumlist.index(min(sumlist))}")


def part2():
    # I implemented a progress updater because this function is a bit slower

    sumlist = []
    numrange = enumerate(list(range(min(positions), max(positions))))
    listrange = list(range(min(positions), max(positions)))  # listrange and numrange are only there for the progress
    for i, pos in numrange:
        if int((listrange[i - 1] / max(positions)) * 100) != int((listrange[i] / max(positions)) * 100):
            print(f"{int((pos / max(positions)) * 100)}% done")
        fuelcost = 0
        for crab in positions:
            fuelcost += sum(list(range(abs(crab - pos) + 1)))  # summing the list of the range to get the answer
        sumlist.append(fuelcost)

    print(f"\nPart 2\n"
          f"minimum fuel required: {min(sumlist)}\n"
          f"the position is: {sumlist.index(min(sumlist))}")


if __name__ == '__main__':
    ON = True

    while ON:  # I just did this because I was bored
        answer = input("\nwhich part would you like to run?\n"
                       "'1' for part 1 and '2' for part 2 '3' to exit\n"
                       "Answer: ")
        try:
            if int(answer.strip("'")) == 1:
                part1()

            elif int(answer.strip("'")) == 2:
                part2()

            elif int(answer.strip("'")) == 3:
                break

            else:
                print("Invalid input!")
        except ValueError:
            print("Invalid input!")
