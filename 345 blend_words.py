def blend_words(word1, word2):
    n1 = len(word1)
    n2 = len(word2)
    return word1[:n1//2] + word2[n2//2:]

print(blend_words("turtle", "toucan"))
print(blend_words("chipmunk", "flamingo") )
print(blend_words("falcon", "pelican"))
print(blend_words("hyena", "iguana"))
print(blend_words("scorpion", "gorilla"))
print(blend_words("platypus", "wolverine"))
