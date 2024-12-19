from puzzles.utils import *


def part1(inpt):
    towels = inpt[0].split(", ")
    patterns = 0
    for pattern in inpt[2:]:
        arrangements = [e for e in towels if pattern.startswith(e)]
        while len(arrangements) > 0:
            a = arrangements.pop(0)
            if pattern == a:
                patterns += 1
                break
            for towel in towels:
                if pattern.startswith(a + towel) and (a + towel) not in arrangements:
                    arrangements += [a + towel]
    return patterns


def part2(inpt):
    towels = inpt[0].split(", ")
    patterns = 0
    for pattern in inpt[2:]:
        arrangements = [[e] for e in towels if pattern.startswith(e)]
        while len(arrangements) > 0:
            a = arrangements.pop(0)
            if pattern == ''.join(a):
                patterns += 1
                continue
            for towel in towels:
                if pattern.startswith(''.join(a) + towel) and (a + [towel]) not in arrangements:
                    arrangements += [a + [towel]]
    return patterns


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "r, wr, b, g, bwu, rb, gb, br",
        "",
        "brwrr",
        "bggr",
        "gbbr",
        "rrbgbr",
        "ubwu",
        "bwurrg",
        "brgr",
        "bbrgwb",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 6)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 16)
        print("part 2 passed")
