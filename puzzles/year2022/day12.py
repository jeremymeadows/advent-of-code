from puzzles.utils import *


def part1(height_data):
    height_map, src, dest = get_height_map(height_data)
    return get_shortest_path(height_map, src, dest)


def part2(height_data):
    height_map, _, dest = get_height_map(height_data)
    possisble_starts = [
        Point(x, y)
        for x, row in enumerate(height_map)
        for y, col in enumerate(row)
        if col == 0
    ]
    return min(get_shortest_path(height_map, src, dest) for src in possisble_starts)


def get_height_map(height_data):
    height_map = []
    src = dest = None
    for row_ndx, row in enumerate(height_data):
        height_map.append([])
        for col_ndx, col in enumerate(row):
            if col == "S":
                src = Point(row_ndx, col_ndx)
                col = "a"
            elif col == "E":
                dest = Point(row_ndx, col_ndx)
                col = "z"
            height_map[-1].append(ord(col) - ord("a"))
    return height_map, src, dest


def get_shortest_path(height_map, src, dest):
    moves = [Point(1, 0), Point(0, 1), Point(-1, 0), Point(0, -1)]
    length, width = len(height_map), len(height_map[0])
    visited = [[False for _ in range(width)] for _ in range(length)]
    visited[src.x][src.y] = True

    available = [(src, 0)]
    while available:
        (src, distance) = available.pop(0)
        if src == dest:
            return distance

        for move in moves:
            next = src + move
            if (
                (0 <= next.x < length and 0 <= next.y < width)
                and height_map[next.x][next.y] <= height_map[src.x][src.y] + 1
                and not visited[next.x][next.y]
            ):
                visited[next.x][next.y] = True
                available.append((next, distance + 1))
    return float("inf")


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "Sabqponm",
        "abcryxxl",
        "accszExk",
        "acctuvwj",
        "abdefghi",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 31)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 29)
        print("part 2 passed")
