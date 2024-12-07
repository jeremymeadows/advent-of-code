from puzzles.utils import *


def part1(inpt):
    x, y = 0, 0
    d = "up"
    p = set()

    for i in range(len(inpt)):
        if "^" in inpt[i]:
            x, y = inpt[i].index("^"), i
            p.add((x, y))
            break

    while True:
        if d == "up":
            if y == 0:
                break
            if inpt[y-1][x] == "#":
                d = "right"
                x += 1
            else:
                y -= 1
        elif d == "right":
            if x == len(inpt[0])-1:
                break
            if inpt[y][x+1] == "#":
                d = "down"
                y += 1
            else:
                x += 1
        elif d == "down":
            if y == len(inpt)-1:
                break
            if inpt[y+1][x] == "#":
                d = "left"
                x -= 1
            else:
                y += 1
        elif d == "left":
            if x == 0:
                break
            if inpt[y][x-1] == "#":
                d = "up"
                y -= 1
            else:
                x -= 1

        p.add((x, y))
    return len(p)


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
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#...",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 41)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 6)
        print("part 2 passed")
