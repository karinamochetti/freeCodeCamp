def knight_moves(position):
    col = ord(position[0].upper()) - ord("A") + 1
    row = int(position[1])

    moves = [
        (1, 2), (1, -2), (-1, 2), (-1, -2),
        (2, 1), (-2, 1), (2, -1), (-2, -1)
    ]

    return sum(1 for dc, dr in moves if 1 <= col + dc <= 8 and 1 <= row + dr <= 8)


print(knight_moves("A1"))
print(knight_moves("D4"))
print(knight_moves("G6"))
print(knight_moves("B8"))
print(knight_moves("H3"))