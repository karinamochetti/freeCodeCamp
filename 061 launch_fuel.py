def launch_fuel(payload):
    fuel = payload/5
    extra = fuel
    while extra >= 1:
        extra = extra/5
        fuel += extra

    return round(fuel, 1)

print(launch_fuel(50))
print(launch_fuel(500))
print(launch_fuel(243))
print(launch_fuel(11000))
print(launch_fuel(6214))
