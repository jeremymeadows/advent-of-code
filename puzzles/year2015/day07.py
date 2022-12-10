from puzzles.utils import *


def part1(connections):
    return read_signals(connections)["a"]


def part2(connections):
    original_a = read_signals(connections)["a"]
    return read_signals(connections, {"b": original_a})["a"]


def read_signals(
    instructions: list[str], overrides: dict[str, int] = {}
) -> dict[str, int]:
    instructions = deepcopy(instructions)
    outputs = {}

    while len(instructions) > 0:
        completed = []
        for ndx, connection in enumerate(instructions):
            ins, out = connection.split(" -> ")
            toks = ins.split()

            try:
                match len(toks):
                    case _ if out in overrides:
                        outputs[out] = overrides[out]
                    case 1:
                        if toks[0].isnumeric():
                            outputs[out] = int(toks[0])
                        else:
                            outputs[out] = outputs[toks[0]]
                    case 2:
                        x = int(toks[1]) if toks[1].isnumeric() else outputs[toks[1]]
                        match toks[0]:
                            case "NOT":
                                outputs[out] = ~x % 2**16
                            case _:
                                raise Exception("Unknown instruction")
                    case 3:
                        a, b = [
                            int(e) if e.isnumeric() else outputs[e] for e in toks[::2]
                        ]
                        match toks[1]:
                            case "AND":
                                outputs[out] = a & b
                            case "OR":
                                outputs[out] = a | b
                            case "LSHIFT":
                                outputs[out] = a << b
                            case "RSHIFT":
                                outputs[out] = a >> b
                            case _:
                                raise Exception("Unknown instruction")
                completed += [ndx]
            except KeyError:
                continue

        for ndx in completed[::-1]:
            instructions.pop(ndx)
    return outputs


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
        self.assertEqual(
            part1(
                [
                    "123 -> x",
                    "456 -> y",
                    "x AND y -> d",
                    "x OR y -> e",
                    "x LSHIFT 2 -> f",
                    "y RSHIFT 2 -> b",
                    "NOT x -> c",
                    "NOT y -> a",
                ]
            ),
            65079,
        )
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(
            part2(
                [
                    "123 -> a",
                    "a LSHIFT 2 -> b",
                    "a AND b -> a",
                ]
            ),
            104,
        )
        print("part 2 passed")
