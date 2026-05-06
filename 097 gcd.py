def gcd(x, y):
    if x > y: x, y = y, x
    div = y%x
    while div != 0:
        y = x
        x = div
        div = y%x
    return x

print(gcd(4, 6))
print(gcd(20, 15))
print(gcd(13, 17))
print(gcd(654, 456))
print(gcd(3456, 4320))
