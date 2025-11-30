from puzzles.utils import *


def part1(inpt):
    password = ''
    i = 0

    while len(password) < 8:
        hsh = md5(f'{inpt}{i}'.encode()).hexdigest()
        if hsh.startswith('00000'):
            password += hsh[5]
        i += 1

    return password


def part2(inpt):
    password = [''] * 8
    i = 0

    while any([not e for e in password]):
        hsh = md5(f'{inpt}{i}'.encode()).hexdigest()
        if hsh.startswith('00000') and ((ndx := int(hsh[5], 16)) < 8) and not password[ndx]:
            password[ndx] = hsh[6]
        i += 1

    return ''.join(password)


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = 'abc'

    def test(self):
        # self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), '18f47a30')
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), '05ace8e3')
        print("part 2 passed")
