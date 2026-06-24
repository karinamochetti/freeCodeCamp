def get_unique_climbs(steps):
    if steps <= 2:
        return steps

    prev, current = 1, 2
    for _ in range(3, steps + 1):
        prev, current = current, prev + current

    return current

print(get_unique_climbs(4))
print(get_unique_climbs(5))
print(get_unique_climbs(10))
print(get_unique_climbs(18))
print(get_unique_climbs(29))
print(get_unique_climbs(50))
