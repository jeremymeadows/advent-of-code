from puzzles.utils import *

ITERATIONS = 2022

WIDTH = 7

ROCKS = [
    e.split()
    for e in """
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
""".split(
        "\n\n"
    )
]


def part1(inpt):
    jet_pattern = [e for e in inpt]
    heights = [0] * WIDTH
    for i in range(ITERATIONS):
        height = max(heights)
        rock_ndx = i % len(ROCKS)
        direction = jet_pattern[i % len(jet_pattern)]
        pos: list[tuple[int, int]] = None
        match rock_ndx:
            case 0:
                pos = [(2, height + 3), (3, height + 3), (4, height + 3), (5, height + 3)]
            case 1:
                pos = [(2, height + 4), (3, height + 3), (3, height + 5), (4, height + 4)]
            case 2:
                pos = [(2, height + 3), (3, height + 3), (4, height + 3), (4, height + 4), (4, height + 5)]
            case 3:
                pos = [(2, height + 3), (2, height + 4), (3, height + 3), (3, height + 4)]
            case n:
                raise Exception(f"invalid rock index ({n})")

        while pos != (next_pos := fall(pos, heights, direction)):
            pos = next_pos

        for x, y in pos:
            heights[x] = max(heights[x], y)

    return max(heights)


def part2(inpt):
    return


def fall(position: list[tuple[int, int]], heights: list[int], direction: str) -> list[tuple[int, int]]:
    pos = deepcopy(position)
    direction = -1 if direction == '<' else 1
    if all(map(lambda x, y: y > heights[x], pos)):
        pass
    return pos

def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 3068)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), None)
        print("part 2 passed")
