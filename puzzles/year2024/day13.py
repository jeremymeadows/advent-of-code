from puzzles.utils import *


def part1(inpt):
    total = 0
    for a, b, prize, _ in chunks(inpt + [""], 4):
        ax, ay = map(int, re.findall(r"X.(\d+), Y.(\d+)", a)[0])
        bx, by = map(int, re.findall(r"X.(\d+), Y.(\d+)", b)[0])
        px, py = map(int, re.findall(r"X=(\d+), Y=(\d+)", prize)[0])
        cost = float('inf')

        for cb in range(1, 100):
            for ca in range(1, 100):
                if ca * ax + cb * bx == px and ca * ay + cb * by == py:
                    cost = min(cost, ca * 3 + cb)
        total += 0 if cost == float('inf') else cost
    return total


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
        "Button A: X+94, Y+34",
        "Button B: X+22, Y+67",
        "Prize: X=8400, Y=5400",
        "",
        "Button A: X+26, Y+66",
        "Button B: X+67, Y+21",
        "Prize: X=12748, Y=12176",
        "",
        "Button A: X+17, Y+86",
        "Button B: X+84, Y+37",
        "Prize: X=7870, Y=6450",
        "",
        "Button A: X+69, Y+23",
        "Button B: X+27, Y+71",
        "Prize: X=18641, Y=10279",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 480)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), None)
        print("part 2 passed")
