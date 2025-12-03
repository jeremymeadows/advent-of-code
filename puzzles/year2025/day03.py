from puzzles.utils import *


def part1(inpt):
    batteries = inpt
    joltage = 0

    for bank in batteries:
        a = max(bank[:-1])
        b = max(bank[bank.index(a) + 1:])
        joltage += int(a + b)
    return joltage


def part2(inpt):
    batteries = inpt
    joltage = 0

    for bank in batteries:
        b = []
        n = 0
        for i in reversed(range(12)):
            b += [max(bank[n:(-i or None)])]
            n = bank.index(b[-1], n) + 1
        joltage += int("".join(b))
    return joltage


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 357)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 3121910778619)
        print("part 2 passed")
