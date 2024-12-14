from puzzles.utils import *


def part1(inpt):
    skip = False
    disk = []

    i = 0
    for d in inpt:
        for _ in range(int(d)):
            disk += [i if not skip else '.']
        if not skip:
            i += 1
        skip = not skip

    i = 0
    while i < len(disk):
        if disk[i] == '.':
            while (e := disk.pop()) == '.':
                pass

            if i < len(disk):
                print(i, len(disk))
                disk[i] = e
            else:
                disk += [e]
        i += 1
    return sum(map(product, enumerate(disk)))


def part2(inpt):
    return


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = "2333133121414131402"

    # 6288338133779 low
    # 6288599492129

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 1928)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), None)
        print("part 2 passed")
