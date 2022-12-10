from puzzles.utils import *


def part1(crate_layout, instructions):
    crates = find_crates(crate_layout)
    moves = parse_instructions(instructions)

    version_a = deepcopy(crates)
    for count, src, dest in moves:
        for _ in range(count):
            version_a[dest].append(version_a[src].pop())
    return "".join([version_a[key][-1] for key in sorted(version_a.keys())])


def part2(crate_layout, instructions):
    crates = find_crates(crate_layout)
    moves = parse_instructions(instructions)

    version_b = deepcopy(crates)
    for count, src, dest in moves:
        for i in range(count):
            version_b[dest].append(version_b[src].pop(i - count))
    return "".join([version_b[key][-1] for key in sorted(version_b.keys())])


def find_crates(crate_layout):
    crates: dict[int, list[str]] = {}
    for row in crate_layout:
        for ndx, col in enumerate(chunks(row, 4)):
            if col[1] != " ":
                if not crates.get(ndx + 1):
                    crates[ndx + 1] = []
                crates[ndx + 1].insert(0, col[1])
    return crates


def parse_instructions(instructions):
    moves: list[tuple[int, int, int]] = []
    for row in instructions:
        count, src, dest = [int(tok) for col, tok in enumerate(row.split()) if col % 2]
        moves.append((count, src, dest))
    return moves


def main():
    inpt = get_input(__file__)
    ndx = inpt.index("")
    print(f"part 1: {part1(inpt[:ndx - 1], inpt[ndx + 1:])}")
    print(f"part 2: {part2(inpt[:ndx - 1], inpt[ndx + 1:])}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        [
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
        ],
        [
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2",
        ],
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(*Test.inpt), "CMZ")
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(*Test.inpt), "MCD")
        print("part 2 passed")
