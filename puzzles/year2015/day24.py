from puzzles.utils import *


def part1(present_weights):
    NUM_GROUPS = 3

    groups = divide_even_groups(present_weights, NUM_GROUPS)
    smallest_group = min(groups, key=lambda e: (len(e), product(e)))
    return product(smallest_group)


def part2(present_weights):
    NUM_GROUPS = 4

    groups = divide_even_groups(present_weights, NUM_GROUPS)
    smallest_group = min(groups, key=lambda e: (len(e), product(e)))
    return product(smallest_group)


def divide_even_groups(lst, n):
    weight = sum(lst) // n
    groups = set()
    for i in range(1, len(lst) - n + 1):
        for j in combinations(lst, i):
            if sum(j) == weight:
                groups.add(j)
    return groups


def main():
    inpt = [int(e) for e in get_input(__file__)]
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 99)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 44)
        print("part 2 passed")
