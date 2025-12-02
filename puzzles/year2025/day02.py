from puzzles.utils import *


def part1(inpt):
    ranges = [[i for i in map(int, r.split("-"))] for r in inpt.split(",")]
    s = 0

    for r in ranges:
        for n in range(r[0], r[1] + 1):
            if re.match(r"^(\d+)(\1)$", str(n)):
                s += n
    return s


def part2(inpt):
    ranges = [[i for i in map(int, r.split("-"))] for r in inpt.split(",")]
    s = 0

    for r in ranges:
        for n in range(r[0], r[1] + 1):
            if re.match(r"^(\d+)(\1+)$", str(n)):
                s += n
    return s


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 1227775554)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 4174379265)
        print("part 2 passed")
