from puzzles.utils import *

TIME_LIMIT = 2503


def part1(reindeer_info, time_limit=TIME_LIMIT):
    reindeer = get_reindeer_stats(reindeer_info)

    distances = {name: 0 for name in reindeer}
    for name in reindeer:
        distances[name] = calc_distance(*reindeer[name], time_limit)
    return max(distances.values())


def part2(reindeer_info, time_limit=TIME_LIMIT):
    reindeer = get_reindeer_stats(reindeer_info)

    distances = {name: 0 for name in reindeer}
    points = {name: 0 for name in reindeer}
    for seconds in range(1, time_limit + 1):
        for name in reindeer:
            distances[name] = calc_distance(*reindeer[name], seconds)

        winning_distance = max(distances.values())
        for name in [name for name in reindeer if distances[name] == winning_distance]:
            points[name] += 1
    return max(points.values())


def get_reindeer_stats(reindeer):
    reindeer_stats = {}
    for stat in reindeer:
        name, speed, flight_duration, rest_duration = re.match(
            r"(\w+) .+ (\d+) .+ (\d+) .+ (\d+)", stat
        ).groups()
        reindeer_stats[name] = (int(speed), int(flight_duration), int(rest_duration))
    return reindeer_stats


def calc_distance(speed, flight_duration, rest_duration, time_limit):
    cycle = flight_duration + rest_duration
    cycles = time_limit // cycle
    remaining = time_limit % cycle
    return cycles * speed * flight_duration + min(remaining, flight_duration) * speed


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    TIME_LIMIT = 1000

    inpt = [
        "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
        "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt, Test.TIME_LIMIT), 1120)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt, Test.TIME_LIMIT), 689)
        print("part 2 passed")
