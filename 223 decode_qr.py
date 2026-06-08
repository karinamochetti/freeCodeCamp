def decode_qr(qr_code):

    def validQR(qr_code):
        top_left = qr_code[0][:2] + qr_code[1][:2]
        top_right = qr_code[0][-2:] + qr_code[1][-2:]
        bottom_left = qr_code[-2][:2] + qr_code[-1][:2]
        return top_left == "1111" and top_right == "1111" and bottom_left == "1111"

    while not validQR(qr_code):
        qr_code = ["".join(list(row)) for row in zip(*qr_code[::-1])]

    code = qr_code[0][2:-2] + qr_code[1][2:-2] + qr_code[2] + qr_code[3] + qr_code[4][2:] + qr_code[5][2:]
    return code

print(decode_qr(["110011", "110011", "000000", "000000", "110000", "110001"]))
print(decode_qr(["100011", "000011", "000000", "000000", "110011", "110011"]))
print(decode_qr(["110011", "111111", "010000", "110000", "110011", "110100"]))
print(decode_qr(["011011", "101011", "101000", "100010", "110011", "111011"]))
print(decode_qr(["111100", "110001", "100011", "001101", "110011", "110011"]))
