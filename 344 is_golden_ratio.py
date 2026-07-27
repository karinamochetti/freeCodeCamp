def is_golden_ratio(a, b):
    return abs(a/b-1.618) <= 0.01 or abs(b/a-1.618) <= 0.01

print(is_golden_ratio(21, 34))
print(is_golden_ratio(15, 20))
print(is_golden_ratio(8, 13))
print(is_golden_ratio(10, 16))
print(is_golden_ratio(1618, 1000))
print(is_golden_ratio(88, 55))
