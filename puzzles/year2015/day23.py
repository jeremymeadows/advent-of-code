from puzzles.utils import *


def part1(instructions):
    return run_program(instructions, {"a": 0, "b": 0})["b"]


def part2(instructions):
    return run_program(instructions, {"a": 1, "b": 0})["b"]


def run_program(instructions, initial_state: dict[str, int]) -> dict[str, int]:
    counter = 0
    registers = deepcopy(initial_state)

    while counter < len(instructions):
        match instructions[counter]:
            case "hlf", reg:
                registers[reg] //= 2
            case "tpl", reg:
                registers[reg] *= 3
            case "inc", reg:
                registers[reg] += 1
            case "jmp", offset:
                counter += int(offset) - 1
            case "jie", reg, offset:
                if registers[reg] % 2 == 0:
                    counter += int(offset) - 1
            case "jio", reg, offset:
                if registers[reg] == 1:
                    counter += int(offset) - 1
        counter += 1
    return registers


def main():
    inpt = [e.replace(",", "").split() for e in get_input()]
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(
            part1(
                [
                    "inc a",
                    "jio a +2",
                    "tpl a",
                    "inc a",
                ]
            ),
            0,
        )
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(
            part2(
                [
                    "inc a",
                    "jio a +2",
                    "tpl a",
                    "inc b",
                ]
            ),
            0,
        )
        print("part 2 passed")
