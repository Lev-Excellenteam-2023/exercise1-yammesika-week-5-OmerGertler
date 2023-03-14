# Author: Omer Gertler

from functools import reduce


def get_recipe_price(prices, optionals=None, **ingredients):
    """
    The function calculates and returns the payment of all products.
    Item that appear in the optional list is ignored.
    The cost of 100g product is the value of the product name in the prices dict.
    :param optionals: list of ignored products
    :param ingredients: name and weight of products (example: banana=5)
    :param prices: dict : {key = <product name> : value = <cost for 100g>}
    :return: final payment
    """
    if optionals is None:
        optionals = []
    return reduce(lambda x, y: x + y, [(ingredients[i] * prices[i]/100) for i in ingredients if i not in optionals], 0)


print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))  # 44
print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))  # 54
print(get_recipe_price({}))  # 0
