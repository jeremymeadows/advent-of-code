from puzzles.utils import *


def part1(inpt):
    pattern = re.compile(r'\[(.+?)\]')
    tls = 0

    for ip in inpt:
        for hypernet in pattern.findall(ip):
            if any(w == w[::-1] and w != w[0] * 4 for w in windows(hypernet, 4)):
                break
        else:
            if any(w == w[::-1] and w != w[0] * 4 for w in windows(pattern.sub('-', ip), 4)):
                tls += 1
    return tls


def part2(inpt):
    pattern = re.compile(r'\[(.+?)\]')
    ssl = 0

    for ip in inpt:
        addr = pattern.sub('-', ip)
        for hypernet in pattern.findall(ip):
            if any(''.join([w[1], w[0], w[1]]) in addr for w in windows(hypernet, 3) if w == w[::-1] and w[0] != w[1]):
                ssl += 1
    return ssl


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "abba[mnop]qrst",
        "abcd[bddb]xyyx",
        "aaaa[qwer]tyui",
        "ioxxoj[asdfgh]zxcvbn",
    ]

    inpt2 = [
        "aba[bab]xyz",
        "xyx[xyx]xyx",
        "aaa[kek]eke",
        "zazbz[bzb]cdb",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 2)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt2), 3)
        print("part 2 passed")
