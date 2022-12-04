#!/usr/bin/env python3

from utils import *

inpt = get_input()

full_duplicates = 0
part_duplicates = 0
for assignment in inpt:
    a, b = assignment.split(",")
    a_start, a_end = map(lambda e: int(e), a.split("-"))
    b_start, b_end = map(lambda e: int(e), b.split("-"))

    if a_start >= b_start and a_end <= b_end or b_start >= a_start and b_end <= a_end:
        full_duplicates += 1
    if a_start >= b_start and a_start <= b_end or b_start >= a_start and b_start <= a_end:
        part_duplicates += 1

print(f"part 1: {full_duplicates}")
print(f"part 2: {part_duplicates}")

if "test" in sys.argv:
    assert full_duplicates == 2
    assert part_duplicates == 4
