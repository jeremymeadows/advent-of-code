from puzzles.utils import *


def part1(forest_map):
    return len(get_visibility(forest_map)[0])


def part2(forest_map):
    return get_visibility(forest_map)[1]


def get_visibility(forest_map):
    rows = list(map(lambda e: [int(x) for x in e], forest_map))
    cols = list(map(lambda e: list(e), zip(*rows)))

    size_x = len(cols)
    size_y = len(rows)

    visible = []
    visible.extend(rows[0])
    visible.extend(rows[-1])
    visible.extend(cols[0][1:-1])
    visible.extend(cols[-1][1:-1])

    max_visibility_score = 0
    for x in range(1, size_x - 1):
        for y in range(1, size_y - 1):
            vis = False
            score = 1

            for ndx, height in enumerate(reversed(rows[x][:y])):
                if not rows[x][y] > height:
                    break
            else:
                vis = True
            score *= ndx + 1

            for ndx, height in enumerate(rows[x][y + 1 :]):
                if not rows[x][y] > height:
                    break
            else:
                vis = True
            score *= ndx + 1

            for ndx, height in enumerate(reversed(cols[y][:x])):
                if not cols[y][x] > height:
                    break
            else:
                vis = True
            score *= ndx + 1

            for ndx, height in enumerate(cols[y][x + 1 :]):
                if not cols[y][x] > height:
                    break
            else:
                vis = True
            score *= ndx + 1

            if vis:
                visible.append(rows[x][y])
            max_visibility_score = max(max_visibility_score, score)
    return visible, max_visibility_score


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 21)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 8)
        print("part 2 passed")
