from puzzles.utils import *

START = Point(500, 0)


def part1(walls):
    walls = get_walls(walls)
    infinite_pit = max(point.y for wall in walls for point in wall)
    obstacles = get_obstacles(walls)

    grains_of_sand = 0
    while (point := landing_location(obstacles, infinite_pit)).y != infinite_pit:
        obstacles.add(point)
        grains_of_sand += 1
    return grains_of_sand


def part2(walls):
    walls = get_walls(walls)
    floor = max(point.y for wall in walls for point in wall) + 2
    obstacles = get_obstacles(walls + [[Point(0, floor), Point(1000, floor)]])

    grains_of_sand = 0
    while (point := landing_location(obstacles, floor)) != START:
        obstacles.add(point)
        grains_of_sand += 1
    return grains_of_sand + 1


def get_walls(walls) -> list[list[Point]]:
    return [
        [Point(int(x), int(y)) for x, y in [w.split(",") for w in wall]]
        for wall in [wall.split(" -> ") for wall in walls]
    ]


def get_obstacles(walls) -> set[Point]:
    obstacles = set()
    for wall in walls:
        for start, end in windows(wall, 2):
            if start.x == end.x:
                for y in range(min(start.y, end.y), max(start.y, end.y) + 1):
                    obstacles.add(Point(start.x, y))
            elif start.y == end.y:
                for x in range(min(start.x, end.x), max(start.x, end.x) + 1):
                    obstacles.add(Point(x, start.y))
    return obstacles


def landing_location(obstacles, max_depth):
    point = START
    while point.y < max_depth:
        if (new := point + Point(0, 1)) not in obstacles:
            point = new
        elif (new := point + Point(-1, 1)) not in obstacles:
            point = new
        elif (new := point + Point(1, 1)) not in obstacles:
            point = new
        else:
            break
    return point


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "498,4 -> 498,6 -> 496,6",
        "503,4 -> 502,4 -> 502,9 -> 494,9",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 24)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 93)
        print("part 2 passed")
