def is_valid_message(message, validation):
    words = message.lower().split()
    validation = validation.lower()

    if len(words) != len(validation):
        return False

    return all(word[0] == letter for word, letter in zip(words, validation))

print(is_valid_message("hello world", "hw"))
print(is_valid_message("ALL CAPITAL LETTERS", "acl"))
print(is_valid_message("Coding challenge are boring.", "cca"))
print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD"))
print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT"))
