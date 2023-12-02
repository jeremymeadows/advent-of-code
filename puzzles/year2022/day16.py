from puzzles.utils import *
from pprint import pprint

MINUTES = 30


class State:
    def __init__(self, location, release, opened, minutes, pressure):
        self.location = location
        self.release = release
        self.opened = opened
        self.minutes = minutes
        self.pressure = pressure


def part1(inpt):
    scan = get_tunnels(inpt)
    location = "AA"
    valves = {}
    tunnels = Graph()
    for valve, (rate, connections) in scan.items():
        valves[valve] = rate
        for connection in connections:
            tunnels.add(valve, connection)

    max_pressure = 0
    states = [{'location': location, 'release': False, 'opened': [], 'minutes': 0, 'pressure': 0}]
    while len(states) > 0:
        state = states.pop(0)
        pprint(state)

        if state['minutes'] >= MINUTES:
            max_pressure = max(max_pressure, state['pressure'])
            continue

        for valve in state['opened']:
            state['pressure'] += valves[valve]

        if state['release']:
            state['opened'].append(state['location'])

        for option in [connection for connection in scan[state['location']][1]]:
            states.append({'location': option, 'release': False, 'opened': deepcopy(state['opened']), 'minutes': state['minutes'] + 1, 'pressure': state['pressure']})
            if valves[option] > 0:
                states.append({'location': option, 'release': True, 'opened': deepcopy(state['opened']), 'minutes': state['minutes'] + 1, 'pressure': state['pressure']})
    return max_pressure


def part2(inpt):
    return


def get_tunnels(inpt):
    tunnels = {}
    for line in inpt:
        name, flow_rate, tunnel_names = re.match(
            r".*([A-Z]{2}).*=(\d+).*?([A-Z]{2}.*)", line
        ).groups()
        tunnels[name] = (int(flow_rate), list(tunnel_names.split(", ")))
    return tunnels


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB",
        "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
        "Valve CC has flow rate=2; tunnels lead to valves DD, BB",
        "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
        "Valve EE has flow rate=3; tunnels lead to valves FF, DD",
        "Valve FF has flow rate=0; tunnels lead to valves EE, GG",
        "Valve GG has flow rate=0; tunnels lead to valves FF, HH",
        "Valve HH has flow rate=22; tunnel leads to valve GG",
        "Valve II has flow rate=0; tunnels lead to valves AA, JJ",
        "Valve JJ has flow rate=21; tunnel leads to valve II",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 1651)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), None)
        print("part 2 passed")
