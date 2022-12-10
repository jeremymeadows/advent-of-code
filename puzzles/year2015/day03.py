from puzzles.utils import *


def part1(directions):
    pos_x, pos_y = 0, 0
    houses = set([(pos_x, pos_y)])
    for move in directions:
        match move:
            case "^":
                pos_y -= 1
            case "v":
                pos_y += 1
            case ">":
                pos_x += 1
            case "<":
                pos_x -= 1
        houses.add((pos_x, pos_y))
    return len(houses)


def part2(directions):
    pos_x, pos_y = 0, 0
    robot_x, robot_y = 0, 0
    houses = set([(pos_x, pos_y)])

    for move in directions[::2]:
        match move:
            case "^":
                pos_y -= 1
            case "v":
                pos_y += 1
            case ">":
                pos_x += 1
            case "<":
                pos_x -= 1
        houses.add((pos_x, pos_y))

    for move in directions[1::2]:
        match move:
            case "^":
                robot_y -= 1
            case "v":
                robot_y += 1
            case ">":
                robot_x += 1
            case "<":
                robot_x -= 1
        houses.add((robot_x, robot_y))

    return len(houses)


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(">"), 2)
        self.assertEqual(part1("^>v<"), 4)
        self.assertEqual(part1("^v^v^v^v^v"), 2)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2("^v"), 3)
        self.assertEqual(part2("^>v<"), 3)
        self.assertEqual(part2("^v^v^v^v^v"), 11)
        print("part 2 passed")
