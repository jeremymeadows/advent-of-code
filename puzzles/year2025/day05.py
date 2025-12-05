from puzzles.utils import *


def part1(inpt):
    fresh, ingredients = split(inpt, "")
    fresh = IntervalSet([tuple(map(int, r.split("-"))) for r in fresh])
    ingredients = set(map(int, ingredients))
    return len([i for i in ingredients if i in fresh])


def part2(inpt):
    fresh, _ = split(inpt, "")
    fresh = IntervalSet([tuple(map(int, r.split("-"))) for r in fresh])
    return len(fresh)


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 3)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 14)
        print("part 2 passed")
