def hex_to_decimal(hex):
    decimal = 0
    i = 0
    for c in hex[::-1]:
        if c.isdigit(): decimal += int(c)*16**i
        else: decimal += (ord(c)-ord("A")+10)*(16**i)
        i += 1
    return decimal
#    return int(hex, 16)

print(hex_to_decimal("A"))
print(hex_to_decimal("15"))
print(hex_to_decimal("2E"))
print(hex_to_decimal("FF"))
print(hex_to_decimal("A3F"))
