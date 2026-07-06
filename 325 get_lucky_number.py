def get_lucky_number(name):
    VOWELS = "aeiou"
    first, last = name.split()
    first = first.lower()
    last = last.lower()

    first_vowel = sum(1 for c in first if c in VOWELS)
    first_len = len(first)
    first_conson = first_len - first_vowel

    last_vowel = sum(1 for c in last if c in VOWELS)
    last_len = len(last)
    last_conson = last_len - last_vowel

    min_vowel = min(first_vowel, last_vowel)
    max_vowel = max(first_vowel, last_vowel)

    min_conson = min(first_conson, last_conson)
    max_conson = max(first_conson, last_conson)

    min_len = min(first_len, last_len)
    max_len = max(first_len, last_len)

    lucky_num = (max_vowel*max_conson*max_len) - (min_vowel*min_conson*min_len)

    return lucky_num if lucky_num != 0 else 13


print(get_lucky_number("John Doe"))
print(get_lucky_number("Olivia Lewis"))
print(get_lucky_number("James Wilson"))
print(get_lucky_number("Elizabeth Hernandez"))
print(get_lucky_number("Mike Walker"))
print(get_lucky_number("Chloe Perez"))
