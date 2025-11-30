from puzzles.utils import *


def part1(inpt, dest):
    num = int(inpt)

    steps = deque([(int(1), int(1), int(0))])
    visited = set()
    shortest = float('inf')

    while len(steps) > 0:
        x, y, d = steps.popleft()
        visited.add((x, y))

        if (x, y) == dest:
            shortest = min(shortest, d)
            continue

        for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if (nx, ny) not in visited and get_location(nx, ny, num) % 2 == 0:
                steps.append((nx, ny, d + 1))
    return shortest


def part2(inpt):
    num = int(inpt)

    steps = deque([(int(1), int(1), int(0))])
    visited = set()
    arrive_under_50 = set()

    while len(steps) > 0:
        x, y, d = steps.popleft()
        visited.add((x, y))

        if d <= 50:
            arrive_under_50.add((x, y))
        if d == 50:
            continue

        for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if (nx, ny) not in visited and get_location(nx, ny, num) % 2 == 0:
                steps.append((nx, ny, d + 1))
    return len(arrive_under_50)
    # 217 high


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt, (31, 39))}")
    print(f"part 2: {part2(inpt)}")


def get_location(x, y, n) -> int:
    return (x * x + 3 * x + 2 * x * y + y + y * y + n).bit_count()


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = '10'

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt, (7, 4)), 11)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), None)
        print("part 2 passed")
