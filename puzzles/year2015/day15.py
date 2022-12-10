from puzzles.utils import *


def part1(ingredient_list):
    ingredients = get_ingredients(ingredient_list)

    best_cookie_score = 0
    for proportions in get_proportions(len(ingredients)):
        score = get_score(ingredients, proportions)
        best_cookie_score = max(best_cookie_score, score)
    return best_cookie_score


def part2(ingredient_list):
    ingredients = get_ingredients(ingredient_list)

    best_low_cal_cookie_score = 0
    for proportions in get_proportions(len(ingredients)):
        score = get_score(ingredients, proportions)
        calories = sum(
            ingredients[name]["calories"] * proportions[i]
            for i, name in enumerate(ingredients)
        )
        if calories == 500:
            best_low_cal_cookie_score = max(best_low_cal_cookie_score, score)
    return best_low_cal_cookie_score


def get_ingredients(ingredient_list):
    ingredients = {}
    for ingredient in ingredient_list:
        name, props = ingredient.split(": ")
        ingredients[name] = {
            prop: int(val) for prop, val in [prop.split() for prop in props.split(", ")]
        }
    return ingredients


def get_proportions(ingredients_count: int, total_amount: int = 100):
    if ingredients_count == 1:
        yield [total_amount]
    else:
        for i in range(total_amount + 1):
            for proportion in get_proportions(ingredients_count - 1, total_amount - i):
                yield [i] + proportion


def get_score(ingredients, proportions):
    return product(
        [
            max(
                0,
                sum(
                    ingredients[name][prop] * proportions[i]
                    for i, name in enumerate(ingredients)
                ),
            )
            for prop in ["capacity", "durability", "flavor", "texture"]
        ]
    )


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
        "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 62842880)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 57600000)
        print("part 2 passed")
