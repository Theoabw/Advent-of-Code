with open("../inputs/4") as raw:
    # 1 is there for part 2
    cards = [[1, tuple(
        [tuple([int(num) for num in row.strip().split(" ") if num]) for row in card.split(":")[1].split("|")])]
             for card in raw.read().splitlines()]


def part1():
    wtracker = []
    for card in cards:
        card = card[1]
        wcount = 0
        for wnum in card[0]:
            if wnum in card[1]:
                wcount += 1
        if wcount > 0:
            wtracker.append(2 ** (wcount - 1))
        else:
            wtracker.append(0)

    return sum(wtracker)


def part2():
    for curr_id, card in enumerate(cards, 1):
        card = card[1]
        win_count = 0
        for win_num in card[0]:
            if win_num in card[1]:
                win_count += 1
        if win_count > 0:
            for card_id in range(curr_id, curr_id + win_count):
                cards[card_id][0] += cards[curr_id - 1][0]

    return sum([amount[0] for amount in cards])


print(f"part 1: {part1()}")
print(f"part 2: {part2()}")
