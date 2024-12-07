from puzzles.utils import *


def part1(inpt):
    total = 0
    for line in inpt:
        result, values = line.split(": ")
        result = int(result)
        values = list(map(int, values.split()))
        evals = []
        
        for i in range(2 ** (len(values) - 1)):
            evals += [values[0]]
            for v in values[1:]:
                if i & 1:
                    evals[-1] += v
                else:
                    evals[-1] *= v
                i >>= 1
        if any(e == result for e in evals):
            total += result
    return total


def part2(inpt):
    total = 0
    for line in inpt:
        result, values = line.split(": ")
        result = int(result)
        values = list(map(int, values.split()))
        evals = []
        
        for i in range(3 ** (len(values) - 1)):
            evals += [values[0]]
            for v in values[1:]:
                if i % 3 == 0:
                    evals[-1] += v
                elif i % 3 == 1:
                    evals[-1] *= v
                else:
                    evals[-1] = int(str(evals[-1]) + str(v))
                i //= 3
        if any(e == result for e in evals):
            total += result
    return total


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "190: 10 19",
        "3267: 81 40 27",
        "83: 17 5",
        "156: 15 6",
        "7290: 6 8 6 15",
        "161011: 16 10 13",
        "192: 17 8 14",
        "21037: 9 7 18 13",
        "292: 11 6 16 20",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 3749)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 11387)
        print("part 2 passed")
