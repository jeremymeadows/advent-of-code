from puzzles.utils import *


def find_peaks(x, y, inpt):
    t = inpt[y][x]
    if t == 9:
        return {(x, y)}

    peaks = set()
    if x > 0 and inpt[y][x - 1] == t + 1:
        peaks = peaks.union(find_peaks(x - 1, y, inpt))
    if x < len(inpt[y]) - 1 and inpt[y][x + 1] == t + 1:
        peaks = peaks.union(find_peaks(x + 1, y, inpt))
    if y < len(inpt) - 1 and inpt[y + 1][x] == t + 1:
        peaks = peaks.union(find_peaks(x, y + 1, inpt))
    if y > 0 and inpt[y - 1][x] == t + 1:
        peaks = peaks.union(find_peaks(x, y - 1, inpt))
    return peaks


def find_paths(x, y, inpt):
    paths = 0
    t = inpt[y][x]
    if t == 9:
        return 1

    if x > 0 and inpt[y][x - 1] == t + 1:
        paths += find_paths(x - 1, y, inpt)
    if x < len(inpt[y]) - 1 and inpt[y][x + 1] == t + 1:
        paths += find_paths(x + 1, y, inpt)
    if y < len(inpt) - 1 and inpt[y + 1][x] == t + 1:
        paths += find_paths(x, y + 1, inpt)
    if y > 0 and inpt[y - 1][x] == t + 1:
        paths += find_paths(x, y - 1, inpt)
    return paths


def part1(inpt):
    inpt = [[int(i) for i in line] for line in inpt]
    scores = 0
    for y in range(len(inpt)):
        for x in range(len(inpt[0])):
            if inpt[y][x] == 0:
                scores += len(find_peaks(x, y, inpt))
    return scores


def part2(inpt):
    inpt = [[int(i) for i in line] for line in inpt]
    ratings = 0
    for y in range(len(inpt)):
        for x in range(len(inpt[0])):
            if inpt[y][x] == 0:
                ratings += find_paths(x, y, inpt)
    return ratings


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "0123",
        "1234",
        "8765",
        "9876",
    ]

    inpt2 = [
        "89010123",
        "78121874",
        "87430965",
        "96549874",
        "45678903",
        "32019012",
        "01329801",
        "10456732",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 1)
        self.assertEqual(part1(Test.inpt2), 36)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt2), 81)
        print("part 2 passed")
