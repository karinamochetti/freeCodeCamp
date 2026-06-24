def get_number_words(n):
    NUM_NAMES = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "fourty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }
    if n in NUM_NAMES:
        return f"{NUM_NAMES[n]}"
    else:
        return f"{NUM_NAMES[(n//10)*10]}-{NUM_NAMES[n%10]}"

print(get_number_words(0))
print(get_number_words(10))
print(get_number_words(19))
print(get_number_words(30))
print(get_number_words(53))
print(get_number_words(7))
print(get_number_words(12))
print(get_number_words(60))
print(get_number_words(67))
print(get_number_words(98))
