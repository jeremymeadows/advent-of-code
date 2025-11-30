from puzzles.utils import *


def part1(inpt):
    return ''.join([Counter(col).most_common()[0][0] for col in reverse_matrix(inpt)])


def part2(inpt):
    return ''.join([Counter(col).most_common()[-1][0] for col in reverse_matrix(inpt)])


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "eedadn",
        "drvtee",
        "eandsr",
        "raavrd",
        "atevrs",
        "tsrnev",
        "sdttsa",
        "rasrtv",
        "nssdts",
        "ntnada",
        "svetve",
        "tesnvt",
        "vntsnd",
        "vrdear",
        "dvrsen",
        "enarar",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 'easter')
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 'advent')
        print("part 2 passed")
