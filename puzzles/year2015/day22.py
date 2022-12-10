from puzzles.utils import *


def part1(boss_stats):
    boss_hp, boss_damage = boss_stats
    game_state = {
        "hp": 50,
        "mp": 500,
        "mp_spent": 0,
        "boss_hp": int(boss_hp),
        "boss_damage": int(boss_damage),
        "armor": 0,
        "shield_timer": 0,
        "poison_timer": 0,
        "recharge_timer": 0,
    }
    return combat(game_state)


def part2(boss_stats):
    boss_hp, boss_damage = boss_stats
    game_state = {
        "hp": 50,
        "mp": 500,
        "mp_spent": 0,
        "boss_hp": int(boss_hp),
        "boss_damage": int(boss_damage),
        "armor": 0,
        "shield_timer": 0,
        "poison_timer": 0,
        "recharge_timer": 0,
    }
    return combat(game_state, hard=True)


def combat(state, hard=False) -> int:
    cheapest_victory = float("inf")

    queue = [
        (deepcopy(state), "missile"),
        (deepcopy(state), "drain"),
        (deepcopy(state), "shield"),
        (deepcopy(state), "poison"),
        (deepcopy(state), "recharge"),
    ]

    while len(queue) > 0:
        state, next_spell = queue.pop(0)

        if hard:
            state["hp"] -= 1
            if state["hp"] <= 0:
                continue

        state["armor"] = 0
        if state["shield_timer"] > 0:
            state["armor"] = 7
            state["shield_timer"] -= 1

        if state["poison_timer"] > 0:
            state["boss_hp"] -= 3
            state["poison_timer"] -= 1

        if state["recharge_timer"] > 0:
            state["mp"] += 101
            state["recharge_timer"] -= 1

        if state["boss_hp"] <= 0:
            cheapest_victory = min(cheapest_victory, state["mp_spent"])
            continue

        mana = 0
        match next_spell:
            case "missile":
                state["boss_hp"] -= 4
                mana = 53
            case "drain":
                state["boss_hp"] -= 2
                state["hp"] += 2
                mana = 73
            case "shield":
                state["shield_timer"] = 6
                mana = 113
            case "poison":
                state["poison_timer"] = 6
                mana = 173
            case "recharge":
                state["recharge_timer"] = 5
                mana = 229

        state["mp"] -= mana
        state["mp_spent"] += mana

        if state["mp_spent"] > cheapest_victory:
            continue

        if state["boss_hp"] <= 0:
            cheapest_victory = min(cheapest_victory, state["mp_spent"])
            continue

        state["armor"] = 0
        if state["shield_timer"] > 0:
            state["armor"] = 7
            state["shield_timer"] -= 1

        if state["poison_timer"] > 0:
            state["boss_hp"] -= 3
            state["poison_timer"] -= 1

        if state["recharge_timer"] > 0:
            state["mp"] += 101
            state["recharge_timer"] -= 1

        if state["boss_hp"] <= 0:
            cheapest_victory = min(cheapest_victory, state["mp_spent"])
            continue

        if state["boss_damage"] > state["armor"]:
            state["hp"] -= state["boss_damage"] - state["armor"]
        else:
            state["hp"] -= 1

        if state["hp"] <= 0:
            continue

        if state["mp"] >= 53:
            queue.append((deepcopy(state), "missile"))
        if state["mp"] >= 73:
            queue.append((deepcopy(state), "drain"))
        if state["mp"] >= 113 and state["shield_timer"] <= 1:
            queue.append((deepcopy(state), "shield"))
        if state["mp"] >= 173 and state["poison_timer"] <= 1:
            queue.append((deepcopy(state), "poison"))
        if state["mp"] >= 229 and state["recharge_timer"] <= 1:
            queue.append((deepcopy(state), "recharge"))

    return cheapest_victory


def main():
    inpt = [int(line.split(": ")[-1]) for line in get_input(__file__)]
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [26, 16]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 279)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 372)
        print("part 2 passed")
