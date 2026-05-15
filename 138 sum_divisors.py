def sum_divisors(n):
    return sum(i for i in range(1, n+1) if n%i == 0)

print(sum_divisors(6))
print(sum_divisors(13))
print(sum_divisors(28))
print(sum_divisors(84))
print(sum_divisors(549))
print(sum_divisors(9348))
