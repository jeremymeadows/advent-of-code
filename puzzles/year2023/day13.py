from puzzles.utils import *


def part1(inpt):
    summary = 0
    for pattern in split(inpt, ''):
        for i in range(1, len(pattern)):
            a, b = partition(pattern, i)
            size = min(len(a), len(b))
            a, b = a[-size:], (b[:size])[::-1]

            if a == b:
                summary += i * 100
                break
        else:
            pattern = rotate_matrix(pattern)
            for i in range(1, len(pattern)):
                a, b = partition(pattern, i)
                size = min(len(a), len(b))
                a, b = a[-size:], b[:size]

                if a == b[::-1]:
                    summary += i
                    break
    return summary


def part2(inpt):
    summary = 0
    for pattern in split(inpt, ''):
        for i in range(1, len(pattern)):
            a, b = partition(pattern, i)
            size = min(len(a), len(b))
            a, b = ''.join(a[-size:]), ''.join((b[:size])[::-1])

            if count(True for a, b in zip(a, b) if a != b) == 1:
                summary += i * 100
                break
        else:
            pattern = rotate_matrix(pattern)
            for i in range(1, len(pattern)):
                a, b = partition([''.join(e) for e in pattern], i)
                size = min(len(a), len(b))
                a, b = ''.join(a[-size:]), ''.join((b[:size])[::-1])

                if count(True for a, b in zip(a, b) if a != b) == 1:
                    summary += i
                    break
    return summary


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "#.##..##.",
        "..#.##.#.",
        "##......#",
        "##......#",
        "..#.##.#.",
        "..##..##.",
        "#.#.##.#.",
        "",
        "#...##..#",
        "#....#..#",
        "..##..###",
        "#####.##.",
        "#####.##.",
        "..##..###",
        "#....#..#",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 405)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 400)
        print("part 2 passed")
