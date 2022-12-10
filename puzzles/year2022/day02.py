from puzzles.utils import *


CODEBOOK: dict[str, int] = {
    "A": 1,
    "X": 1,
    "B": 2,
    "Y": 2,
    "C": 3,
    "Z": 3,
}


def part1(guide):
    score = 0
    for opponent, move in guide:
        opponent = CODEBOOK[opponent]
        move = CODEBOOK[move]

        score += move
        match (opponent - move) % 3:
            case 0:  # draw
                score += 3
            case 2:  # win
                score += 6
    return score


def part2(guide):
    score = 0
    for opponent, outcome in guide:
        opponent = CODEBOOK[opponent]

        match outcome:
            case "X":  # lose
                score += (opponent - 2) % 3 + 1
            case "Y":  # draw
                score += 3 + opponent
            case "Z":  # win
                score += 6 + (opponent) % 3 + 1
    return score


def main():
    inpt = [e.split() for e in get_input(__file__)]
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        ("A", "Y"),
        ("B", "X"),
        ("C", "Z"),
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 15)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 12)
        print("part 2 passed")
