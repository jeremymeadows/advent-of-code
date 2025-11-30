from puzzles.utils import *


def part1(inpt):
    direction = 0
    x, y = 0, 0

    for d in inpt.split(', '):
        count = int(d[1:])
        d = d[0]
        direction = (direction + (1 if d == 'R' else -1)) % 4

        match direction:
            case 0:
                y += count
            case 1:
                x += count
            case 2:
                y -= count
            case 3:
                x -= count

    return Point(x, y).rectilinear_distance(Point(0, 0))


def part2(inpt):
    direction = 0
    locations = set()
    x, y = 0, 0

    for d in inpt.split(', '):
        count = int(d[1:])
        d = d[0]
        direction = (direction + (1 if d == 'R' else -1)) % 4

        for _ in range(1, count + 1):
            match direction:
                case 0:
                    y += 1
                case 1:
                    x += 1
                case 2:
                    y -= 1
                case 3:
                    x -= 1

            if (x, y) in locations:
                return Point(x, y).rectilinear_distance(Point(0, 0))
            locations.add((x, y))

    return None


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = "R5, L5, R5, R3"
    inpt2 = "R8, R4, R4, R8"

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 12)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt2), 4)
        print("part 2 passed")
