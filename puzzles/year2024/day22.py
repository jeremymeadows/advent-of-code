from puzzles.utils import *


def part1(inpt):
    total = 0
    calc = lambda secret, num: (secret ^ num) % 16777216
    for secret in map(int, inpt):
        for _ in range(2000):
            secret = calc(secret, secret * 64)
            secret = calc(secret, secret // 32)
            secret = calc(secret, secret * 2048)
        total += secret
    return total


def part2(inpt):
    total = 0
    calc = lambda secret, num: (secret ^ num) % 16777216
    for secret in map(int, inpt):
        for _ in range(2000):
            secret = calc(secret, secret * 64)
            secret = calc(secret, secret // 32)
            secret = calc(secret, secret * 2048)
        total += secret
    return total


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "1",
        "10",
        "100",
        "2024",
    ]

    inpt2 = [
        "1",
        "2",
        "3",
        "2024",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 37327623)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt2), 23)
        print("part 2 passed")
