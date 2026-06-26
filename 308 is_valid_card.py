def is_valid_card(number):
    digits = list(map(int, number))
    for i in range(len(digits)-2, -1, -2):
        doubled = (digits[i]*2)
        digits[i] = doubled if doubled <= 9 else doubled - 9
    return sum(digits)%10==0

print(is_valid_card("4532015112830366"))
print(is_valid_card("5425233430109903"))
print(is_valid_card("371449635398431"))
print(is_valid_card("6011111111111117"))
print(is_valid_card("4532015112830367"))
print(is_valid_card("1234567890123456"))
print(is_valid_card("4532015112830368"))

