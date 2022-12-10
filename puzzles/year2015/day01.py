from puzzles.utils import *


def part1(directions):
    return sum({"(": 1, ")": -1}[d] for d in directions)


def part2(directions):
    floor = 0
    for ndx, d in enumerate(directions):
        floor += {"(": 1, ")": -1}[d]

        if floor == -1:
            return ndx + 1
    return None


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1("(())"), 0)
        self.assertEqual(part1("()()"), 0)
        self.assertEqual(part1("((("), 3)
        self.assertEqual(part1("(()(()("), 3)
        self.assertEqual(part1("))((((("), 3)
        self.assertEqual(part1("())"), -1)
        self.assertEqual(part1("))("), -1)
        self.assertEqual(part1(")))"), -3)
        self.assertEqual(part1(")())())"), -3)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(")"), 1)
        self.assertEqual(part2("()())"), 5)
        print("part 2 passed")
