from puzzles.utils import *


ptr = 0
a, b, c = 0, 0, 0
output = []

def get_combo_op(op):
    global a, b, c
    match op:
        case 0 | 1 | 2 | 3:
            return op
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c
        case 7 | _:
            raise ValueError


def adv(op):
    global a
    a = a // 2 ** get_combo_op(op)


def bxl(op):
    global b
    b ^= op


def bst(op):
    global b
    b = get_combo_op(op) & 0b111


def jnz(op):
    global ptr, a
    if a != 0:
        ptr = op
        return True


def bxc(_):
    global b, c
    b ^= c


def out(op):
    global output
    output += [get_combo_op(op) & 0b111]


def bdv(op):
    global a, b
    b = a // 2 ** get_combo_op(op)


def cdv(op):
    global a, c
    c = a // 2 ** get_combo_op(op)


def part1(inpt):
    global ptr, a, b, c, output
    a = int(inpt[0].split(' ')[-1])
    b = int(inpt[1].split(' ')[-1])
    c = int(inpt[2].split(' ')[-1])
    program = [int(i) for i in inpt[4].split(' ')[-1].split(',')]

    while ptr < len(program) - 1:
        inst, oper = program[ptr], program[ptr + 1]
        ret = [adv, bxl, bst, jnz, bxc, out, bdv, cdv][inst](oper)
        if ret is None:
            ptr += 2
    return ','.join(map(str, output))


def part2(inpt):
    return


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "Register A: 729",
        "Register B: 0",
        "Register C: 0",
        "",
        "Program: 0,1,5,4,3,0",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), "4,6,3,5,6,3,5,2,1,0")
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), None)
        print("part 2 passed")
