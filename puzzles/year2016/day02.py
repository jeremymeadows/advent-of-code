from puzzles.utils import *


def part1(inpt):
    x, y = 1, 1
    keypad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    code = ''

    for line in inpt:
        for c in line:
            match c:
                case 'U':
                    y = max(0, y - 1)
                case 'D':
                    y = min(2, y + 1)
                case 'L':
                    x = max(0, x - 1)
                case 'R':
                    x = min(2, x + 1)
        code += keypad[y][x]
    return code


def part2(inpt):
    machine = StateMachine('5')

    machine.add_transitions(chain(
        [('1', d, '1') for d in 'ULR'],
        [('2', d, '2') for d in 'UL'],
        [('4', d, '4') for d in 'UR'],
        [('5', d, '5') for d in 'UDL'],
        [('9', d, '9') for d in 'UDR'],
        [('A', d, 'A') for d in 'LD'],
        [('C', d, 'C') for d in 'DR'],
        [('D', d, 'D') for d in 'DLR'],
    ))
    machine.add_transitions([
        ('1', 'D', '3'),
        ('5', 'R', '6'),
        ('9', 'L', '8'),
        ('D', 'U', 'B'),
    ])
    machine.add_transitions(chain(
        [('2', d, n) for d, n in [('R', '3'), ('D', '6')]],
        [('3', d, n) for d, n in [('U', '1'), ('R', '4'), ('D', '7'), ('L', '2')]],
        [('4', d, n) for d, n in [('D', '8'), ('L', '3')]],
        [('6', d, n) for d, n in [('U', '2'), ('R', '7'), ('D', 'A'), ('L', '5')]],
        [('7', d, n) for d, n in [('U', '3'), ('R', '8'), ('D', 'B'), ('L', '6')]],
        [('8', d, n) for d, n in [('U', '4'), ('R', '9'), ('D', 'C'), ('L', '7')]],
        [('A', d, n) for d, n in [('U', '6'), ('R', 'B')]],
        [('B', d, n) for d, n in [('U', '7'), ('R', 'C'), ('D', 'D'), ('L', 'A')]],
        [('C', d, n) for d, n in [('U', '8'), ('L', 'B')]],
    ))

    code = ''
    for line in inpt:
        for c in line:
            machine.transition(c)
        code += machine.current_state
    return code


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "ULL",
        "RRDDD",
        "LURDL",
        "UUUUD",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), '1985')
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), '5DB3')
        print("part 2 passed")
