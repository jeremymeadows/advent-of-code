from puzzles.utils import *


def part1(inpt):
    games = []
    for line in inpt:
        gid, rounds = line.split(': ')
        gid = gid[6:]
        game = { 'red': 0, 'green': 0, 'blue': 0 }

        for d in rounds.split('; '):
            for pull in d.split(', '):
                count, color = pull.split()
                game[color] = max(int(count), game[color])
        games.append(game)

    return sum(i + 1 for i, g in enumerate(games) if g['red'] <= 12 and g['green'] <= 13 and g['blue'] <= 14)


def part2(inpt):
    games = []
    for line in inpt:
        gid, rounds = line.split(': ')
        gid = gid[6:]
        game = { 'red': 0, 'green': 0, 'blue': 0 }

        for d in rounds.split('; '):
            for pull in d.split(', '):
                count, color = pull.split()
                game[color] = max(int(count), game[color])
        games.append(game)

    return sum(g['red'] * g['green'] * g['blue'] for g in games)


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 8)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 2286)
        print("part 2 passed")
