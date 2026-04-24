def to_decimal(binary):
    num = 0
    i = 0
    for b in binary[::-1]:
        num += int(b)*(2**i)
        i += 1
    return num

print(to_decimal("101"))
print(to_decimal("1010"))
print(to_decimal("10010"))
print(to_decimal("1010101"))
