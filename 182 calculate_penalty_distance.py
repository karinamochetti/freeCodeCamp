def calculate_penalty_distance(rounds):
    return sum((5-target)*150 for target in rounds)

print(calculate_penalty_distance([4, 4]))
print(calculate_penalty_distance([5, 5]))
print(calculate_penalty_distance([4, 5, 3, 5]))
print(calculate_penalty_distance([5, 4, 5, 5]))
print(calculate_penalty_distance([4, 3, 0, 3]))
