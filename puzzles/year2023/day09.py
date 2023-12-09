from puzzles.utils import *


def part1(inpt):
    predictions = []
    for line in inpt:
        iters = [[int(i) for i in line.split()]]
        while not all(i == 0 for i in iters[-1]):
            iters += [[iters[-1][i] - iters[-1][i - 1] for i in range(1, len(iters[-1]))]]

        for i in range(len(iters) - 2, -1, -1):
            iters[i] += [iters[i][-1] + iters[i + 1][-1]]
            
        predictions += [iters[0][-1]]
    return sum(predictions)


def part2(inpt):
    predictions = []
    for line in inpt:
        iters = [[int(i) for i in line.split()]]
        while not all(i == 0 for i in iters[-1]):
            iters += [[iters[-1][i] - iters[-1][i - 1] for i in range(1, len(iters[-1]))]]

        for i in range(len(iters) - 2, -1, -1):
            iters[i] += [iters[i][0] - iters[i + 1][-1]]
            
        predictions += [iters[0][-1]]
    return sum(predictions)


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "0 3 6 9 12 15",
        "1 3 6 10 15 21",
        "10 13 16 21 30 45",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 114)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 2)
        print("part 2 passed")
