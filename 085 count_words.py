def count_words(sentence):
    words = sentence.split()
    return len(words)

print(count_words("Hello world"))
print(count_words("The quick brown fox jumps over the lazy dog."))
print(count_words("I like coding challenges!"))
print(count_words("Complete the challenge in JavaScript and Python."))
print(count_words("The missing semi-colon crashed the entire internet."))
