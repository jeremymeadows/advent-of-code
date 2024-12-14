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
                disk[i] = e
            else:
                disk += [e]
        i += 1
    return sum(map(product, enumerate(disk)))


def part2(inpt):
    skip = False
    disk = []

    i = 0
    for d in inpt:
        for _ in range(int(d)):
            disk += [i if not skip else '.']
        if not skip:
            i += 1
        skip = not skip

    e = i - 1
    while e != 0:
        count = disk.count(e)
        ndx = find_substring(['.'] * count, disk)
        if ndx and ndx < disk.index(e):
            disk = disk[:disk.index(e)] + ['.'] * count + disk[disk.index(e) + count:]
            disk = disk[:ndx] + [e] * count + disk[ndx + count:]
        e -= 1
    return sum([i * e for i, e in enumerate(disk) if e != '.'])


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = "2333133121414131402"

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 1928)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 2858)
        print("part 2 passed")
