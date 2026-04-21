def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)

print(reverse_sentence("world hello"))
print(reverse_sentence("push commit git"))
print(reverse_sentence("npm  install   apt    sudo"))
print(reverse_sentence("import    default   function  export"))
