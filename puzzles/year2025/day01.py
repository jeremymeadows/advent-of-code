from puzzles.utils import *


def part1(inpt):
    count = 0
    location = 50

    for line in inpt:
        direction = line[0]
        number = int(line[1:])

        if direction == "L":
            location -= number
        elif direction == "R":
            location += number
        location %= 100

        if location == 0:
            count += 1
    return count


def part2(inpt):
    count = 0
    location = 50

    for line in inpt:
        direction = line[0]
        number = int(line[1:])
        prev = location

        if direction == "L":
            location -= number
        elif direction == "R":
            location += number

        count += abs(location // 100)
        location %= 100

        if prev == 0 and direction == "L":
            count -= 1
        if location == 0 and direction == "L":
            count += 1

    return count


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 3)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 6)
        print("part 2 passed")
