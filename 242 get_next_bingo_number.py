def get_next_bingo_number(n):
    BINGO = "BINGO"
    
    letter = n[0]
    num = int(n[1:])

    number = 1 if num == 75 else num + 1
    
    if num % 15 == 0:
        index = (BINGO.index(letter) + 1) % len(BINGO)
        letter = BINGO[index]

    return f"{letter}{number}"

print(get_next_bingo_number("B10"))
print(get_next_bingo_number("N33"))
print(get_next_bingo_number("I30"))
print(get_next_bingo_number("G60"))
print(get_next_bingo_number("O75"))
