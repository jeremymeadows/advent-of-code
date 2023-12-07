from puzzles.utils import *


def part1(inpt):
    points = 0
    for card in inpt:
        win, nums = card.split(' | ')
        win = win.split(': ')[-1].split()
        nums = [i for i in nums.split() if i in win]

        points += 0 if not nums else 2**(len(nums) - 1)
    return points


def part2(inpt):
    cards = { i: 1 for i in range(1, len(inpt) + 1) }
    for i, card in enumerate(inpt):
        win, nums = card.split(' | ')
        win = win.split(': ')[-1].split()

        for won in range(i + 2, i + 2 + count(True for c in nums.split() if c in win)):
            cards[won] += 1 * cards[i + 1]
    return sum(cards.values())


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 13)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 30)
        print("part 2 passed")
