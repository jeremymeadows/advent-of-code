from puzzles.utils import *


def part1(medicine, formulae):
    replacements = get_replacements(formulae)

    molecules = set()
    for old, new in replacements:
        ndx = 0
        while (s := medicine.find(old, ndx)) != -1:
            molecules.add(medicine[:s] + new + medicine[s + len(old) :])
            ndx = s + len(old)
    return len(molecules)


def part2(medicine, formulae):
    replacements = get_replacements(formulae)

    steps = 0
    while medicine != "e":
        for new, old in replacements:
            if (s := medicine.find(old)) != -1:
                medicine = medicine[:s] + new + medicine[s + len(old) :]
                steps += 1
                break
    return steps


def get_replacements(replacement_formulae):
    replacements = []
    for replacement in replacement_formulae:
        src, dst = replacement.split(" => ")
        replacements.append((src, dst))
    return sorted(replacements, key=lambda x: len(x[1]), reverse=True)


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt[-1], inpt[:-2])}")
    print(f"part 2: {part2(inpt[-1], inpt[:-2])}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1("HOH", ["H => HO", "H => OH", "O => HH"]), 4)
        self.assertEqual(part1("HOHOHO", ["H => HO", "H => OH", "O => HH"]), 7)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(
            part2("HOH", ["e => H", "e => O", "H => HO", "H => OH", "O => HH"]), 3
        )
        self.assertEqual(
            part2("HOHOHO", ["e => H", "e => O", "H => HO", "H => OH", "O => HH"]), 6
        )
        print("part 2 passed")
