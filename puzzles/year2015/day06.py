from puzzles.utils import *


def part1(instructions):
    lights = [[False for _ in range(1000)] for _ in range(1000)]
    for instruction in instructions:
        mode, x1, y1, x2, y2 = parse_instruction(instruction)

        match mode:
            case "turn on":
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        lights[x][y] = True
            case "turn off":
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        lights[x][y] = False
            case "toggle":
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        lights[x][y] = not lights[x][y]
    return list(chain(*lights)).count(True)


def part2(instructions):
    fancy_lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for instruction in instructions:
        mode, x1, y1, x2, y2 = parse_instruction(instruction)

        match mode:
            case "turn on":
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        fancy_lights[x][y] += 1
            case "turn off":
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        fancy_lights[x][y] -= 1
                        fancy_lights[x][y] = max(0, fancy_lights[x][y])
            case "toggle":
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        fancy_lights[x][y] += 2
    return sum(chain(*fancy_lights))


def parse_instruction(instruction):
    toks = re.match(r"(.+) (\d+),(\d+) .+ (\d+),(\d+)", instruction).groups()
    return toks[0], *[int(e) for e in toks[1:]]


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(["turn on 0,0 through 999,999"]), 1000000)
        self.assertEqual(part1(["toggle 0,0 through 999,0"]), 1000)
        self.assertEqual(part1(["turn off 499,499 through 500,500"]), 0)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(["turn on 0,0 through 0,0"]), 1)
        self.assertEqual(part2(["toggle 0,0 through 999,999"]), 2000000)
        print("part 2 passed")
