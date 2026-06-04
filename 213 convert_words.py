def convert_words(s):
    lenghts = [str(len(word)) for word in s.split()]
    return " ".join(lenghts)

print(convert_words("hello world"))
print(convert_words("Thanks and happy coding"))
print(convert_words("The quick brown fox jumps over the lazy dog"))
print(convert_words("Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula vehicula iaculis orci vel semper nisl"))

