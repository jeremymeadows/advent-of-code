from puzzles.utils import *


def part1(assignments):
    full_duplicates = 0
    for assignment in assignments:
        a_start, a_end, b_start, b_end = get_assignment_ranges(assignment)
        if (
            a_start >= b_start
            and a_end <= b_end
            or b_start >= a_start
            and b_end <= a_end
        ):
            full_duplicates += 1
    return full_duplicates


def part2(assignments):
    part_duplicates = 0
    for assignment in assignments:
        a_start, a_end, b_start, b_end = get_assignment_ranges(assignment)
        if (
            a_start >= b_start
            and a_end <= b_end
            or b_start >= a_start
            and b_end <= a_end
            or a_start >= b_start
            and a_start <= b_end
            or b_start >= a_start
            and b_start <= a_end
        ):
            part_duplicates += 1
    return part_duplicates


def get_assignment_ranges(assignment):
    a, b = assignment.split(",")
    return *map(lambda e: int(e), a.split("-")), *map(lambda e: int(e), b.split("-"))


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 2)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 4)
        print("part 2 passed")
