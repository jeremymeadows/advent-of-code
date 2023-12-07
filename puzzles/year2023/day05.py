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
    seed_ranges = [(s, s + n) for s, n in chunks([int(i) for i in inpt[0].split(': ')[1].split()], 2)]
    seeds = {}
    print(seed_ranges)

    # for start, count in seed_ranges:
    #     while count > 0:
    #         seeds[start + count - 1] = start + count - 1
    #         count -= 1

    for mapping in '\n'.join(inpt[2:]).split('\n\n'):
        print(mapping.split('\n')[0])
        for seed_range in seed_ranges:
            for dst, src, rng in ((int(i) for i in m.split()) for m in mapping.split('\n')[1:]):
                if (r := range_intersection(seed_range, (src, src + rng))):
                    for seed in range(r[0], r[1] + 1):
                        seeds[seed] = 
        # for seed, curr in seeds.items():
        #     for dst, src, rng in ((int(i) for i in m.split()) for m in mapping.split('\n')[1:]):
        #         if (i := curr - src) >= 0 and i < rng:
        #             seeds[seed] = dst + i
        #             break

    return min(seeds.values())


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
