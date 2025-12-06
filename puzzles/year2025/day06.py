from puzzles.utils import *


def part1(inpt):
    grid = rotate_matrix([list(map(int, line.split())) for line in inpt[:-1]] + [inpt[-1].split()])
    total = 0

    for line in grid:
        total += product(line[:-1]) if line[-1] == "*" else sum(line[:-1])
    return total

def part2(inpt):
    inpt[-1] += " "
    grid = [[] for _ in range(len(inpt) - 1)]

    ndx = 0
    while ndx < len(inpt[-1]):
        width = 0
        ndx += 1
        while ndx < len(inpt[-1]) and inpt[-1][ndx] == " ":
            width += 1
            ndx += 1
        for i, line in enumerate(inpt[:-1]):
            grid[i] += [line[ndx - width - 1: ndx - 1]]

    grid = rotate_matrix(grid)
    total = 0

    ops = [product if c == "*" else sum for c in inpt[-1].split()]
    for i, line in enumerate(grid):
        values = [int("".join(v)) for v in reversed(rotate_matrix(line))]
        total += ops[i](values)
    return total


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   +  ",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 4277556)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 3263827)
        print("part 2 passed")
