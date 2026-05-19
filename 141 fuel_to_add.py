import math

def fuel_to_add(current_gallons, required_liters):
    missing_litters = max(required_liters - current_gallons*3.78541, 0)
    return math.ceil(missing_litters/3.78541)

print(fuel_to_add(0, 1))
print(fuel_to_add(5, 40))
print(fuel_to_add(10, 30))
print(fuel_to_add(896, 20500))
print(fuel_to_add(1000, 50000))
