from puzzles.utils import *


def part1(inpt):
    seeds = { seed: seed for seed in map(int, inpt[0].split(': ')[1].split()) }
    for mapping in '\n'.join(inpt[2:]).split('\n\n'):
        for seed, curr in seeds.items():
            for dst, src, rng in ((int(i) for i in m.split()) for m in mapping.split('\n')[1:]):
                if (i := curr - src) >= 0 and i < rng:
                    seeds[seed] = dst + i
                    break
    return min(seeds.values())


def part2(inpt):
    seed_ranges = deque((int(s), int(s + n), int(0)) for s, n in chunks([i for i in inpt[0].split(': ')[1].split()], 2))
    maps = [[tuple(map(int, e.split())) for e in i[1:]] for i in map(lambda e: e.split('\n'), '\n'.join(inpt[2:]).split('\n\n'))]

    # seed_ranges = deque([seed_ranges[0]])
    closest = float('inf')

    while len(seed_ranges) != 0:
        start, end, m = seed_ranges.popleft()

        if m == len(maps):
            closest = min(closest, start)
            continue

        print(f'seeds: {start}-{end - 1} with map {m}')
        for mapping in maps[m]:
            map_range = (mapping[1], mapping[1] + mapping[2])
            map_diff = mapping[0] - mapping[1]

            print(f'  mapping {map_range[0]}-{map_range[1] - 1} to {map_range[0] + map_diff}-{map_range[1] + map_diff - 1}')
            if overlap := range_intersection((start, end), map_range):
                for a, b in split_range((start, end), overlap):
                    if a in range(*map_range):
                        print(f'    {(a, b - 1)} to {(a + map_diff, b + map_diff - 1)}')
                        seed_ranges.append((a + map_diff, b + map_diff, m + 1))
                    else:
                        print(f'    {(a, b - 1)} to {(a, b - 1)} (retry)')
                        seed_ranges.appendleft((a, b, m))
                break
        else:
            print(f'  no change for {start}-{end - 1}')
            seed_ranges.append((start, end, m + 1))

    return closest
    # 593433105 high
    # 231612163 high
    # 930661260
    # 634347552
    # 1296352523
    # 54576670 high


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 35)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 46)
        print("part 2 passed")
