from puzzles.utils import *


def part1(inpt):
    hands = [(hand, int(bid)) for hand, bid in map(lambda e: e.split(), inpt)]
    ranks = { typ: [] for typ in ['five', 'four', 'full', 'three', 'double', 'two', 'one'] }

    for (hand, bid) in hands:
        counts = Counter(hand).most_common()
        if counts[0][1] == 5:
            ranks['five'] += [(hand, bid)]
        elif counts[0][1] == 4:
            ranks['four'] += [(hand, bid)]
        elif [e[1] for e in counts] == [3, 2]:
            ranks['full'] += [(hand, bid)]
        elif counts[0][1] == 3:
            ranks['three'] += [(hand, bid)]
        elif [e[1] for e in counts[:2]] == [2, 2]:
            ranks['double'] += [(hand, bid)]
        elif counts[0][1] == 2:
            ranks['two'] += [(hand, bid)]
        else:
            ranks['one'] += [(hand, bid)]

    return sum(map(lambda e: (e[0] + 1) * e[1][1],
       enumerate(reversed(list(
            chain.from_iterable(sorted(lst, key=lambda e: e[0].translate(
                str.maketrans('23456789TJQKA', 'abcdefghijklm')
            ), reverse=True) for lst in ranks.values())
        )))
    ))


def part2(inpt):
    hands = [(hand, int(bid)) for hand, bid in map(lambda e: e.split(), inpt)]
    ranks = { typ: [] for typ in ['five', 'four', 'full', 'three', 'double', 'two', 'one'] }

    for (hand, bid) in hands:
        counts = Counter(hand.replace('J', '')).most_common()
        jokers = count([c for c in hand if c == 'J'])

        counts += [('J', jokers)]
        counts[0] = (counts[0][0], counts[0][1] + jokers)

        if counts[0][1] >= 5:
            ranks['five'] += [(hand, bid)]
        elif counts[0][1] == 4:
            ranks['four'] += [(hand, bid)]
        elif [e[1] for e in counts[:2]] == [3, 2]:
            ranks['full'] += [(hand, bid)]
        elif counts[0][1] == 3:
            ranks['three'] += [(hand, bid)]
        elif [e[1] for e in counts[:2]] == [2, 2]:
            ranks['double'] += [(hand, bid)]
        elif counts[0][1] == 2:
            ranks['two'] += [(hand, bid)]
        else:
            ranks['one'] += [(hand, bid)]

    return sum(map(lambda e: (e[0] + 1) * e[1][1],
       enumerate(reversed(list(
            chain.from_iterable(sorted(lst, key=lambda e: e[0].translate(
                str.maketrans('23456789TJQKA', 'abcdefghi-klm')
            ), reverse=True) for lst in ranks.values())
        )))
    ))


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 6440)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 5905)
        print("part 2 passed")
