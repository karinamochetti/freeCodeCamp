def exact_change(amount):
    ways = [0]*(amount+1)
    ways[0] = 1
    for c in [1, 5, 10, 25]:
        for i in range(amount+1):
            if i-c >= 0:
                ways[i] += ways[i-c]
    return ways[amount]


print(exact_change(3))
print(exact_change(9))
print(exact_change(17))
print(exact_change(39))
print(exact_change(61))
print(exact_change(99))
