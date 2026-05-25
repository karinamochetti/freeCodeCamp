def is_valid_hex(s):
    valid_hex = "0123456789abcdef"
    if len(s) != 4 and len(s) != 7:
        return False
    if s[0] != "#":
        return False
    s = s.lower()
    if any(c for c in s[1:] if c not in valid_hex):
        return False
    return True

print(is_valid_hex("#123"))
print(is_valid_hex("#123abc"))
print(is_valid_hex("#ABCDEF"))
print(is_valid_hex("#0a1B2c"))
print(is_valid_hex("#12G"))
print(is_valid_hex("#1234567"))
print(is_valid_hex("#12 3"))
print(is_valid_hex("fff"))
