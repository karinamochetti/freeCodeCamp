def digits_or_letters(s):
    digits = 0
    letters = 0
    for char in s:
        if char.isdigit(): digits += 1
        if char.isalpha(): letters += 1

    if digits > letters: return "digits"
    if digits < letters: return "letters"
    if digits == letters: return "tie"

print(digits_or_letters("abc123"))
print(digits_or_letters("a1b2c3d"))
print(digits_or_letters("1a2b3c4"))
print(digits_or_letters("abc123!@#DEF"))
print(digits_or_letters("H3110 W0R1D"))
print(digits_or_letters("P455W0RD"))
