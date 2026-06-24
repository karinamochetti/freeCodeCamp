def get_word_score(word):
    return sum(ord(c)-ord('A')+1 for c in word.upper())

print(get_word_score("hi"))
print(get_word_score("hello") )
print(get_word_score("hippopotamus"))
print(get_word_score("freeCodeCamp"))
