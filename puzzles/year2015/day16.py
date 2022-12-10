from puzzles.utils import *

DETECTED = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def part1(aunt_info):
    sues = get_aunt_properties(aunt_info)

    for ndx, sue in enumerate(sues):
        for prop in sue:
            if sue[prop] != DETECTED[prop]:
                break
        else:
            break
    return ndx + 1


def part2(aunt_info):
    sues = get_aunt_properties(aunt_info)

    for ndx, sue in enumerate(sues):
        for prop in sue:
            match prop:
                case "cats" | "trees":
                    if not sue[prop] > DETECTED[prop]:
                        break
                case "pomeranians" | "goldfish":
                    if not sue[prop] < DETECTED[prop]:
                        break
                case _:
                    if sue[prop] != DETECTED[prop]:
                        break
        else:
            break
    return ndx + 1


def get_aunt_properties(aunt_info):
    aunt_sues = []
    for sue in aunt_info:
        aunt_sues.append(
            {
                prop: int(val)
                for prop, val in [
                    prop.split(": ") for prop in sue.split(": ", 1)[-1].split(", ")
                ]
            }
        )
    return aunt_sues


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "Sue 1: goldfish: 5, trees: 3, akitas: 0",
        "Sue 2: perfumes: 1, cats: 1, samoyeds: 0",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 1)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 2)
        print("part 2 passed")
