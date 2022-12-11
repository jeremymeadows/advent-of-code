from puzzles.utils import *

ITERATIONS_1 = 20
ITERATIONS_2 = 10000


class Monkey:
    def __init__(self):
        self.num_inspections = 0
        self.starting_items = []
        self.operation = None
        self.test = None
        self.if_true = None
        self.if_false = None


def part1(monkey_info):
    monkeys = get_monkeys(monkey_info)
    return get_monkey_business(monkeys, ITERATIONS_1)


def part2(monkey_info):
    monkeys = get_monkeys(monkey_info)
    return get_monkey_business(monkeys, ITERATIONS_2, decrease_worry=False)


def get_monkeys(monkey_info: list[str]) -> list[Monkey]:
    monkeys = []
    for line in monkey_info:
        if line.startswith("Monkey"):
            monkeys.append(Monkey())
        elif line.startswith("  Starting items"):
            monkeys[-1].starting_items = [
                int(x) for x in line.split(": ")[1].split(", ")
            ]
        elif line.startswith("  Operation"):
            monkeys[-1].operation = eval(
                line.split(": ")[1].replace("new =", "lambda old:")
            )
        elif line.startswith("  Test"):
            monkeys[-1].test = int(line.split()[-1])
        elif line.startswith("    If true"):
            monkeys[-1].if_true = int(line.split()[-1])
        elif line.startswith("    If false"):
            monkeys[-1].if_false = int(line.split()[-1])
    return monkeys


def get_monkey_business(
    monkeys: list[Monkey], rounds: int, *, decrease_worry: bool = True
) -> int:
    common_mod = product(map(lambda monkey: monkey.test, monkeys))
    for _ in range(rounds):
        for monkey in monkeys:
            while len(monkey.starting_items) > 0:
                monkey.num_inspections += 1
                item = monkey.operation(monkey.starting_items.pop())

                if decrease_worry:
                    item //= 3

                monkeys[
                    monkey.if_true if item % monkey.test == 0 else monkey.if_false
                ].starting_items.append(item % common_mod)
    return product(sorted(map(lambda m: m.num_inspections, monkeys), reverse=True)[:2])


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "Monkey 0:",
        "  Starting items: 79, 98",
        "  Operation: new = old * 19",
        "  Test: divisible by 23",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 3",
        "",
        "Monkey 1:",
        "  Starting items: 54, 65, 75, 74",
        "  Operation: new = old + 6",
        "  Test: divisible by 19",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 0",
        "",
        "Monkey 2:",
        "  Starting items: 79, 60, 97",
        "  Operation: new = old * old",
        "  Test: divisible by 13",
        "    If true: throw to monkey 1",
        "    If false: throw to monkey 3",
        "",
        "Monkey 3:",
        "  Starting items: 74",
        "  Operation: new = old + 3",
        "  Test: divisible by 17",
        "    If true: throw to monkey 0",
        "    If false: throw to monkey 1",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 10605)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 2713310158)
        print("part 2 passed")
