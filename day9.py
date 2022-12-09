#!/usr/bin/env python3

from utils import *

inpt = [e.split() for e in get_input()]

@dataclass(repr=True, eq=True)
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other) -> float:
        return sqrt(pow(abs(self.x - other.x), 2) + pow(abs(self.y - other.y), 2))

    def __iter__(self):
        yield self.x
        yield self.y

    def __sub__(self, other) -> int:
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

def get_tail_positions(n) -> set[tuple[int, int]]:
    knots = [Point() for _ in range(n)]
    tail_positions = set()

    for direction, distance in inpt:
        for _ in range(int(distance)):
            match direction:
                case "U":
                    knots[0].y += 1
                case "D":
                    knots[0].y -= 1
                case "L":
                    knots[0].x -= 1
                case "R":
                    knots[0].x += 1

            for i in range(1, len(knots)):
                head = knots[i - 1]
                tail = knots[i]

                x, y = head - tail
                if (d := head.distance(tail)) == 2:
                    tail.x += x // 2
                    tail.y += y // 2
                elif d > 2:
                    tail.x += copysign(1, x)
                    tail.y += copysign(1, y)
            tail_positions.add((knots[-1].x, knots[-1].y))
    return tail_positions

num_positions = len(get_tail_positions(2))
print(f"part 1: {num_positions}")
if "test" in sys.argv:
    assert len(num_positions) == 13

num_positions = len(get_tail_positions(10))
print(f"part 2: {num_positions}")
if "test" in sys.argv:
    assert len(num_positions) == 1
