from puzzles.utils import *


def part1(inpt):
    steps, parts = split(inpt, '')
    instruction = re.compile(r'(.)(.)(\d+):(.+)')

    steps = { k: v.split(',') for k, v in map(lambda e: e[:-1].split('{'), steps) }
    parts = [{ k: int(v) for k, v in map(lambda e: e.split('='), part[1:-1].split(','))} for part in parts ]

    accepted = 0
    for part in parts:
        workflow = 'in'
        while workflow is not None:
            for step in steps[workflow]:
                if match := instruction.match(step):
                    component, op, val, dest = match.groups()
                    if eval(f'{part[component]}{op}{val}'):
                        workflow = dest
                        break
                else:
                    workflow = step

            if workflow == 'A':
                accepted += sum(part.values())
                workflow = None
            elif workflow == 'R':
                workflow = None
    return accepted


def part2(inpt):
    steps = { k: v.split(',') for k, v in map(lambda e: e[:-1].split('{'), inpt[:inpt.index('')]) }
    print(steps)
    return len(steps)


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "px{a<2006:qkq,m>2090:A,rfg}",
        "pv{a>1716:R,A}",
        "lnx{m>1548:A,A}",
        "rfg{s<537:gd,x>2440:R,A}",
        "qs{s>3448:A,lnx}",
        "qkq{x<1416:A,crn}",
        "crn{x>2662:A,R}",
        "in{s<1351:px,qqz}",
        "qqz{s>2770:qs,m<1801:hdj,R}",
        "gd{a>3333:R,R}",
        "hdj{m>838:A,pv}",
        "",
        "{x=787,m=2655,a=1222,s=2876}",
        "{x=1679,m=44,a=2067,s=496}",
        "{x=2036,m=264,a=79,s=2244}",
        "{x=2461,m=1339,a=466,s=291}",
        "{x=2127,m=1623,a=2188,s=1013}",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 19114)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 167409079868000)
        print("part 2 passed")
