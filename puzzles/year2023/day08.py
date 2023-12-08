from puzzles.utils import *


def part1(inpt):
    directions = cycle(d for d in inpt[0])
    dir_map = { loc: to[1:-1].split(', ') for loc, to in map(lambda e: e.split(' = '), inpt[2:]) }

    location = 'AAA'
    steps = 0

    while location != 'ZZZ':
        location = dir_map[location][0 if next(directions) == 'L' else 1]
        steps += 1
    return steps


def part2(inpt):
    dir_map = { loc: to[1:-1].split(', ') for loc, to in map(lambda e: e.split(' = '), inpt[2:]) }
    all_paths = {loc: 0 for loc in dir_map if loc.endswith('A')}

    for loc in all_paths:
        directions = cycle(d for d in inpt[0])
        location = loc
        steps = 0

        while not location.endswith('Z'):
            location = dir_map[location][0 if next(directions) == 'L' else 1]
            steps += 1
        all_paths[loc] = steps

    return lcm(*all_paths.values())


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "RL",
        "",
        "AAA = (BBB, CCC)",
        "BBB = (DDD, EEE)",
        "CCC = (ZZZ, GGG)",
        "DDD = (DDD, DDD)",
        "EEE = (EEE, EEE)",
        "GGG = (GGG, GGG)",
        "ZZZ = (ZZZ, ZZZ)",
    ]

    inpt2 = [
        "LR",
        "",
        "11A = (11B, XXX)",
        "11B = (XXX, 11Z)",
        "11Z = (11B, XXX)",
        "22A = (22B, XXX)",
        "22B = (22C, 22C)",
        "22C = (22Z, 22Z)",
        "22Z = (22B, 22B)",
        "XXX = (XXX, XXX)",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 2)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt2), 6)
        print("part 2 passed")
