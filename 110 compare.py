def compare(word, guess):
    word = list(word)
    n = len(word)
    values = ["0"]*n
    for i in range(n):
        if guess[i] == word[i]:
            values[i] = "2"
            word[i] = None
    for i in range(n):
        if values[i] == "0" and guess[i] in word:
            values[i] = "1"
            word[word.index(guess[i])] = None

    return "".join(values)

print(compare("APPLE", "POPPA"))
print(compare("REACT", "TRACE"))
print(compare("DEBUGS", "PYTHON"))
print(compare("JAVASCRIPT", "TYPESCRIPT"))
print(compare("ORANGE", "ROUNDS"))
print(compare("WIRELESS", "ETHERNET"))
