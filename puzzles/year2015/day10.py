from puzzles.utils import *

ITERATIONS_1 = 40
ITERATIONS_2 = 50


def part1(sequence, iterations=ITERATIONS_1):
    return len(look_and_say(sequence, iterations))


def part2(sequence, iterations=ITERATIONS_2):
    return len(look_and_say(sequence, iterations))


def look_and_say(string: str, iterations: int) -> str:
    for _ in range(iterations):
        toks: list[str] = [string[0]]
        for ch in string[1:]:
            if ch == toks[-1][0]:
                toks[-1] += ch
            else:
                toks.append(ch)

        string = "".join(f"{len(tok)}{tok[0]}" for tok in toks)
    return string


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
        self.assertEqual(part1("1"), 82350)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2("1"), 1166642)
        print("part 2 passed")
