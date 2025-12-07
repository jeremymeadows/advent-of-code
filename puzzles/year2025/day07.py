from puzzles.utils import *


def part1(inpt):
    manifold = [list(line) for line in inpt]
    manifold[1][manifold[0].index("S")] = "|"
    splits = 0

    for i, line in enumerate(manifold[2::2]):
        i = i * 2 + 2
        for j, c in enumerate(manifold[i - 1]):
            if c == "|":
                if line[j] == ".":
                    manifold[i + 1][j] = "|"
                elif line[j] == "^":
                    manifold[i + 1][j - 1] = "|"
                    manifold[i + 1][j + 1] = "|"
                    splits += 1
    return splits


def part2(inpt):
    manifold = [list(line) for line in inpt]
    manifold[1][manifold[0].index("S")] = 1

    for i, line in enumerate(manifold[2::2]):
        i = i * 2 + 2
        for j, c in enumerate(manifold[i - 1]):
            if type(c) is int:
                if line[j] == ".":
                    x = manifold[i + 1][j]
                    manifold[i + 1][j] = c if x == "." else c + x
                elif line[j] == "^":
                    a = manifold[i + 1][j - 1]
                    b = manifold[i + 1][j + 1]
                    manifold[i + 1][j - 1] = c if a == "." else c + a
                    manifold[i + 1][j + 1] = c if b == "." else c + b
    return sum(c for c in manifold[-1] if type(c) is int)


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 21)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 40)
        print("part 2 passed")
