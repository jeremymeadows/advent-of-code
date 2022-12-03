#!/usr/bin/env python3

from utils import *

from functools import reduce
from itertools import chain
from math import log2

inpt = get_input()

priority = [
    chr(i) for i in chain(range(ord("a"), ord("z") + 1), range(ord("A"), ord("Z") + 1))
]

misplaced_priority = 0
for bag in inpt:
    contents = BitVec()
    a, b = bag[:len(bag) // 2], bag[len(bag) // 2:]

    for item in a:
        contents[ord(item) - ord("A")] = True

    for item in b:
        if contents[ord(item) - ord("A")]:
            misplaced_priority += priority.index(item) + 1
            break

print(f"part 1: {misplaced_priority}")
if "test" in sys.argv:
    assert misplaced_priority == 157

GROUP_SIZE = 3
badge_priority = 0
for group in chunks(inpt, GROUP_SIZE):
    bags = [0] * GROUP_SIZE

    for elf in range(GROUP_SIZE):
        for ch in group[elf]:
            bags[elf] |= 1 << ord(ch) - ord("A")

    badge = reduce(lambda a, b: a & b, bags)
    badge = chr(int(log2(badge)) + ord("A"))
    badge_priority += priority.index(badge) + 1

print(f"part 2: {badge_priority}")
if "test" in sys.argv:
    assert badge_priority == 70
