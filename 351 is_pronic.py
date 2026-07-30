def is_pronic(n):
    return any(i for i in range(n+1) if i*(i+1) == n) or n==0

print(is_pronic(6))
print(is_pronic(15))
print(is_pronic(12))
print(is_pronic(132))
print(is_pronic(80))
print(is_pronic(0))
