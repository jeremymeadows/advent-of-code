from puzzles.utils import *


def part1(inpt):
    matches = re.findall(r"mul\((\d+,\d+)\)", "".join(inpt))
    return sum(int(a) * int(b) for match in matches for a, b in [match.split(",")])


def part2(inpt):
    val = 0
    inpt = "".join(inpt)
    dos = [0] + [i.start() for i in re.finditer(r"do\(\)", inpt)]
    donts = [i.start() for i in re.finditer(r"don't\(\)", inpt)] + [len(inpt)]
    ranges = []

    while donts:
        if len(dos) > 0 and dos[0] < donts[0]:
            ranges.append((dos.pop(0), donts.pop(0)))
            while len(dos) > 0 and dos[0] < ranges[-1][1]:
                dos.pop(0)
        else:
            donts.pop(0)

    for start, end in ranges:
        muls = re.findall(r"mul\((\d+,\d+)\)", inpt[start:end])
        val += sum(int(a) * int(b) for match in muls for a, b in [match.split(",")])
    return val


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    inpt2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 161)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt2), 48)
        print("part 2 passed")
