import math

def get_combinations(n):
    return math.factorial(2*n)/(math.factorial(n+1)*math.factorial(n))

print(get_combinations(2))
print(get_combinations(3))
print(get_combinations(5))
print(get_combinations(8))
print(get_combinations(13))
