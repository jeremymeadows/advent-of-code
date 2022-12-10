from puzzles.utils import *


def part1(strings):
    original = sum([len(s) for s in strings])
    decoded = sum([len(eval(s)) for s in strings])
    return original - decoded


def part2(strings):
    original = sum([len(s) for s in strings])
    encoded = sum(
        [len(s.replace("\\", "\\\\").replace('"', '\\"')) + 2 for s in strings]
    )
    return encoded - original


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
        self.assertEqual(
            part1(
                [
                    R'""',
                    R'"abc"',
                    R'"aaa\"aaa"',
                    R'"\x27"',
                ]
            ),
            12,
        )
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(
            part2(
                [
                    R'""',
                    R'"abc"',
                    R'"aaa\"aaa"',
                    R'"\x27"',
                ]
            ),
            19,
        )
        print("part 2 passed")
