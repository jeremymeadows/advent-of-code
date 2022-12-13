from puzzles.utils import *


class Ordering(Enum):
    Less = -1
    Equal = 0
    Greater = 1

    def __eq__(self, other: int):
        return self.value == other


def part1(packets):
    correct = 0
    for ndx, [a, b] in enumerate(split(packets, "")):
        a, b = json.loads(a), json.loads(b)
        if cmp(a, b) == Ordering.Less:
            correct += ndx + 1
    return correct


def part2(packets):
    DIVIDER_PACKETS = [[[2]], [[6]]]

    packets = sorted(
        [json.loads(p) for p in packets if p != ""] + DIVIDER_PACKETS,
        key=cmp_to_key(cmp),
    )
    return product(
        [packets.index(DIVIDER_PACKETS[i]) + 1 for i in range(len(DIVIDER_PACKETS))]
    )


def cmp(a, b):
    types = (type(a), type(b))
    if types == (int, int):
        return (a > b) - (a < b)
    elif types == (int, list):
        return cmp([a], b)
    elif types == (list, int):
        return cmp(a, [b])
    elif types == (list, list):
        for i in range(min(len(a), len(b))):
            if c := cmp(a[i], b[i]):
                return c
        return cmp(len(a), len(b))


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "[1,1,3,1,1]",
        "[1,1,5,1,1]",
        "",
        "[[1],[2,3,4]]",
        "[[1],4]",
        "",
        "[9]",
        "[[8,7,6]]",
        "",
        "[[4,4],4,4]",
        "[[4,4],4,4,4]",
        "",
        "[7,7,7,7]",
        "[7,7,7]",
        "",
        "[]",
        "[3]",
        "",
        "[[[]]]",
        "[[]]",
        "",
        "[1,[2,[3,[4,[5,6,7]]]],8,9]",
        "[1,[2,[3,[4,[5,6,0]]]],8,9]",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 13)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 140)
        print("part 2 passed")
