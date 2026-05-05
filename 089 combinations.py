def combinations(cards):
    if cards < 0 or cards > 52:
        return 0
    
    k = min(cards, 52 - cards)
    
    numerator = 1
    denominator = 1
    for i in range(1, k + 1):
        numerator *= (52 - i + 1)
        denominator *= i

    return numerator // denominator


print(combinations(52))
print(combinations(1))
print(combinations(2))
print(combinations(5))
print(combinations(10))
print(combinations(50))
