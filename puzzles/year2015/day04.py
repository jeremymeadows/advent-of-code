from puzzles.utils import *


def part1(key):
    n = 0
    while True:
        if md5(f"{key}{n}".encode("utf-8")).hexdigest()[:5] == "00000":
            return n
        n += 1


def part2(key):
    n = 0
    while True:
        if md5(f"{key}{n}".encode("utf-8")).hexdigest()[:6] == "000000":
            return n
        n += 1


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
        self.assertEqual(part1("abcdef"), 609043)
        self.assertEqual(part1("pqrstuv"), 1048970)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2("abcdef"), 6742839)
        self.assertEqual(part2("pqrstuv"), 5714438)
        print("part 2 passed")
