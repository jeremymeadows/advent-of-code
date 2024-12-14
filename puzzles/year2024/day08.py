from math import dist
from puzzles.utils import *


def part1(inpt):
    h, w = len(inpt), len(inpt[0])
    antennas = dict()
    for i, e in enumerate(''.join(inpt)):
        if e != '.':
            antennas[e] = antennas.get(e, []) + [(i % w, i // h)]

    antinodes = set()
    for antenna in antennas:
        for a, b in combinations(antennas[antenna], 2):
            a = Point(*a)
            b = Point(*b)
            dx, dy = abs(a.x - b.x), abs(a.y - b.y)
            nodes = []
            if a.x < b.x:
                if a.y < b.y:
                    nodes += [(a.x - dx, a.y - dy)]
                    nodes += [(b.x + dx, b.y + dy)]
                else:
                    nodes += [(a.x - dx, a.y + dy)]
                    nodes += [(b.x + dx, a.y - dy)]
            else:
                if a.y < b.y:
                    nodes += [(a.x + dx, a.y - dy)]
                    nodes += [(b.x - dx, b.y + dy)]
                else:
                    nodes += [(a.x + dx, a.y + dy)]
                    nodes += [(b.x - dx, b.y - dy)]
            for node in nodes:
                antinodes.add(node)
    antinodes = { p for p in antinodes if 0 <= p[0] < w and 0 <= p[1] < h }
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

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 14)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), None)
        print("part 2 passed")
