def jbelmu(text):
    words = text.split(" ")
    new_text = ""
    for word in words:
        if len(word) > 1:
            new_text += word[0] + "".join(sorted(word[1:-1])) + word[-1] + " "
        else:
            new_text += word + " "
    return new_text[:-1]

print(jbelmu("hello world"))
print(jbelmu("i love jumbled text"))
print(jbelmu("freecodecamp is my favorite place to learn to code"))
print(jbelmu("the quick brown fox jumps over the lazy dog"))
