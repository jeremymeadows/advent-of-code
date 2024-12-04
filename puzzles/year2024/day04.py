from puzzles.utils import *


def part1(inpt):
    count = 0
    for y, line in enumerate(inpt):
        for x, c in enumerate(line):
            if c == "X":
                surrounding_coords = [
                    [(y, x + 1), (y, x + 2), (y, x + 3)],
                    [(y, x - 1), (y, x - 2), (y, x - 3)],
                    [(y + 1, x), (y + 2, x), (y + 3, x)],
                    [(y - 1, x), (y - 2, x), (y - 3, x)],
                    [(y + 1, x + 1), (y + 2, x + 2), (y + 3, x + 3)],
                    [(y - 1, x - 1), (y - 2, x - 2), (y - 3, x - 3)],
                    [(y + 1, x - 1), (y + 2, x - 2), (y + 3, x - 3)],
                    [(y - 1, x + 1), (y - 2, x + 2), (y - 3, x + 3)],
                ]
                for coord in surrounding_coords:
                    if any(x < 0 or y < 0 or x >= len(line) or y >= len(inpt) for x, y in coord):
                        continue
                    if (
                        inpt[coord[0][0]][coord[0][1]] +
                        inpt[coord[1][0]][coord[1][1]] +
                        inpt[coord[2][0]][coord[2][1]] == "MAS"
                    ):
                        count += 1
    return count


def part2(inpt):
    count = 0
    for y, line in enumerate(inpt):
        for x, c in enumerate(line):
            if c == "A":
                if x < 1 or y < 1 or x >= len(line) - 1 or y >= len(inpt) - 1:
                    continue
                if (
                    inpt[y - 1][x - 1] + inpt[y + 1][x + 1] in ["MS", "SM"] and
                    inpt[y - 1][x + 1] + inpt[y + 1][x - 1] in ["MS", "SM"]
                ):
                    count += 1
    return count


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 18)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 9)
        print("part 2 passed")
