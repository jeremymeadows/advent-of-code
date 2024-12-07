from puzzles.utils import *


def part1(inpt):
    i = inpt.index("")
    rules = {}
    for k, v in map(lambda e: list(map(int, e.split('|'))), inpt[:i]):
        rules[k] = rules.get(k, []) + [v]
    books = list(map(lambda e: list(map(int, e.split(','))), inpt[i+1:]))

    nums = 0
    for book in books:
        ordered = True
        for i, num in enumerate(book):
            if any([e not in rules.get(num, []) for e in book[i + 1:]]):
                ordered = False
                break
        if ordered:
            nums += book[len(book) // 2]
    return nums


def part2(inpt):
    i = inpt.index("")
    rules = {}
    for k, v in map(lambda e: list(map(int, e.split('|'))), inpt[:i]):
        rules[k] = rules.get(k, []) + [v]
    books = list(map(lambda e: list(map(int, e.split(','))), inpt[i+1:]))
    incorrect = []

    for book in books:
        for i, num in enumerate(book):
            if any([e not in rules.get(num, []) for e in book[i + 1:]]):
                incorrect += [book]
                break
    for book in incorrect:
        i = 0
        while i < len(book):
            updated = False
            j = i + 1
            while j < len(book):
                if book[j] not in rules.get(book[i], []):
                    book[j], book[i] = book[i], book[j]
                    updated = True
                j += 1
            if not updated:
                i += 1
    return sum(book[len(book) // 2] for book in incorrect)


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "61|13",
        "75|53",
        "29|13",
        "97|29",
        "53|29",
        "61|53",
        "97|53",
        "61|29",
        "47|13",
        "75|47",
        "97|75",
        "47|61",
        "75|61",
        "47|29",
        "75|13",
        "53|13",
        "",
        "75,47,61,53,29",
        "97,61,53,29,13",
        "75,29,13",
        "75,97,47,61,53",
        "61,13,29",
        "97,13,75,29,47"
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 143)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 123)
        print("part 2 passed")
