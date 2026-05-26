def count_change(change):
    value = sum(coin/100 for coin in change)
    return f"${value:.2f}"

print(count_change([25, 10, 5, 1]))
print(count_change([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25]) )
print(count_change([100, 25, 100, 1000, 5, 500, 2000, 25]))
print(count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10]))
print(count_change([1]))
print(count_change([25, 25, 25, 25]))
