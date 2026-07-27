def letter_distance(str1, str2):
    return sum(min(abs(ord(s1) - ord(s2)), 26-abs(ord(s1) - ord(s2))) for s1, s2 in zip(str1, str2))

print(letter_distance("abc", "bcd"))
print(letter_distance("abc", "xyz"))
print(letter_distance("encrypt", "decrypt"))
print(letter_distance("algorithm", "codeblock"))
print(letter_distance("lobster", "penguin"))
print(letter_distance("alligator", "crocodile"))
