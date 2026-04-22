def capitalize(paragraph):
    should_cap = True
    result = ""
    for c in paragraph:
        if should_cap and c.isalpha():
            c = c.upper()
            should_cap = False
        if c in [".", "?", "!"]:
            should_cap = True
        result += c

    return result

print(capitalize("this is a simple sentence."))
print(capitalize("hello world. how are you?"))
print(capitalize("i did today's coding challenge... it was fun!!"))
print(capitalize("crazy!!!strange???unconventional...sentences."))
print(capitalize("there's a space before this period . why is there a space before that period ?"))
