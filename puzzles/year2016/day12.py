from puzzles.utils import *


def part1(inpt):
    instructions = [list(line.split()) for line in inpt]
    registers = { r: 0 for r in 'abcd' }
    pc = 0

    while pc < len(instructions):
        match instructions[pc]:
            case 'cpy', x, y:
                if x.isnumeric():
                    registers[y] = int(x)
                else:
                    registers[y] = registers[x]
            case 'inc', r:
                registers[r] += 1
            case 'dec', r:
                registers[r] -= 1
            case 'jnz', r, d:
                if r.isnumeric() and int(r) != 0 or registers[r] != 0:
                    pc += int(d) - 1
        pc += 1
    return registers['a']


def part2(inpt):
    instructions = [list(line.split()) for line in inpt]
    registers = { 'a': 0, 'b': 0, 'c': 1, 'd': 1 }
    pc = 0

    while pc < len(instructions):
        match instructions[pc]:
            case 'cpy', x, y:
                if x.isnumeric():
                    registers[y] = int(x)
                else:
                    registers[y] = registers[x]
            case 'inc', r:
                registers[r] += 1
            case 'dec', r:
                registers[r] -= 1
            case 'jnz', r, d:
                if r.isnumeric() and int(r) != 0 or registers[r] != 0:
                    pc += int(d) - 1
        pc += 1
    return registers['a']


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "cpy 41 a",
        "inc a",
        "inc a",
        "dec a",
        "jnz a 2",
        "dec a",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 42)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 42)
        print("part 2 passed")
