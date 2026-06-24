def compress(s):
    seen_words = {}
    words = s.split()
    for i, word in enumerate(words):
        if word in seen_words:
            words[i] = seen_words[word]
        else:
            seen_words[word] = str(i+1)
    return " ".join(words)

print(compress("practice makes perfect and perfect practice makes perfect"))
print(compress("hello hello hello"))
print(compress("the cat sat on the mat on which the cat sat"))
print(compress("the more you know the more you realize you don't know"))
print(compress("lorem ipsum dolor sit per elit donec sit nostra libero per donec ligula sit gravida at elit vitae a elit sodales donec en donec at dolor nam ligula dignissim risus at ligula per nam ipsum ipsum gravida en elit per ipsum ligula en gravida per sodales sit at nam lorem sit per libero en ipsum elit sit sodales sit risus elit risus ipsum elit at gravida vitae en dignissim nam sit vitae sollicitudin per nostra per sit libero"))
