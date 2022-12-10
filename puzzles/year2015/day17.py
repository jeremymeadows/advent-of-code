from puzzles.utils import *

AMOUNT_OF_EGGNOG = 150


def part1(containers, amount=AMOUNT_OF_EGGNOG):
    combos = get_container_combinations(containers, amount)
    return len(combos)


def part2(containers, amount=AMOUNT_OF_EGGNOG):
    combos = get_container_combinations(containers, amount)
    optimal_combo_size = min(map(len, combos))
    return count(filter(lambda combo: len(combo) == optimal_combo_size, combos))


def get_container_combinations(containers, amount):
    combos = []
    for i in range(1, len(containers) + 1):
        for j in combinations(containers, i):
            if sum(j) == amount:
                combos.append(j)
    return combos


def main():
    inpt = [int(i) for i in get_input(__file__)]
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    AMOUNT_OF_EGGNOG = 25

    inpt = [20, 15, 10, 5, 5]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt, Test.AMOUNT_OF_EGGNOG), 4)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt, Test.AMOUNT_OF_EGGNOG), 3)
        print("part 2 passed")
