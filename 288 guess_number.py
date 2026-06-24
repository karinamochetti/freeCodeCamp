def guess_number(secret, guess):
    if guess > secret: return "lower"
    if guess < secret: return "higher"
    return "you got it!"

print(guess_number(50, 30))
print(guess_number(85, 99))
print(guess_number(2026, 2026))
print(guess_number(92904, 11283))
print(guess_number(230495, 423920))
print(guess_number(120349, 120349))
