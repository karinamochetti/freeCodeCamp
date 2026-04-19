def is_pangram(sentence, letters):
    sentence = [char.lower() for char in sentence if char.isalpha()]
    letters = set(letters)
    sentence = set(sentence)
    return (letters.issubset(sentence) and sentence.issubset(letters))

print(is_pangram("hello", "helo"))
print(is_pangram("hello", "hel"))
print(is_pangram("hello", "helow"))
print(is_pangram("hello world", "helowrd"))
print(is_pangram("Hello World!", "helowrd"))
print(is_pangram("hello World!", "heliowrd"))
print(is_pangram("freeCodeCamp", "frcdmp"))
print(is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz"))
