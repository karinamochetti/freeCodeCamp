def is_in_crossword(char):
    rows = ["01000001", "01101111", "01000100", "01100101", "01010010", "01010100", "01101000", "10101110"]
    cols = {"00000001", "11111110", "01010011", "00001100", "01000011", "01110101", "01001001", "11010000"}

    bin_char = format(ord(char), '08b')
    for row in rows:
        if bin_char in row or bin_char in row[::-1]:
            return True
    for col in cols:
        if bin_char in col or bin_char in col[::-1]:
            return True
    return False

print(is_in_crossword("I"))
print(is_in_crossword("D"))
print(is_in_crossword("0"))
print(is_in_crossword("u"))
print(is_in_crossword("Y"))
print(is_in_crossword("p"))
print(is_in_crossword("1"))
print(is_in_crossword("Q"))
