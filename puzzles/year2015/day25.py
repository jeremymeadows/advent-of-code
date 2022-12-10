from puzzles.utils import *

INITIAL_CODE = 20151125
FACTOR = 252533
MODULO = 33554393


def part1(row, col):
    return get_code(row, col)


def get_code(row: int, col: int) -> int:
    code_num = sum(range(row + col - 1)) + col

    code = INITIAL_CODE
    for _ in range(1, code_num):
        code = (code * FACTOR) % MODULO
    return code


def main():
    inpt = [
        int(e)
        for e in re.match(r".*row (\d+), column (\d+)", get_input(__file__)).groups()
    ]
    print(f"part 1: {part1(*inpt)}")
    print("MERRY CHRISTMAS!")


if __name__ == "__main__":
    main()


class Test(TestCase):
    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(2, 1), 31916031)
        self.assertEqual(part1(6, 6), 27995004)
        print("part 1 passed")

    def test_part2(self):
        print("MERRY CHRISTMAS!")
