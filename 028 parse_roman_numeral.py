def parse_roman_numeral(numeral):
    roman_num = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    value = 0
    max_num = 0
    for num in reversed(numeral):
        if roman_num[num] < max_num:
            value -= roman_num[num]
        else:
            value += roman_num[num]
            max_num = roman_num[num]
    return value


print(parse_roman_numeral("III"))
print(parse_roman_numeral("IV"))
print(parse_roman_numeral("XXVI"))
print(parse_roman_numeral("XCIX"))
print(parse_roman_numeral("CDLX"))
print(parse_roman_numeral("DIV"))
print(parse_roman_numeral("MMXXV"))
