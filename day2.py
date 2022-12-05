#!/usr/bin/env python3

from utils import *

inpt = [e.split() for e in get_input()]

CODEBOOK: dict[str, int] = {
    "A": 1, "X": 1,
    "B": 2, "Y": 2,
    "C": 3, "Z": 3,
}

score = 0
for opponent, move in inpt:
    opponent = CODEBOOK[opponent]
    move = CODEBOOK[move]

    score += move
    match (opponent - move) % 3:
        case 0:  # draw
            score += 3
        case 2:  # win
            score += 6

print(f"part 1: {score}")
if "test" in sys.argv:
    assert score == 15

score = 0
for opponent, outcome in inpt:
    opponent = CODEBOOK[opponent]

    match outcome:
        case "X":  # lose
            score += (opponent - 2) % 3 + 1
        case "Y":  # draw
            score += 3 + opponent
        case "Z":  # win
            score += 6 + (opponent) % 3 + 1

print(f"part 2: {score}")
if "test" in sys.argv:
    assert score == 12
