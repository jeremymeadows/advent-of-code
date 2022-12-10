from puzzles.utils import *

STEPS = 100


def part1(pattern, steps=STEPS):
    lights = [[{".": False, "#": True}[col] for col in row] for row in pattern]
    return list(chain(*animate_lights(lights, steps))).count(True)


def part2(pattern, steps=STEPS):
    lights = [[{".": False, "#": True}[col] for col in row] for row in pattern]
    return list(chain(*animate_lights(lights, steps, always_on_corners=True))).count(
        True
    )


def animate_lights(
    lights: list[list[bool]],
    steps: int,
    *,
    always_on_corners: bool = False,
) -> list[list[bool]]:
    num_lights = len(lights)

    def light_corners():
        lights[0][0] = True
        lights[0][-1] = True
        lights[-1][0] = True
        lights[-1][-1] = True

    if always_on_corners:
        light_corners()

    for _ in range(steps):
        framebuffer = deepcopy(lights)
        for x in range(num_lights):
            for y in range(num_lights):
                neighbors = [
                    lights[x - 1][y - 1] if x > 0 and y > 0 else False,
                    lights[x - 1][y] if x > 0 else False,
                    lights[x - 1][y + 1] if x > 0 and y < num_lights - 1 else False,
                    lights[x][y - 1] if y > 0 else False,
                    lights[x][y + 1] if y < num_lights - 1 else False,
                    lights[x + 1][y - 1] if x < num_lights - 1 and y > 0 else False,
                    lights[x + 1][y] if x < num_lights - 1 else False,
                    lights[x + 1][y + 1]
                    if x < num_lights - 1 and y < num_lights - 1
                    else False,
                ]
                if lights[x][y]:
                    if sum(neighbors) not in [2, 3]:
                        framebuffer[x][y] = False
                else:
                    if sum(neighbors) == 3:
                        framebuffer[x][y] = True
        lights = framebuffer
        if always_on_corners:
            light_corners()
    return lights


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    STEPS = 4

    inpt = [
        ".#.#.#",
        "...##.",
        "#....#",
        "..#...",
        "#.#..#",
        "####..",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt, Test.STEPS), 4)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt, Test.STEPS), 14)
        print("part 2 passed")
