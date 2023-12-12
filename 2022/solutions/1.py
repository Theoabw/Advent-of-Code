inp = open('../inputs/1').read()
tot_inv = [sum([int(calorie) for calorie in inv.split('\n') if calorie]) for inv in inp.split('\n\n') if inv]
print(f"P1 Ans:", max(tot_inv))
print(f"P2 Ans:", sum(sorted(tot_inv)[-3:]))
