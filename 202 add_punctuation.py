def add_punctuation(sentences):
    sentences_period = []
    words = sentences.split()
    for word, next_word in zip(words[:-1], words[1:]):
        if next_word[0].isupper():
            sentences_period.append(word+".")
        else:
            sentences_period.append(word)

    return " ".join(sentences_period)+" "+words[-1]+"."

print(add_punctuation("Hello world"))
print(add_punctuation("Hello world It's nice today"))
print(add_punctuation("JavaScript is great Sometimes"))
print(add_punctuation("A b c D e F g h I J k L m n o P Q r S t U v w X Y Z"))
print(add_punctuation("Wait.. For it"))
