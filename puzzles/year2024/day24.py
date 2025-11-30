from puzzles.utils import *


def part1(inpt):
    inputs, actions = inpt[:inpt.index("")], inpt[inpt.index("") + 1:]
    wires = {}
    for line in inputs:
        wire, value = line.split(": ")
        wires[wire] = value == "1"
    i = 0
    while len(actions) > 0:
        print(actions[i])
        value, wire = actions[i].split(" -> ")
        value = re.sub("(.+) AND (.+)", r"wires[\1] & wires[\2]", wire)
        value = re.sub("(.+) OR (.+)", r"wires[\1] | wires[\2]", wire)
        value = re.sub("(.+) XOR (.+)", r"wires[\1] ^ wires[\2]", wire)
        try:
            wires[wire] = eval(value)
            actions.pop(i)
        except:
            i = 0
        i += 1
    return wires


def part2(inpt):
    return


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "x00: 1",
        "x01: 0",
        "x02: 1",
        "x03: 1",
        "x04: 0",
        "y00: 1",
        "y01: 1",
        "y02: 1",
        "y03: 1",
        "y04: 1",
        "",
        "ntg XOR fgs -> mjb",
        "y02 OR x01 -> tnw",
        "kwq OR kpj -> z05",
        "x00 OR x03 -> fst",
        "tgd XOR rvg -> z01",
        "vdt OR tnw -> bfw",
        "bfw AND frj -> z10",
        "ffh OR nrd -> bqk",
        "y00 AND y03 -> djm",
        "y03 OR y00 -> psh",
        "bqk OR frj -> z08",
        "tnw OR fst -> frj",
        "gnj AND tgd -> z11",
        "bfw XOR mjb -> z00",
        "x03 OR x00 -> vdt",
        "gnj AND wpb -> z02",
        "x04 AND y00 -> kjc",
        "djm OR pbm -> qhw",
        "nrd AND vdt -> hwm",
        "kjc AND fst -> rvg",
        "y04 OR y02 -> fgs",
        "y01 AND x02 -> pbm",
        "ntg OR kjc -> kwq",
        "psh XOR fgs -> tgd",
        "qhw XOR tgd -> z09",
        "pbm OR djm -> kpj",
        "x03 XOR y03 -> ffh",
        "x00 XOR y04 -> ntg",
        "bfw OR bqk -> z06",
        "nrd XOR fgs -> wpb",
        "frj XOR qhw -> z04",
        "bqk OR frj -> z07",
        "y03 OR x01 -> nrd",
        "hwm AND bqk -> z03",
        "tgd XOR rvg -> z12",
        "tnw OR pbm -> gnj",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), None)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), None)
        print("part 2 passed")
