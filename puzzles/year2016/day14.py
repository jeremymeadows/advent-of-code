from puzzles.utils import *


def part1(inpt):
    counter = 0
    print(md5(f'{inpt}{counter}'.encode()).hexdigest())
    return


def part2(inpt):
    return


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = "abc"

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), None)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), None)
        print("part 2 passed")
