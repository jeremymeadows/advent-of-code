from puzzles.utils import *


def part1(inpt):
    screen = [['.'] * 50 for _ in range(6)]
    pattern = re.compile(r'(.+?) .=(\d+) by (\d+)')

    for line in inpt:
        command, args = line.split(maxsplit=1)
        match command:
            case 'rect':
                x, y = map(int, args.split('x'))
                for j in range(y):
                    for i in range(x):
                        screen[j][i] = '#'
            case 'rotate':
                if match := pattern.search(args):
                    direction, num, amt = match.groups()
                    num, amt = int(num), int(amt)

                    if direction == 'column':
                        screen = reverse_matrix(screen)
                    screen[num] = screen[num][-amt:] + screen[num][:-amt]
                    if direction == 'column':
                        screen = reverse_matrix(screen)
    return [e for row in screen for e in row].count('#')


def part2(inpt):
    screen = [['.'] * 50 for _ in range(6)]
    pattern = re.compile(r'(.+?) .=(\d+) by (\d+)')

    for line in inpt:
        command, args = line.split(maxsplit=1)
        match command:
            case 'rect':
                x, y = map(int, args.split('x'))
                for j in range(y):
                    for i in range(x):
                        screen[j][i] = '#'
            case 'rotate':
                if match := pattern.search(args):
                    direction, num, amt = match.groups()
                    num, amt = int(num), int(amt)

                    if direction == 'column':
                        screen = reverse_matrix(screen)
                    screen[num] = screen[num][-amt:] + screen[num][:-amt]
                    if direction == 'column':
                        screen = reverse_matrix(screen)
    return '\n' + '\n'.join(''.join(row) for row in screen)


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "rect 3x2",
        "rotate column x=1 by 1",
        "rotate row y=0 by 4",
        "rotate column x=1 by 1",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 6)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), '''
....#.#...........................................
#.#...............................................
.#................................................
.#................................................
..................................................
..................................................''')
        print("part 2 passed")
