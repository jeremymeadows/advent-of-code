from puzzles.utils import *


def part1(inpt):
    max_len = max(map(len, inpt))
    for i, row in enumerate(inpt):
        inpt[i] = f'{row:.<{max_len}}'

    for y, row in enumerate(inpt):
        for x, char in enumerate(row):
            if not char.isdigit() and char != '.':
                print(char, inpt[y][x])
                if inpt[y][x-1].isdigit():
                    rfind(lambda c: not c.isdigit(), inpt[y][:x])
                # if inpt[y-1][x-1].isdigit():
                #     print(inpt[y-1][x-1])
                # if inpt[y-1][x].isdigit():
                #     print(inpt[y-1][x])
                # if inpt[y-1][x+1].isdigit():
                #     print(inpt[y-1][x+1])

    return


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
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 4361)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), None)
        print("part 2 passed")
