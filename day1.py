#!/usr/bin/env python3

from utils import *

inpt = get_input()

ndx = 0
elves = [0]
for calories in inpt:
    if not calories:
        ndx += 1
        elves += [0]
    else:
        elves[ndx] += int(calories)

most_calories = max(elves)
top_three_calories = sum(sorted(elves)[-1:-4:-1])

print(f"part 1: {most_calories}")
print(f"part 2: {top_three_calories}")

if "test" in sys.argv:
    assert most_calories == 24000
    assert top_three_calories == 45000
