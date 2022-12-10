from puzzles.utils import *


def part1(movements):
    return len(get_tail_positions(movements, 2))


def part2(movements):
    return len(get_tail_positions(movements, 10))


def get_tail_positions(movements, rope_len) -> set[tuple[int, int]]:
    knots = [Point() for _ in range(rope_len)]
    tail_positions = set()

    for direction, distance in movements:
        for _ in range(int(distance)):
            match direction:
                case "U":
                    knots[0].y += 1
                case "D":
                    knots[0].y -= 1
                case "L":
                    knots[0].x -= 1
                case "R":
                    knots[0].x += 1

            for i in range(1, len(knots)):
                head = knots[i - 1]
                tail = knots[i]

                x, y = head - tail
                if (d := head.distance(tail)) == 2:
                    tail.x += x // 2
                    tail.y += y // 2
                elif d > 2:
                    tail.x += copysign(1, x)
                    tail.y += copysign(1, y)
            tail_positions.add((knots[-1].x, knots[-1].y))
    return tail_positions


def main():
    inpt = [e.split() for e in get_input(__file__)]
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        ("R", "4"),
        ("U", "4"),
        ("L", "3"),
        ("D", "1"),
        ("R", "4"),
        ("D", "1"),
        ("L", "5"),
        ("R", "2"),
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 13)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 1)
        print("part 2 passed")
