from puzzles.utils import *


def get_path(x, y, d, m):
    path = { (x, y, d) }

    while True:
        if d == "up":
            if y == 0:
                break
            if m[y-1][x] == "#":
                d = "right"
            else:
                y -= 1
        elif d == "right":
            if x == len(m[0])-1:
                break
            if m[y][x+1] == "#":
                d = "down"
            else:
                x += 1
        elif d == "down":
            if y == len(m)-1:
                break
            if m[y+1][x] == "#":
                d = "left"
            else:
                y += 1
        elif d == "left":
            if x == 0:
                break
            if m[y][x-1] == "#":
                d = "up"
            else:
                x -= 1

        if (x, y, d) in path:
            raise ValueError("Loop detected")
        path.add((x, y, d))
    return { (x, y) for x, y, _ in path }


def part1(inpt):
    x, y = 0, 0

    for i in range(len(inpt)):
        if "^" in inpt[i]:
            x, y = inpt[i].index("^"), i
            break

    path = get_path(x, y, "up", inpt)
    return len(path)


def part2(inpt):
    start = (0, 0)
    count = 0

    for i in range(len(inpt)):
        if "^" in inpt[i]:
            start = (inpt[i].index("^"), i)
            break

    orig_path = get_path(*start, "up", inpt)

    for x, y in orig_path:
        if start == (x, y):
            continue

        inpt[y] = inpt[y][:x] + "#" + inpt[y][x+1:]
        try:
            get_path(*start, "up", inpt)
        except ValueError:
            count += 1
        inpt[y] = inpt[y][:x] + "." + inpt[y][x+1:]

    return count


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
    
    edge = [ ".#..", "..#.", ".^.." ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 41)
        self.assertEqual(part1(Test.edge), 2)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 6)
        print("part 2 passed")
