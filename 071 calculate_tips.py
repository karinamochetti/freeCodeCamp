def calculate_tips(meal_price, custom_tip):
    price = float(meal_price.strip("$"))
    tip = int(custom_tip.strip("%"))

    tip15 = 15*price/100
    tip20 = 20*price/100
    tipCT = tip*price/100
    return [f"${tip15:.2f}", f"${tip20:.2f}", f"${tipCT:.2f}"]

print(calculate_tips("$10.00", "25%"))
print(calculate_tips("$89.67", "26%"))
print(calculate_tips("$19.85", "9%"))
