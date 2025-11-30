from puzzles.utils import *


def part1(inpt):
    ptr = 0
    decompressed = ''

    while ptr < len(inpt):
        if inpt[ptr] == '(':
            marker = ''
            ptr += 1
            while inpt[ptr] != ')':
                marker += inpt[ptr]
                ptr += 1
            ptr += 1
            length, count = map(int, marker.split('x'))
            decompressed += inpt[ptr:ptr + length] * count
            ptr += length - 1
        else:
            decompressed += inpt[ptr]
        ptr += 1
    return len(decompressed)


def part2(inpt):
    marker_pattern = re.compile(r'^(\(\d+x\d+\))(.*)')

    def calculate_len(s: str) -> int:
        length = 0
        while len(s) > 0:
            if (match := marker_pattern.search(s)):
                marker, s = match.groups()
                l, c = map(int, marker[1:-1].split('x'))

                length += calculate_len(s[:l]) * c
                s = s[l:]
            else:
                length += 1
                s = s[1:]
        return length

    return calculate_len(inpt)


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = 'ADVENTA(1x5)BC(3x3)XYZA(2x2)BCD(2x2)EFG(6x1)(1x3)AX(8x2)(3x3)ABCY'
    inpt2 = '(3x3)XYZX(8x2)(3x3)ABCY(27x12)(20x12)(13x14)(7x10)(1x12)A(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 57)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt2), 242394)
        print("part 2 passed")
