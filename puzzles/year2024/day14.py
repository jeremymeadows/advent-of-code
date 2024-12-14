from puzzles.utils import *


def part1(inpt, w = 101, h = 103):
    robots = []
    for line in inpt:
        x, y, vx, vy = map(int, re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)[0])
        robots += [((x, y), (vx, vy))]

    for _ in range(100):
        for i in range(len(robots)):
            (x, y), (vx, vy) = robots[i]
            robots[i] = ((x + vx) % w, (y + vy) % h), (vx, vy)

    q = [
        count(True for (x, y), _ in robots if 0 <= x < w // 2 and 0 <= y < h // 2),
        count(True for (x, y), _ in robots if x > w // 2 and 0 <= y < h // 2),
        count(True for (x, y), _ in robots if 0 <= x < w // 2 and y > h // 2),
        count(True for (x, y), _ in robots if x > w // 2 and y > h // 2),
    ]
    return product(q)


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
        "p=0,4 v=3,-3",
        "p=6,3 v=-1,-3",
        "p=10,3 v=-1,2",
        "p=2,0 v=2,-1",
        "p=0,0 v=1,3",
        "p=3,0 v=-2,-2",
        "p=7,6 v=-1,-3",
        "p=3,0 v=-1,-2",
        "p=9,3 v=2,3",
        "p=7,3 v=-1,2",
        "p=2,4 v=2,-3",
        "p=9,5 v=-3,-3",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt, 11, 7), 12)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), None)
        print("part 2 passed")
