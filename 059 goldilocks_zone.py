import math

def goldilocks_zone(mass):
    luminosity = mass**3.5
    start_zone = 0.95*(math.sqrt(luminosity))
    end_zone = 1.37*(math.sqrt(luminosity))

    return [round(start_zone, 2), round(end_zone, 2)]


print(goldilocks_zone(1))
print(goldilocks_zone(0.5))
print(goldilocks_zone(6))
print(goldilocks_zone(3.7))
print(goldilocks_zone(20))
