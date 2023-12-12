from puzzles.utils import *


def part1(inpt):
    options = 0
    for line in inpt:
        ucode, pattern = line.split()
        n = ucode.count('?')

        for arrangement in range(2**n):
            code = ucode
            for bit in f'{bin(arrangement)[2:]:>0{int(log2(2**n))}}':
                code = code.replace('?', '#' if bit == '1' else '.', 1)
            code = re.sub(r'\.+', '.', code).strip('.')
            
            p_chunk = pattern.split(',')
            c_chunk = code.split('.')
            if len(p_chunk) == len(c_chunk) and all(len(act) == int(exp) for exp, act in zip(p_chunk, c_chunk)):
                options += 1
    return options


def part2(inpt):
    options = 0


    @cache
    def check_next_options(code, pattern, count) -> int:
        # print('checking', code, count)
        # print('--', code)
        a = code.replace('?', '#', 1)
        b = code.replace('?', '.', 1)

        if '?' in code:
            # a = code.replace('?', '#', 1)
            # b = code.replace('?', '.', 1)
            # print(a, b)
            # print(count)

            return check_next_options(a, pattern, count) + check_next_options(b, pattern, count)
        else:
            # print(code, pattern)
            p_chunk = pattern.split(',')
            c_chunk = re.sub(r'\.+', '.', code).strip('.').split('.')
            if len(p_chunk) == len(c_chunk) and all(len(act) == int(exp) for exp, act in zip(p_chunk, c_chunk)):
                # print('found', code)
                return 1
            else:
                return 0


    for line in inpt:
        print(line)
        ucode, pattern = line.split()
        ucode, pattern = '?'.join([ucode * 5]), pattern * 5

        options += check_next_options(ucode, pattern, 0)
        check_next_options.cache_clear()
        # 
        # for arrangement in range(2**n):
        #     code = ucode
        #     for bit in f'{bin(arrangement)[2:]:>0{int(log2(2**n))}}':
        #         code = code.replace('?', '#' if bit == '1' else '.', 1)
        #     code = re.sub(r'\.+', '.', code).strip('.')
        #     
        #     p_chunk = pattern.split(',')
        #     c_chunk = code.split('.')
        #     if len(p_chunk) == len(c_chunk) and all(len(act) == int(exp) for exp, act in zip(p_chunk, c_chunk)):
        #         options += 1
    return options


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "???.### 1,1,3",
        ".??..??...?##. 1,1,3",
        "?#?#?#?#?#?#?#? 1,3,1,6",
        "????.#...#... 4,1,1",
        "????.######..#####. 1,6,5",
        "?###???????? 3,2,1",
    ]

    def test(self):
        # self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 21)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 525152)
        print("part 2 passed")
