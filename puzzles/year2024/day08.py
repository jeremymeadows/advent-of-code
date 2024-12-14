from math import dist
from puzzles.utils import *


def part1(inpt):
    h, w = len(inpt), len(inpt[0])
    antennas = dict()
    for i, e in enumerate(''.join(inpt)):
        if e != '.':
            antennas[e] = antennas.get(e, []) + [(i % w, i // h)]

    print(antennas)
    antinodes = set()
    for antenna in antennas:
        print(antenna)
        for a, b in combinations(antennas[antenna], 2):
            a = Point(*a)
            b = Point(*b)
            print(a, b)
            node = Point(0, 0)
            minx, maxx = sorted([a.x, b.x])
            miny, maxy = sorted([a.y, b.y])
            dx, dy = maxx - minx, maxy - miny
            if (x := minx - dx) >= 0 and x < w and (y := miny - dy) >= 0 and y < h:
                antinodes.add((minx - dx, miny - dy))
            if (x := maxx + dx) >= 0 and x < w and (y := maxy + dy) >= 0 and y < h:
                antinodes.add((maxx + dx, maxy + dy))
            print((minx - dx, miny - dy))
            print((maxx + dx, maxy + dy))

    print(antinodes)
    return len(antinodes)


def part2(inpt):
    return


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "............",
        "........0...",
        ".....0......",
        ".......0....",
        "....0.......",
        "......A.....",
        "............",
        "............",
        "........A...",
        ".........A..",
        "............",
        "............",
    ]
    inpt2 = [
"..........",
"..........",
"..........",
"....a.....",
"..........",
".....a....",
"..........",
"..........",
"..........",
"..........",
            ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt2), 2)
        self.assertEqual(part1(Test.inpt), 14)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), None)
        print("part 2 passed")
