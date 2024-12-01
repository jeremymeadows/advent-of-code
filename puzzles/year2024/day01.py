from puzzles.utils import *


def part1(inpt):
    inpt = [list(map(int, x.split())) for x in inpt]
    col1, col2 = [sorted(col) for col in zip(*inpt)]
    return sum([abs(a - b) for a, b in zip(col1, col2)])


def part2(inpt):
    inpt = [list(map(int, x.split())) for x in inpt]
    col1, col2 = zip(*inpt)
    counts = Counter(col2)
    return sum([x * counts[x] for x in col1])


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 11)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 31)
        print("part 2 passed")
