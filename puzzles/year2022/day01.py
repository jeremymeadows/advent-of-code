from puzzles.utils import *


def part1(calories):
    return max(calories_per_elf(calories))


def part2(calories):
    return sum(sorted(calories_per_elf(calories), reverse=True)[:3])


def calories_per_elf(calories):
    ndx = 0
    elves = [0]
    for calories_carried in calories:
        if not calories_carried:
            ndx += 1
            elves += [0]
        else:
            elves[ndx] += int(calories_carried)
    return elves


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 24000)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 45000)
        print("part 2 passed")
