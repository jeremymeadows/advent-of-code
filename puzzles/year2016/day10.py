from puzzles.utils import *


def part1(inpt):
    final = [3, 5] if len(inpt) == 6 else [61, 17]
    value_parser = re.compile(r'value (\d+) goes to bot (\d+)')
    action_parser = re.compile(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)')
    actions = {}
    bots = {}
    outputs = {}

    for line in inpt:
        if (match := action_parser.match(line)):
            initial, dst_low, n_low, dst_high, n_high = match.groups()
            actions[int(initial)] = (bots if dst_low == 'bot' else outputs, int(n_low), bots if dst_high == 'bot' else outputs, int(n_high))

    for line in inpt:
        modified_bots = []

        if (match := value_parser.match(line)):
            value, bot = map(int, match.groups())
            bots[bot] = (bots.get(bot) or []) + [value]
            modified_bots += [bot]

            while modified_bots:
                bot = modified_bots.pop()
                if len(bots[bot]) == 2:
                    low, high = sorted(bots[bot])
                    if [low, high] == final or [high, low] == final:
                        return int(bot)

                    dst_low, n_low, dst_high, n_high = actions[bot]
                    dst_low[n_low] = (dst_low.get(n_low) or []) + [low]
                    dst_high[n_high] = (dst_high.get(n_high) or []) + [high]

                    modified_bots += [n_low, n_high]


def part2(inpt):
    value_parser = re.compile(r'value (\d+) goes to bot (\d+)')
    action_parser = re.compile(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)')
    actions = {}
    bots = {}
    outputs = {}

    for line in inpt:
        if (match := action_parser.match(line)):
            initial, dst_low, n_low, dst_high, n_high = match.groups()
            actions[int(initial)] = (bots if dst_low == 'bot' else outputs, int(n_low), bots if dst_high == 'bot' else outputs, int(n_high))

    for line in inpt:
        modified_bots = []

        if (match := value_parser.match(line)):
            value, bot = map(int, match.groups())
            bots[bot] = (bots.get(bot) or []) + [value]
            modified_bots += [bot]

            while modified_bots:
                bot = modified_bots.pop()
                if len(bots[bot]) == 2:
                    low, high = sorted(bots[bot])

                    dst_low, n_low, dst_high, n_high = actions[bot]
                    dst_low[n_low] = (dst_low.get(n_low) or []) + [low]
                    dst_high[n_high] = (dst_high.get(n_high) or []) + [high]

                    modified_bots += [n_low, n_high]

    return outputs[0][0] * outputs[1][0] * outputs[2][0]


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "value 5 goes to bot 2",
        "bot 2 gives low to bot 1 and high to bot 0",
        "value 3 goes to bot 1",
        "bot 1 gives low to output 1 and high to bot 0",
        "bot 0 gives low to output 2 and high to output 0",
        "value 2 goes to bot 2",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 0)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), None)
        print("part 2 passed")
