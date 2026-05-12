def convert_to_kgs(lbs):
    kgs = round(0.453592*lbs, 2)
    pounds = "pounds"
    kilograms = "kilograms"
    if lbs == 1: pounds = "pound"
    if kgs == 1: kilograms = "kilogram"
    return f"{lbs} {pounds} equals {kgs:.2f} {kilograms}."

print(convert_to_kgs(1))
print(convert_to_kgs(0))
print(convert_to_kgs(100))
print(convert_to_kgs(2.5))
print(convert_to_kgs(2.20462))
