from puzzles.utils import *


def part1(inpt):
    x, y = -1, -1
    for i, line in enumerate(inpt):
        if (j := line.find('S')) != -1:
            x, y = j, i
            break

    direction = 'down'
    steps = 1
    y += 1

    while (loc := inpt[y][x]) != 'S':
        match loc:
            case '|':
                y += 1 if direction == 'down' else -1
                steps += 1
            case '-':
                x += 1 if direction == 'right' else -1
                steps += 1
            case 'L':
                match direction:
                    case 'down':
                        x += 1
                        direction = 'right'
                    case 'left':
                        y -= 1
                        direction = 'up'
                steps += 1
            case 'J':
                match direction:
                    case 'down':
                        x -= 1
                        direction = 'left'
                    case 'right':
                        y -= 1
                        direction = 'up'
                steps += 1
            case 'F':
                match direction:
                    case 'up':
                        x += 1
                        direction = 'right'
                    case 'left':
                        y += 1
                        direction = 'down'
                steps += 1
            case '7':
                match direction:
                    case 'up':
                        x -= 1
                        direction = 'left'
                    case 'right':
                        y += 1
                        direction = 'down'
                steps += 1
            case _:
                raise Exception('invalid path detected')
    return steps // 2


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
        "..F7.",
        ".FJ|.",
        "SJ.L7",
        "|F--J",
        "LJ...",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 8)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), None)
        print("part 2 passed")
