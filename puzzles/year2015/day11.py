from puzzles.utils import *

ALPHABET_FULL = "abcdefghijlkmnopqrstuvwxyz"
ALPHABET = "abcdefghjkmnpqrstuvwxyz"
LENGTH = 8


def part1(password):
    while not is_valid(password):
        password = increment(password)
    return password


def part2(password):
    password = increment(part1(password))
    while not is_valid(password):
        password = increment(password)
    return password


def is_valid(password: str) -> bool:
    if not re.match(rf"[{ALPHABET}]" + "{8}", password):
        return False

    if not re.match(r".*(.)\1.*(.)\2.*", password):
        return False

    for w in windows(password, 3):
        if "".join(w) in ALPHABET_FULL:
            return True

    return False


def increment(password: str) -> str:
    for ndx, ch in enumerate(password):
        if ch not in ALPHABET:
            password = (password[:ndx] + chr(ord(ch) + 1)).ljust(LENGTH, ALPHABET[0])
            break

    for i in range(len(password) - 1, -1, -1):
        if password[i] == ALPHABET[-1]:
            password = password[:i] + ALPHABET[0] + password[i + 1 :]
        else:
            password = (
                password[:i]
                + ALPHABET[ALPHABET.index(password[i]) + 1]
                + password[i + 1 :]
            )
            break

    return password


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
        self.assertEqual(part1("abcdefgh"), "abcdffaa")
        self.assertEqual(part1("ghijklmn"), "ghjaabcc")
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2("abcdefgh"), "abcdffbb")
        self.assertEqual(part2("ghijklmn"), "ghjbbcdd")
        print("part 2 passed")
