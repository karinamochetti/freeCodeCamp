def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    l = 1
    r = n
    i = (l+r)//2
    while i > l and i < r:
        if i*i == n: return True
        if i*i < n: l = i
        if i*i > n: r = i
        i = (l+r)//2
    return False
    
print(is_perfect_square(9))
print(is_perfect_square(49))
print(is_perfect_square(1))
print(is_perfect_square(2))
print(is_perfect_square(99))
print(is_perfect_square(-9))
print(is_perfect_square(0))
print(is_perfect_square(25281))
