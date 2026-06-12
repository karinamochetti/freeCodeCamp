def rook_bishop_attack(rook, bishop):
    if rook[0] == bishop[0] or rook[1] == bishop[1]:
        return "rook"
    if abs(int(rook[1])-int(bishop[1])) == abs(ord(rook[0])-ord(bishop[0])):
        return "bishop"
    return "neither"

print(rook_bishop_attack("A1", "A5"))
print(rook_bishop_attack("C3", "F6"))
print(rook_bishop_attack("D4", "D7"))
print(rook_bishop_attack("B7", "H1"))
print(rook_bishop_attack("B3", "C5"))
print(rook_bishop_attack("G3", "E8"))
