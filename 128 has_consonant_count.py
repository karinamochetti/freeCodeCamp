def has_consonant_count(text, target):
    consonants = "bcdfghjklmnpqrstvwxyz"
    num = sum(1 for c in text.lower() if c in consonants)
    if num == target: 
        return True
    return False

print(has_consonant_count("helloworld", 7))
print(has_consonant_count("eieio", 5))
print(has_consonant_count("freeCodeCamp Rocks!", 11))
print(has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24))
print(has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23))
