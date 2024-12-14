from puzzles.utils import *


def part1(inpt):
    stones = list(map(int, inpt.split()))
    for _ in range(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones += ['1']
            elif len(str(stone)) % 2 == 0:
                sstone = str(stone)
                new_stones += [int(sstone[:len(sstone)//2]), int(sstone[len(sstone)//2:])]
            else:
                new_stones += [stone * 2024]
        stones = [int(stone) for stone in new_stones]
    return len(stones)


def part2(inpt):
    return


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = "125 17"

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 55312)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), None)
        print("part 2 passed")
