def get_longest_word(sentence):
    sentence = sentence.lower().replace(".", "")
    words = sentence.split()
    largest = ""
    for word in words:
        if len(word) > len(largest):
            largest = word
    return largest

print(get_longest_word("coding is fun"))
print(get_longest_word("Coding challenges are fun and educational."))
print(get_longest_word("This sentence has multiple long words."))
