from puzzles.utils import *


def part1(strings):
    return len(
        [
            e
            for e in strings
            if re.match(r"(.*[aeiou].*){3}", e)
            and re.match(r".*(.)\1", e)
            and not re.match(r".*(ab|cd|pq|xy)", e)
        ]
    )


def part2(strings):
    return len(
        [e for e in strings if re.match(r".*(..).*\1", e) and re.match(r".*(.).\1", e)]
    )


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
        self.assertEqual(part1(["ugknbfddgicrmopn"]), 1)
        self.assertEqual(part1(["aaa"]), 1)
        self.assertEqual(part1(["jchzalrnumimnmhp"]), 0)
        self.assertEqual(part1(["haegwjzuvuyypxyu"]), 0)
        self.assertEqual(part1(["dvszwmarrgswjxmb"]), 0)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(["qjhvhtzxzqqjkmpb"]), 1)
        self.assertEqual(part2(["xxyxx"]), 1)
        self.assertEqual(part2(["uurcxstgmygtbstg"]), 0)
        self.assertEqual(part2(["ieodomkazucvgmuy"]), 0)
        print("part 2 passed")
