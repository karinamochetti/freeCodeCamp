def fix_numerals(s):
    VALUES = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }

    num = sum(v*s.count(VALUES[v]) for v in VALUES)

    check = (num//1000)%10
    if check <= 3:
        rom = "M"*check
    else:
        rom = ""

    for i in range(2, -1, -1):
        check = (num//10**i)%10
        if check <= 3:
            rom += VALUES[10**i]*check
        if check == 4:
            rom += VALUES[10**i]+VALUES[5*10**i]
        if 5 <= check < 9:
            rom += VALUES[5*10**i]+VALUES[10**i]*(check-5)
        if check == 9:
            rom += VALUES[10**i]+VALUES[10**(i+1)]

    return rom

print(fix_numerals("XIIIII"));
print(fix_numerals("IIIILX"));
print(fix_numerals("XXVVVIIIII"));
print(fix_numerals("MDCCLXXXXVIIII"));
print(fix_numerals("IIIIVVVVXXXXLLLLCCDD"));
print(fix_numerals("ILCDMIVDIIXLCVCXDL"));
