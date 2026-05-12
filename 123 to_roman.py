def to_roman(num):
    roman = ""
    digit = num//1000
    num %= 1000
    roman += (digit%5)*"M"
    
    digit = num//100
    num %= 100
    if digit%5 != 4: roman += (digit//5)*"D" + (digit%5)*"C"
    else: roman += "C" + (digit==4)*"D" + (digit==9)*"M"  

    digit = num//10
    num %= 10
    if digit%5 != 4: roman += (digit//5)*"L" + (digit%5)*"X"
    else: roman += "X" + (digit==4)*"L" + (digit==9)*"C"  

    digit = num
    if digit%5 != 4: roman += (digit//5)*"V" + (digit%5)*"I"
    else: roman += "I" + (digit==4)*"V" + (digit==9)*"X"  

    return roman

print(to_roman(1))
print(to_roman(2))
print(to_roman(3))
print(to_roman(4))
print(to_roman(5))
print(to_roman(6))
print(to_roman(7))
print(to_roman(8))
print(to_roman(9))
print(to_roman(18))
print(to_roman(19))
print(to_roman(1464))
print(to_roman(2025))
print(to_roman(3999))
