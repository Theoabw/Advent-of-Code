# with open('Example ../inputs/Input 6.txt', 'r') as raw:
#     timerlist = [int(age) for age in raw.read().split(',')]
#
# def fish_simulation():
#     tlist = timerlist.copy()
#     for x in range(80):
#         for index, time in enumerate(tlist):
#             if not time:
#                 tlist.append(9)
#                 tlist[index] = 6
#             if time:
#                 tlist[index] -= 1
#
#     print(len(tlist))
#
# fish_simulation()


from time import perf_counter

start_time = perf_counter()
starting_fish = [int(i) for i in
                 open("../inputs/6").read().split(',')]
total = 0

current_states = {
    0: starting_fish.count(0),
    1: starting_fish.count(1),
    2: starting_fish.count(2),
    3: starting_fish.count(3),
    4: starting_fish.count(4),
    5: starting_fish.count(5),
    6: starting_fish.count(6),
    7: starting_fish.count(7),
    8: starting_fish.count(8)
}
next_states = {}

for i in range(256):

    next_states = {
        0: current_states[1],
        1: current_states[2],
        2: current_states[3],
        3: current_states[4],
        4: current_states[5],
        5: current_states[6],
        6: current_states[7],
        7: current_states[8],
        8: current_states[0]
    }

    if current_states[0] > 0:
        next_states[6] += current_states[0]

    current_states = next_states
    next_states = {}

for fish in current_states:
    total += current_states[fish]

print(f"length is {total}")
print(f"took {perf_counter() - start_time} seconds")
