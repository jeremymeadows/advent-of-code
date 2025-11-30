from puzzles.utils import *


def part1(inpt):
    pattern = re.compile(r'(.+)-(\d+)\[(.+)\]')
    real = 0
    for line in inpt:
        if not (match := pattern.match(line)):
            continue

        name, sector, checksum = match.groups()
        name = name.replace('-', '')

        if ''.join([e[0] for e in sorted(sorted(Counter(name).most_common(), key=lambda e: e[0]), key=lambda e: e[1], reverse=True)][:5]) == checksum:
            real += int(sector)
    return real


def part2(inpt):
    pattern = re.compile(r'(.+)-(\d+)\[(.+)\]')

    for line in inpt:
        if not (match := pattern.match(line)):
            continue

        name, sector, _ = match.groups()
        name = name.replace('-', '')

        for i in range(26):
            if ''.join(chr((ord(c) - 97 + i) % 26 + 97) for c in name) == 'northpoleobjectstorage':
                return sector


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "aaaaa-bbb-z-y-x-123[abxyz]",
        "a-b-c-d-e-f-g-h-987[abcde]",
        "not-a-real-room-404[oarel]",
        "totally-real-room-200[decoy]",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 1514)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), None)
        print("part 2 passed")
