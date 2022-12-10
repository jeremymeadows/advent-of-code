from puzzles.utils import *

PRIORITIES: list[str] = [
    chr(i) for i in chain(range(ord("a"), ord("z") + 1), range(ord("A"), ord("Z") + 1))
]


def part1(inventory_list):
    misplaced_priority = 0
    for bag in inventory_list:
        contents = BitVec()
        a, b = bag[: len(bag) // 2], bag[len(bag) // 2 :]

        for item in a:
            contents[ord(item) - ord("A")] = True

        for item in b:
            if contents[ord(item) - ord("A")]:
                misplaced_priority += PRIORITIES.index(item) + 1
                break
    return misplaced_priority


def part2(inventory_list):
    GROUP_SIZE = 3

    badge_priority = 0
    for group in chunks(inventory_list, GROUP_SIZE):
        bags = [0] * GROUP_SIZE

        for elf in range(GROUP_SIZE):
            for ch in group[elf]:
                bags[elf] |= 1 << ord(ch) - ord("A")

        badge = reduce(lambda a, b: a & b, bags)
        badge = chr(int(log2(badge)) + ord("A"))
        badge_priority += PRIORITIES.index(badge) + 1
    return badge_priority


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 157)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 70)
        print("part 2 passed")
