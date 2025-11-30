from puzzles.utils import *


def part1(inpt):
    possible = 0
    for line in inpt:
        for a, b, c in [map(int, line.split())]:
            if a + b > c and a + c > b and b + c > a:
                possible += 1
    return possible


def part2(inpt):
    possible = 0
    for a, b, c in chunks(list(chain(*reverse_matrix([[int(i) for i in line.split()] for line in inpt]))), 3):
        if a + b > c and a + c > b and b + c > a:
            possible += 1
    return possible


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "5 10 25",
        "3 4 5",
        "6 8 10",
    ]

    inpt2 = [
        "101 301 501",
        "102 302 502",
        "103 303 503",
        "201 401 601",
        "202 402 602",
        "203 403 603",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 2)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt2), 6)
        print("part 2 passed")
