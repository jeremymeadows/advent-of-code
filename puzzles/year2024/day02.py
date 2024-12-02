from puzzles.utils import *


def is_safe(data: list[int]):
    if not is_sorted(data) and not is_sorted(data, reverse=True):
        return False
    for pair in windows(data, 2):
        a, b = map(int, pair)
        if abs(a - b) == 0 or abs(a - b) > 3:
            return False
    return True


def part1(inpt):
    safe = 0
    for line in inpt:
        data = list(map(int, line.split()))
        if is_safe(data):
            safe += 1
    return safe


def part2(inpt):
    safe = 0
    for line in inpt:
        data = list(map(int, line.split()))
        if is_safe(data):
            safe += 1
        else:
            for i in range(len(data)):
                if is_safe(data[:i] + data[i+1:]):
                    safe += 1
                    break
    return safe


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 2)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 4)
        print("part 2 passed")
