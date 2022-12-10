from puzzles.utils import *


def part1(flight_distances):
    routes = find_routes(flight_distances)

    min_dist = float("inf")
    for route in permutations(routes.keys()):
        route_dist = sum([routes[src][dst] for src, dst in windows(route, 2)])
        min_dist = min(min_dist, route_dist)
    return min_dist


def part2(flight_distances):
    routes = find_routes(flight_distances)

    max_dist = float("-inf")
    for route in permutations(routes.keys()):
        route_dist = sum([routes[src][dst] for src, dst in windows(route, 2)])
        max_dist = max(max_dist, route_dist)
    return max_dist


def find_routes(flight_distances) -> dict[str, dict[str, int]]:
    routes = {}
    for flight in flight_distances:
        src, dst, dist = re.match(r"(\w+) to (\w+) = (\d+)", flight).groups()

        if src not in routes:
            routes[src] = {}
        if dst not in routes:
            routes[dst] = {}

        routes[src][dst] = int(dist)
        routes[dst][src] = int(dist)
    return routes


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
        self.assertEqual(
            part1(
                [
                    "London to Dublin = 464",
                    "London to Belfast = 518",
                    "Dublin to Belfast = 141",
                ]
            ),
            605,
        )
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(
            part2(
                [
                    "London to Dublin = 464",
                    "London to Belfast = 518",
                    "Dublin to Belfast = 141",
                ]
            ),
            982,
        )
        print("part 2 passed")
