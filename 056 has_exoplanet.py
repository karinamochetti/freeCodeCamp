def has_exoplanet(readings):
    values = [int(char, 36) for char in readings if char.isalnum()]
    average = sum(values)/len(values)
    under_80 = any(value <= 0.8*average for value in values)
    return under_80

print(has_exoplanet("665544554"))
print(has_exoplanet("FGFFCFFGG"))
print(has_exoplanet("MONOPLONOMONPLNOMPNOMP"))
print(has_exoplanet("FREECODECAMP"))
print(has_exoplanet("9AB98AB9BC98A"))
