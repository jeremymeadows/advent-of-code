from puzzles.utils import *

PACKET_MARKER_LEN = 4
MESSAGE_MARKER_LEN = 14


def part1(data):
    packet_start = None
    for ndx, win in enumerate(windows(data, PACKET_MARKER_LEN)):
        if len(win) == len(set(win)):
            packet_start = ndx + PACKET_MARKER_LEN
            break
    return packet_start


def part2(data):
    message_start = None
    for ndx, win in enumerate(windows(data, MESSAGE_MARKER_LEN)):
        if len(win) == len(set(win)):
            message_start = ndx + MESSAGE_MARKER_LEN
            break
    return message_start


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 7)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 19)
        print("part 2 passed")
