import string

def count_characters(sentence):
    result = []
    sentence = sentence.lower()
    for c in string.ascii_lowercase:
        n = sentence.count(c)
        if n != 0:
            result.append(c + " " + str(n))
    return result

print(count_characters("hello world"))
print(count_characters("I love coding challenges!"))
print(count_characters("// TODO: Complete this challenge ASAP!"))
