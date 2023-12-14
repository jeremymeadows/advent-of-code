from puzzles.utils import *


def part1(inpt):
    dish = [[c for c in line] for line in inpt]
    for y in range(1, len(dish)):
        for x in range(len(dish[y])):
            if dish[y][x] == 'O':
                i = 0
                while y - i - 1 >= 0 and dish[y - i - 1][x] == '.':
                    i += 1
                dish[y][x] = '.'
                dish[y - i][x] = 'O'
    return sum(row.count('O') * (len(dish) - i) for i, row in enumerate(dish))


def part2(inpt):
    dish = [[c for c in line] for line in inpt]
    for _ in range(1000):
        for y in range(1, len(dish)):
            for x in range(len(dish[y])):
                if dish[y][x] == 'O':
                    i = 0
                    while y - i - 1 >= 0 and dish[y - i - 1][x] == '.':
                        i += 1
                    dish[y][x] = '.'
                    dish[y - i][x] = 'O'
        for y in range(len(dish)):
            for x in range(1, len(dish[y])):
                if dish[y][x] == 'O':
                    i = 0
                    while x - i - 1 >= 0 and dish[y][x - i - 1] == '.':
                        i += 1
                    dish[y][x] = '.'
                    dish[y][x - i] = 'O'
        for y in reversed(range(len(dish) - 1)):
            for x in range(len(dish[y])):
                if dish[y][x] == 'O':
                    i = 0
                    while y + i + 1 < len(dish) and dish[y + i + 1][x] == '.':
                        i += 1
                    dish[y][x] = '.'
                    dish[y + i][x] = 'O'
        for y in range(len(dish)):
            for x in reversed(range(len(dish[y]) - 1)):
                if dish[y][x] == 'O':
                    i = 0
                    while x + i + 1 < len(dish[y]) and dish[y][x + i + 1] == '.':
                        i += 1
                    dish[y][x] = '.'
                    dish[y][x + i] = 'O'
    return sum(row.count('O') * (len(dish) - i) for i, row in enumerate(dish))


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "O....#....",
        "O.OO#....#",
        ".....##...",
        "OO.#O....O",
        ".O.....O#.",
        "O.#..O.#.#",
        "..O..#O..O",
        ".......O..",
        "#....###..",
        "#OO..#....",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 136)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 64)
        print("part 2 passed")
