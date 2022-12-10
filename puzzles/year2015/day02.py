from puzzles.utils import *


def part1(dimensions):
    paper = 0
    for x, y, z in dimensions:
        a, b, c = x * y, x * z, y * z
        paper += 2 * (a + b + c) + a
    return paper


def part2(dimensions):
    ribbon = 0
    for x, y, z in dimensions:
        ribbon += 2 * (x + y) + x * y * z
    return ribbon


def main():
    inpt = [[int(x) for x in line.split("x")] for line in get_input(__file__)]
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1([[2, 3, 4]]), 58)
        self.assertEqual(part1([[1, 1, 10]]), 43)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2([[2, 3, 4]]), 34)
        self.assertEqual(part2([[1, 1, 10]]), 14)
        print("part 2 passed")
