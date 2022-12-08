#!/usr/bin/env python3

from utils import *

inpt = get_input()
rows = list(map(lambda e: [int(x) for x in e], inpt))
cols = list(map(lambda e: list(e), zip(*rows)))

size_x = len(cols)
size_y = len(rows)

visible = []
visible.extend(rows[0])
visible.extend(rows[-1])
visible.extend(cols[0][1:-1])
visible.extend(cols[-1][1:-1])

max_visibility_score = 0
for x in range(1, size_x-1):
    for y in range(1, size_y-1):
        vis = False
        score = 1

        for ndx, height in enumerate(reversed(rows[x][:y])):
            if not rows[x][y] > height:
                break
        else:
            vis = True
        score *= ndx + 1

        for ndx, height in enumerate(rows[x][y+1:]):
            if not rows[x][y] > height:
                break
        else:
            vis = True
        score *= ndx + 1

        for ndx, height in enumerate(reversed(cols[y][:x])):
            if not cols[y][x] > height:
                break
        else:
            vis = True
        score *= ndx + 1

        for ndx, height in enumerate(cols[y][x+1:]):
            if not cols[y][x] > height:
                break
        else:
            vis = True
        score *= ndx + 1
            
        if vis:
            visible.append(rows[x][y])
        max_visibility_score = max(max_visibility_score, score)

print(f"part 1: {len(visible)}")
print(f"part 2: {max_visibility_score}")

if "test" in sys.argv:
    assert len(visible) == 21
    assert max_visibility_score == 8
