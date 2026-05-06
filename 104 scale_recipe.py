def scale_recipe(ingredients, scale):
    result = []
    for ingredient in ingredients:
        parts = ingredient.split(None, 1)
        value = float(parts[0])*scale
        result.append(f"{value:g} {parts[1]}")
    return result

print(scale_recipe(["2 C Flour", "1.5 T Sugar"], 2))
print(scale_recipe(["4 T Flour", "1 C Milk", "2 T Oil"], 1.5))
print(scale_recipe(["3 C Milk", "2 C Oats"], 0.5))
print(scale_recipe(["2 C All-purpose Flour", "1 t Baking Soda", "1 t Salt", "1 C Butter", "0.5 C Sugar", "0.5 C Brown Sugar", "1 t Vanilla Extract", "2 C Chocolate Chips"], 2.5))