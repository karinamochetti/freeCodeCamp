def decompress(s):
    words = s.split()
    for i, word in enumerate(words):
        if all(c.isdigit() for c in words[i]):
            idx = int(word)
            words[i] = words[idx-1]
    return " ".join(words)

print(decompress("practice makes perfect and 3 1 2 3"))
print(decompress("hello 1 1"))
print(decompress("the cat sat on 1 mat 4 which 1 2 3"))
print(decompress("the more you know 1 2 3 realize 3 don't 4"))
print(decompress("lorem ipsum dolor sit per elit donec 4 nostra libero 5 7 ligula 4 gravida at 6 vitae a 6 sodales 7 en 7 16 3 nam 13 dignissim risus 16 13 5 27 2 2 15 23 6 5 2 13 23 15 5 21 4 16 27 1 4 5 10 23 2 6 4 21 4 30 6 30 2 6 16 15 18 23 29 27 4 18 sollicitudin 5 9 5 4 10"))
