def rook_attack(rook1, rook2):
    return rook1[0] == rook2[0] or rook1[1] == rook2[1]

print(rook_attack("A1", "A8"))
print(rook_attack("B4", "F4"))
print(rook_attack("E3", "D4"))
print(rook_attack("H7", "F6"))