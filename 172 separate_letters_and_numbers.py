def separate_letters_and_numbers(s):
    arr = [s[0]]
    for prev, c in zip(s, s[1:]):
        if c.isdigit() and not prev.isdigit():
            arr.append("-")
        if not c.isdigit() and prev.isdigit():
            arr.append("-")
        arr.append(c)
    return "".join(arr)

print(separate_letters_and_numbers("ABC123"))
print(separate_letters_and_numbers("Route66"))
print(separate_letters_and_numbers("H3LL0W0RLD"))
print(separate_letters_and_numbers("a1b2c3d4"))
