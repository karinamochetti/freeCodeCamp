def get_odds(dice, target):
    all_num = 6**dice
    target_chances = []
    target_chances.append([0]*(6*dice+1))
    target_chances.append([0]*(6*dice+1))
    for i in range(1, 7):
        target_chances[1][i] = 1

    for d in range(2, dice+1):
        target_chances.append([0]*(6*dice+1))
        for value in range(0, 6*dice+1):
            for i in range(1, 7):
                if 0 <= value-i <= 6*(d-1):
                    target_chances[d][value] += target_chances[d-1][value-i]

    return f"1 in {round(all_num/target_chances[dice][target])}"

print(get_odds(1, 5))
print(get_odds(2, 4))
print(get_odds(3, 10))
print(get_odds(4, 7))
print(get_odds(5, 26))
print(get_odds(6, 35))
