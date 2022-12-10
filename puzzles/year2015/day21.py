from puzzles.utils import *

SHOP = {
    "weapons": {
        "Dagger": (8, 4, 0),
        "Shortsword": (10, 5, 0),
        "Warhammer": (25, 6, 0),
        "Longsword": (40, 7, 0),
        "Greataxe": (74, 8, 0),
    },
    "armor": {
        "None": (0, 0, 0),
        "Leather": (13, 0, 1),
        "Chainmail": (31, 0, 2),
        "Splintmail": (53, 0, 3),
        "Bandedmail": (75, 0, 4),
        "Platemail": (102, 0, 5),
    },
    "rings": {
        "None": (0, 0, 0),
        "Damage +1": (25, 1, 0),
        "Damage +2": (50, 2, 0),
        "Damage +3": (100, 3, 0),
        "Defense +1": (20, 0, 1),
        "Defense +2": (40, 0, 2),
        "Defense +3": (80, 0, 3),
    },
}


def part1(boss_stats):
    return min(combat(*boss_stats)[0])


def part2(boss_stats):
    return max(combat(*boss_stats)[1])


def item_sets():
    for weapon in SHOP["weapons"]:
        for armor in SHOP["armor"]:
            for ring1 in SHOP["rings"]:
                for ring2 in SHOP["rings"]:
                    if ring1 == ring2 and ring1 != "None":
                        continue
                    yield SHOP["weapons"][weapon], SHOP["armor"][armor], SHOP["rings"][
                        ring1
                    ], SHOP["rings"][ring2]


@cache
def combat(boss_hp, boss_damage, boss_armor, player_hp=100):
    victory_costs = set()
    defeat_costs = set()

    for items in item_sets():
        hp = player_hp
        boss = boss_hp

        cost = sum([e[0] for e in items])
        damage = sum([e[1] for e in items])
        armor = sum([e[2] for e in items])

        while hp > 0:
            boss -= max(1, damage - boss_armor)
            if boss <= 0:
                break
            hp -= max(1, boss_damage - armor)
        if boss <= 0:
            victory_costs.add(cost)
        else:
            defeat_costs.add(cost)
    return victory_costs, defeat_costs


def main():
    inpt = [int(line.split(": ")[-1]) for line in get_input(__file__)]
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [24, 14, 4]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 40)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 215)
        print("part 2 passed")
