def find_pawn_moves(position):
    letter, number = position[0], int(position[1])
    moves = [letter+str(number+1)]
    if number == 2:
        moves.append(letter+str(number+2))
    return moves

print(find_pawn_moves("D4"))
print(find_pawn_moves("B2"))
print(find_pawn_moves("A7"))
print(find_pawn_moves("G2"))
print(find_pawn_moves("E3"))
