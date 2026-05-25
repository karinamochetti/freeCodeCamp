def get_bingo_letter(n):
    bingo_letter = [
        (61, "O"),
        (46, "G"),
        (31, "N"),
        (16, "I"),
        (1, "B"),
    ]

    for value, letter in bingo_letter:
        if n >= value:
            return letter

print(get_bingo_letter(75))
print(get_bingo_letter(54))
print(get_bingo_letter(25))
print(get_bingo_letter(38))
print(get_bingo_letter(11))
