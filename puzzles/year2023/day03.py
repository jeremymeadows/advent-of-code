from puzzles.utils import *


def part1(inpt):
    max_len = max(map(len, inpt))
    for i, row in enumerate(inpt):
        inpt[i] = f'{row:.<{max_len}}'

    part_sum = 0
    symbol = re.compile(r'[^0-9.]')

    for y, row in enumerate(inpt):
        num = ''
        part = False
        for x, char in enumerate(row):
            if char.isdigit():
                num += char

                part = part or bool(symbol.search(''.join([
                    inpt[max(0, y - 1)][max(0, x - 1):min(max_len, x + 2)] if y > 0 else '',
                    inpt[max(0, y)][max(0, x - 1):min(max_len, x + 2)],
                    inpt[max(0, y + 1)][max(0, x - 1):min(max_len, x + 2)] if y < len(inpt) - 1 else '',
                ])))

            if num and (not char.isdigit() or x == max_len - 1):
                if part:
                    part_sum += int(num)
                num = ''
                part = False
    return part_sum


def part2(inpt):
    max_len = max(map(len, inpt))
    for i, row in enumerate(inpt):
        inpt[i] = f'{row:.<{max_len}}'

    gear_map = {}
    for y, row in enumerate(inpt):
        num = ''
        gear_locs = []
        for x, char in enumerate(row):
            if char.isdigit():
                num += char

                neighbors = [
                    inpt[max(0, y - 1)][max(0, x - 1):min(max_len, x + 2)] if y > 0 else '...',
                    inpt[max(0, y)][max(0, x - 1):min(max_len, x + 2)],
                    inpt[max(0, y + 1)][max(0, x - 1):min(max_len, x + 2)] if y < len(inpt) - 1 else '...',
                ]

                if '*' in ''.join(neighbors):
                    if x == 0:
                        for i in range(3):
                            neighbors[i] = '.' + neighbors[i]
                    elif x == max_len - 1:
                        for i in range(3):
                            neighbors[i] = neighbors[i] + '.'
                    
                    for i in range(3):
                        if (ndx := neighbors[i].find('*')) != -1:
                            gear_locs += [(x + (ndx - 1), y + (i - 1))]

            if num and (not char.isdigit() or x == max_len - 1):
                for loc in set(gear_locs):
                    gear_map[loc] = (gear_map.get(loc) or []) + [int(num)]
                num = ''
                gear_locs.clear()
    return sum(product(gears) for gears in gear_map.values() if len(gears) == 2)


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 4361)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 467835)
        print("part 2 passed")
