def is_valid_number(n, base):
    bases = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    not_valid = [digit for digit in str(n).upper() if digit not in bases[:base]]
    print(not_valid)
    return not len(not_valid)

print(is_valid_number("10101", 2))
print(is_valid_number("10201", 2))
print(is_valid_number("76543210", 8))
print(is_valid_number("9876543210", 8))
print(is_valid_number("9876543210", 10))
print(is_valid_number("ABC", 10))
print(is_valid_number("ABC", 16))
print(is_valid_number("ABC", 36))
print(is_valid_number("Z", 20))
print(is_valid_number("ABC", 16))
print(is_valid_number("4B4BA9", 16))
print(is_valid_number("5G3F8F", 17))
print(is_valid_number("5G3F8F", 10))
print(is_valid_number("abc", 16))
print(is_valid_number("AbC", 16))
print(is_valid_number("z", 36))
