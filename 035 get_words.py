def get_words(paragraph):
    # remove non alpha
    words = paragraph.lower().split()
    dictionary = {}
    for word in words:
        clean_word = "".join(filter(str.isalnum, word))
        dictionary[clean_word] = dictionary.get(clean_word, 0) + 1
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return list(sorted_dict.keys())[:3]
    

print(get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding"))
print(get_words("I like coding. I like testing. I love debugging!"))
print(get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!"))
