from puzzles.utils import *


def part1(inpt):
    x, y = -1, -1
    for y, line in enumerate(inpt):
        if (x := line.find('S')) != -1:
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
    x, y = -1, -1
    for y, line in enumerate(inpt):
        if (x := line.find('S')) != -1:
            break

    direction = 'down'
    steps = 1
    path = set([(x, y)])
    y += 1

    while (loc := inpt[y][x]) != 'S':
        path.add((x, y))

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

    position = 'out'
    enclosed_spaces = 0
    for y, row in enumerate(inpt):
        for x, col in enumerate(row):
            if col == 'S':
                col = '|' if inpt[y - 1][x] == 'F' else 'F'

            if (x, y) in path:
                match col:
                    case '|':
                        position = { 'in': 'out', 'out': 'in' }[position]
                    case 'F' | 'L':
                        position = f'border-{position}-{col}'
                    case '7':
                        _, pos, key = position.split('-')
                        position = pos if key == 'F' else { 'in': 'out', 'out': 'in' }[pos]
                    case 'J':
                        _, pos, key = position.split('-')
                        position = pos if key == 'L' else { 'in': 'out', 'out': 'in' }[pos]
                    case _:
                        pass
            elif position == 'in':
                enclosed_spaces += 1
    return enclosed_spaces


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

    inpt2 = [
        "...........",
        ".S-------7.",
        ".|F-----7|.",
        ".||.....||.",
        ".||.....||.",
        ".|L-7.F-J|.",
        ".|..|.|..|.",
        ".L--J.L--J.",
        "...........",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 8)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt2), 4)
        print("part 2 passed")
