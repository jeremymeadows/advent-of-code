from puzzles.utils import *


def part1(guests):
    preferences = {}
    for guest in guests:
        a, pos_neg, num, b = parse_guest_list(guest)

        if a not in preferences:
            preferences[a] = {}
        preferences[a][b] = int(num) * {"gain": 1, "lose": -1}[pos_neg]
    return calculate_optimal_happiness(preferences)


def part2(guests):
    preferences = {"self": {}}
    for guest in guests:
        a, pos_neg, num, b = parse_guest_list(guest)

        if a not in preferences:
            preferences[a] = {"self": 0}
            preferences["self"][a] = 0
        preferences[a][b] = int(num) * {"gain": 1, "lose": -1}[pos_neg]
    return calculate_optimal_happiness(preferences)


def parse_guest_list(guest):
    return re.match(r"(\w+) \w+ (\w+) (\d+) .+ (\w+)", guest).groups()


def calculate_optimal_happiness(preferences):
    max_happiness = float("-inf")
    for seats in permutations(preferences.keys()):
        arrangement_happiness = sum(
            [preferences[a][b] + preferences[b][a] for a, b in windows(seats, 2)]
        )
        arrangement_happiness += (
            preferences[seats[0]][seats[-1]] + preferences[seats[-1]][seats[0]]
        )
        max_happiness = max(max_happiness, arrangement_happiness)
    return max_happiness


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "Alice would gain 54 happiness units by sitting next to Bob.",
        "Alice would lose 79 happiness units by sitting next to Carol.",
        "Alice would lose 2 happiness units by sitting next to David.",
        "Bob would gain 83 happiness units by sitting next to Alice.",
        "Bob would lose 7 happiness units by sitting next to Carol.",
        "Bob would lose 63 happiness units by sitting next to David.",
        "Carol would lose 62 happiness units by sitting next to Alice.",
        "Carol would gain 60 happiness units by sitting next to Bob.",
        "Carol would gain 55 happiness units by sitting next to David.",
        "David would gain 46 happiness units by sitting next to Alice.",
        "David would lose 7 happiness units by sitting next to Bob.",
        "David would gain 41 happiness units by sitting next to Carol.",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 330)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 286)
        print("part 2 passed")
