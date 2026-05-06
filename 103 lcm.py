def lcm(a, b):
    if a > b: a, b = b, a
    for i in range(b, a*b+1, b):
        if i%a==0:
            return i

print(lcm(4, 6))
print(lcm(9, 6))
print(lcm(10, 100))
print(lcm(13, 17))
print(lcm(45, 70))
