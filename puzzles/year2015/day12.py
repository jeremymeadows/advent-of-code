from puzzles.utils import *


def part1(js):
    return sum([int(e.group(0)) for e in re.finditer(r"-?\d+", js)])


def part2(js):
    js = [json.loads(js)]
    purge_dict({"": js})
    return sum([int(e.group(0)) for e in re.finditer(r"-?\d+", json.dumps(js))])


def purge_dict(d: dict):
    for k in deepcopy(d):
        if type(d[k]) == dict:
            if purge_dict(d[k]):
                del d[k]
        elif type(d[k]) == list:
            purge_list(d[k])
        elif d[k] == "red":
            return True
    return False


def purge_list(l: list):
    rem = []
    for i in range(len(l)):
        if type(l[i]) == dict:
            if purge_dict(l[i]):
                rem.append(i)
        elif type(l[i]) == list:
            purge_list(l[i])
    for ndx in rem[::-1]:
        del l[ndx]


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
        self.assertEqual(part1("[1,2,3]"), 6)
        self.assertEqual(part1('{"a":2,"b":4}'), 6)
        self.assertEqual(part1("[[[3]]]"), 3)
        self.assertEqual(part1('{"a":{"b":4},"c":-1}'), 3)
        self.assertEqual(part1('{"a":[-1,1]}'), 0)
        self.assertEqual(part1('[-1,{"a":1}]'), 0)
        self.assertEqual(part1("[]"), 0)
        self.assertEqual(part1("{}"), 0)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2("[1,2,3]"), 6)
        self.assertEqual(part2('[1,{"c":"red","b":2},3]'), 4)
        self.assertEqual(part2('{"d":"red","e":[1,2,3,4],"f":5}'), 0)
        self.assertEqual(part2('[1,"red",5]'), 6)
        print("part 2 passed")
