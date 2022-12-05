#!/usr/bin/env python3

from utils import *

inpt = get_input()
indx = inpt.index("")

crates: dict[int, list[str]] = {}
for row in inpt[: indx - 1]:
    for ndx, col in enumerate(chunks(row, 4)):
        if col[1] != " ":
            if not crates.get(ndx + 1):
                crates[ndx + 1] = []
            crates[ndx + 1].insert(0, col[1])

moves: list[tuple[int, int, int]] = []
for row in inpt[indx + 1 :]:
    count, src, dest = [int(tok) for col, tok in enumerate(row.split()) if col % 2]
    moves.append((count, src, dest))

version_a = deepcopy(crates)
version_b = deepcopy(crates)
for count, src, dest in moves:
    for i in range(count):
        version_a[dest].append(version_a[src].pop())
        version_b[dest].append(version_b[src].pop(i - count))

top_a = "".join([version_a[key][-1] for key in sorted(version_a.keys())])
top_b = "".join([version_b[key][-1] for key in sorted(version_b.keys())])

print(f"part 1: {top_a}")
print(f"part 2: {top_b}")

if "test" in sys.argv:
    assert top_a == "CMZ"
    assert top_b == "MCD"
