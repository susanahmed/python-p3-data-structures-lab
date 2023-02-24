spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):

    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food ["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        name = item["name"]
        country = item["cuisine"]
        heat = item["heat_level"] * "🌶"

        print(f"{name} ({country}) | Heat Level: {heat}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
        for food in spicy_foods:
            if food ["cuisine"] == cuisine:
                return food

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    sum = 0
    for food in spicy_foods:
        heat = food["heat_level"]
        sum += heat

    average = sum / len(spicy_foods)
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
