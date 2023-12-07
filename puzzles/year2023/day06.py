from puzzles.utils import *


def part1(inpt):
    races = zip(
        map(int, re.split(r'\s+', inpt[0])[1:]),
        map(int, re.split(r'\s+', inpt[1])[1:])
    )
    score = 1

    for time, dist in races:
        ways_to_win = 0
        for speed in range(1, time):
            if speed * (time - speed) > dist:
                ways_to_win += 1
        score *= ways_to_win
    return score


def part2(inpt):
    time = int(inpt[0].split(': ')[-1].replace(' ', ''))
    dist = int(inpt[1].split(': ')[-1].replace(' ', ''))

    ways_to_win = 0
    for speed in range(1, time):
        if speed * (time - speed) > dist:
            ways_to_win += 1
    return ways_to_win


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "Time:      7  15   30",
        "Distance:  9  40  200",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 288)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 71503)
        print("part 2 passed")
