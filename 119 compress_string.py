def compress_string(sentence):
    words = sentence.split()
    compressed = [words[0]]
    count = 1
    for word in words[1:]:
        if word == compressed[-1]:
            count += 1
        else:
            if count > 1:
                compressed[-1] += f"({count})"
                count = 1
            compressed.append(word)
    if count > 1:
        compressed[-1] += f"({count})"

    return " ".join(compressed)

print(compress_string("yes yes yes please"))
print(compress_string("I have have have apples"))
print(compress_string("one one three and to the the the the"))
print(compress_string("route route route route route route tee tee tee tee tee tee"))
