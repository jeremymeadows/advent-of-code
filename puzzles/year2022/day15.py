from puzzles.utils import *

ROW = 2000000
FREQUENCY = 4000000

from pprint import pprint


def part1(sensor_positions, row=ROW):
    sensors = get_sensors(sensor_positions)
    cleared = [
        location
        for location in get_clear_locations(sensors, row)
        if location not in [beacon for _, beacon in sensors]
    ]
    return len(cleared)


def part2(sensor_positions, rows=ROW):
    sensors = get_sensors(sensor_positions)
    perimiters = set()
    for ndx, (s, b) in enumerate(sensors):
        print(ndx)
        perims = get_sensor_perimiter(s, b)
        for p in perims:
            if p not in perimiters:
                perimiters.add(p)
            else:
                print("found")
                print(p)
    perimiters = [get_sensor_perimiter(*sensor) for sensor in sensors]
    pprint(perimiters)
    unchecked = set.intersection(*perimiters)
    print(unchecked)
    # with Pool() as pool:
    #     results = pool.starmap_async(
    #         get_clear_locations,
    #         [(sensors, i) for i in range(rows)],
    #     )
    #     for a, b in windows(sorted(list(results.get())), 2):
    #         if a.rectilinear_distance(b) > 1:
    #             return (a.x + 1) * FREQUENCY + row
    #         # for a, b in windows(sorted(list()))
    #         # res = r.get()
    #         print(r)
        # for i, result in enumerate(results):
        #     print(f"{i}: {len(result)}")
    for row in range(rows * 2):
        print(row)
        for a, b in windows(sorted(list(get_clear_locations(sensors, row))), 2):
            if a.rectilinear_distance(b) > 1:
                return (a.x + 1) * FREQUENCY + row


def get_sensors(sensor_positions) -> list[tuple[Point, Point]]:
    return [
        [
            (Point(int(x), int(y)), Point(int(a), int(b)))
            for x, y, a, b in [
                re.findall(r"-?\d+", row)
            ]
        ][0]
        for row in sensor_positions
    ]

def intervals(sensors, y):
    for sx, sy, bx, by in sensors:
        dx = abs(sx - bx) + abs(sy - by) - abs(sy - y)
        if dx >= 0:
            yield sx - dx, sx + dx

def coverage(sensors, y):
    l, r = zip(*intervals(sensors, y))
    beacons = len(set(bx for _, _, bx, by in sensors if by == y))
    return max(r) + 1 - min(l) - beacons


def get_clear_locations(sensors, row) -> set[Point]:
    clear_locations = set()
    for sensor, beacon in sensors:
        dist = sensor.rectilinear_distance(beacon)
        for i in range(sensor.x, sensor.x + dist):
            if (p := Point(i, row)).rectilinear_distance(sensor) <= dist:
                clear_locations.add(p)
            else:
                break

        for i in range(sensor.x - 1, sensor.x - dist, -1):
            if (p := Point(i, row)).rectilinear_distance(sensor) <= dist:
                clear_locations.add(p)
            else:
                break
    return clear_locations


def get_sensor_area(sensor, beacon) -> set[Point]:
    dist = sensor.rectilinear_distance(beacon) + 1
    area = set()
    for x in range(dist):
        for y in range(dist - x):
            area.add(Point(sensor.x + x, sensor.y + y))
            area.add(Point(sensor.x + x, sensor.y - y))
            area.add(Point(sensor.x - x, sensor.y + y))
            area.add(Point(sensor.x - x, sensor.y - y))
    return area


def get_sensor_perimiter(sensor, beacon) -> set[Point]:
    dist = sensor.rectilinear_distance(beacon) + 1
    perimiter = set()
    for i in range(dist):
        perimiter.add(Point(sensor.x + dist - i, sensor.y + i))
        perimiter.add(Point(sensor.x + dist - i, sensor.y - i))
        perimiter.add(Point(sensor.x - dist + i, sensor.y + i))
        perimiter.add(Point(sensor.x - dist + i, sensor.y - i))
    return perimiter


def main():
    inpt = get_input(__file__)
    # print(f"part 1: {part1(inpt)}")
    # exit()
    p2 = part2(inpt)
    with open("p2.txt", "w") as f:
        f.write(str(p2))
    print(f"part 2: {p2}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    ROW = 10

    inpt = [
        "Sensor at x=2, y=18: closest beacon is at x=-2, y=15",
        "Sensor at x=9, y=16: closest beacon is at x=10, y=16",
        "Sensor at x=13, y=2: closest beacon is at x=15, y=3",
        "Sensor at x=12, y=14: closest beacon is at x=10, y=16",
        "Sensor at x=10, y=20: closest beacon is at x=10, y=16",
        "Sensor at x=14, y=17: closest beacon is at x=10, y=16",
        "Sensor at x=8, y=7: closest beacon is at x=2, y=10",
        "Sensor at x=2, y=0: closest beacon is at x=2, y=10",
        "Sensor at x=0, y=11: closest beacon is at x=2, y=10",
        "Sensor at x=20, y=14: closest beacon is at x=25, y=17",
        "Sensor at x=17, y=20: closest beacon is at x=21, y=22",
        "Sensor at x=16, y=7: closest beacon is at x=15, y=3",
        "Sensor at x=14, y=3: closest beacon is at x=15, y=3",
        "Sensor at x=20, y=1: closest beacon is at x=15, y=3",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt, Test.ROW), 26)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt, Test.ROW), 56000011)
        print("part 2 passed")
