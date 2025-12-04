from puzzles.utils import *


def part1(inpt):
    rolls = inpt
    free = 0

    for row in range(len(rolls)):
        for col in range(len(rolls[row])):
            adj = 0
            cell = rolls[row][col]
            if cell == "@":
                if row > 0:
                    adj += rolls[row - 1][max(col - 1, 0):min(col + 2, len(rolls[row]))].count("@")
                if row < len(rolls) - 1:
                    adj += rolls[row + 1][max(col - 1, 0):min(col + 2, len(rolls[row]))].count("@")
                if col > 0 and rolls[row][col - 1] == "@":
                    adj += 1
                if col < len(rolls[row]) - 1 and rolls[row][col + 1] == "@":
                    adj += 1
                
                if adj < 4:
                    free += 1
    return free

def part2(inpt):
    rolls = inpt
    free = 0
    repeat = True

    while repeat:
        repeat = False
        for row in range(len(rolls)):
            for col in range(len(rolls[row])):
                adj = 0
                cell = rolls[row][col]
                if cell == "@":
                    if row > 0:
                        adj += rolls[row - 1][max(col - 1, 0):min(col + 2, len(rolls[row]))].count("@")
                    if row < len(rolls) - 1:
                        adj += rolls[row + 1][max(col - 1, 0):min(col + 2, len(rolls[row]))].count("@")
                    if col > 0 and rolls[row][col - 1] == "@":
                        adj += 1
                    if col < len(rolls[row]) - 1 and rolls[row][col + 1] == "@":
                        adj += 1
                    
                    if adj < 4:
                        rolls[row] = rolls[row][:col] + "X" + rolls[row][col + 1:]
                        free += 1
                        repeat = True
    return free


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 13)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 43)
        print("part 2 passed")
