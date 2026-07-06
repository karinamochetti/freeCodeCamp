def kaprekar(n):
    i = 0
    while n != 6174:
        digits = "".join(sorted(str(n)))
        num1 = int(digits)
        num2 = int(digits[::-1])
        n = num2-num1 if num2 > num1 else num1-num2
        i += 1
    return i

print(kaprekar(1234))
print(kaprekar(2025))
print(kaprekar(7173))
print(kaprekar(3164))
print(kaprekar(8082))
