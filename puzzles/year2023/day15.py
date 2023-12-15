from puzzles.utils import *


def part1(inpt):
    result = 0
    for code in inpt.split(','):
        curr = 0
        for ch in code:
            curr = (curr + ord(ch)) * 17 % 256
        result += curr
    return result


def part2(inpt):
    boxes = [[] for _ in range(256)]
    code_parser = re.compile(r'(.+)([=-])(\d+)?')

    for code in inpt.split(','):
        if match := code_parser.match(code):
            label, op, num = match.groups()
        else:
            continue

        hsh = 0
        for ch in label:
            hsh = (hsh + ord(ch)) * 17 % 256
        if op == '=':
            if (n := position(lambda e: e[0] == label, boxes[hsh])) is not None:
                boxes[hsh][n] = (label, int(num))
            else:
                boxes[hsh] += [(label, int(num))]
        else:
            remove(lambda e: e[0] == label, boxes[hsh])

    power = 0
    for b, box in enumerate(boxes):
        for l, lens in enumerate(box):
            power += (b + 1) * (l + 1) * lens[1]
    return power


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 1320)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 145)
        print("part 2 passed")
