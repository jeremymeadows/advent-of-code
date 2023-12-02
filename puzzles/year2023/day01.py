from puzzles.utils import *


def part1(inpt):
    values = [[c for c in line if c.isdigit()] for line in inpt]
    for i, val in enumerate(values):
        values[i] = int(f'{val[0]}{val[-1]}')
    return sum(values)


def part2(inpt):
    numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    for i, line in enumerate(inpt):
        while not line[0].isdigit():
            for num in numbers:
                if line.startswith(num):
                    line = line.replace(num, numbers[num], 1)
                    break
            else:
                line = line[1:]

        while not line[-1].isdigit():
            for num in numbers:
                if line.endswith(num):
                    line = rreplace(line, num, numbers[num], 1)
                    break
            else:
                line = line[:-1]

        inpt[i] = line

    values = [[c for c in line if c.isdigit()] for line in inpt]
    for i, val in enumerate(values):
        values[i] = int(f'{val[0]}{val[-1]}')
    return sum(values)


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]

    inpt2 = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 142)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt2), 281)
        print("part 2 passed")
