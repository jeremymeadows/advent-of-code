from puzzles.utils import *


def part1(min_presents):
    first_house = 1
    while sum([e * 10 for e in factors(first_house)]) < min_presents:
        first_house += 1
    return first_house


def part2(min_presents):
    first_house = 1
    while (
        sum(
            [
                e * 11
                for e in filter(lambda e: first_house / e < 50, factors(first_house))
            ]
        )
        < min_presents
    ):
        first_house += 1
    return first_house


@cache
def factors(x):
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            yield i
            yield x // i


def main():
    inpt = int(get_input(__file__))
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(10), 1)
        self.assertEqual(part1(30), 2)
        self.assertEqual(part1(40), 3)
        self.assertEqual(part1(70), 4)
        self.assertEqual(part1(60), 5)
        self.assertEqual(part1(120), 6)
        self.assertEqual(part1(80), 7)
        self.assertEqual(part1(150), 8)
        self.assertEqual(part1(130), 9)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(100), 10)
        self.assertEqual(part2(1000), 36)
        self.assertEqual(part2(10000), 336)
        print("part 2 passed")
