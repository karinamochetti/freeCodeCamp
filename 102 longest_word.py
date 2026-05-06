def longest_word(sentence):
    for c in ".!?',":
        sentence = sentence.replace(c, "")
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word("The quick red fox"))
print(longest_word("Hello coding challenge."))
print(longest_word("Do Try This At Home."))
print(longest_word("This sentence... has commas, ellipses, and an exclamation point!"))
print(longest_word("A tie? No way!"))
print(longest_word("Wouldn't you like to know."))
