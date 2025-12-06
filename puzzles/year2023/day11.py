from puzzles.utils import *


def part1(inpt):
    star_map = rotate_matrix(inpt)
    for i, row in reversed(list(enumerate(star_map))):
        if not '#' in row:
            star_map.insert(i, row)
    star_map = rotate_matrix(star_map)
    for i, row in reversed(list(enumerate(star_map))):
        if not '#' in row:
            star_map.insert(i, row)

    galaxies = []
    for y, row in enumerate(star_map):
        for x in find_all(lambda e: e == '#', row):
            galaxies += [Point(x, y)]

    distance = 0
    for i, galaxy in enumerate(galaxies):
        for g in galaxies[i + 1:]:
            distance += galaxy.rectilinear_distance(g)

    return distance


def part2(inpt):
    distances = ([0] * len(inpt[0]), [0] * len(inpt))
    star_map = rotate_matrix(inpt)
    expansion_factor = 1_000_000

    for i, row in enumerate(star_map[:-1]):
        if not '#' in row:
            distances[0][i + 1] = distances[0][i] + expansion_factor
        else:
            distances[0][i + 1] = distances[0][i] + 1

    star_map = rotate_matrix(star_map)
    for i, row in enumerate(star_map[:-1]):
        if not '#' in row:
            distances[1][i + 1] = distances[1][i] + expansion_factor
        else:
            distances[1][i + 1] = distances[1][i] + 1

    galaxies = []
    for y, row in enumerate(star_map):
        for x in find_all(lambda e: e == '#', row):
            galaxies += [Point(distances[0][x], distances[1][y])]
    
    distance = 0
    for i, galaxy in enumerate(galaxies):
        for g in galaxies[i + 1:]:
            distance += galaxy.rectilinear_distance(g)

    return distance


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#.....",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 374)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 82000210)
        print("part 2 passed")
