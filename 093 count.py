def count(s):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    v_count = sum(1 for char in s if char.lower() in vowels)
    c_count = sum(1 for char in s if char.lower() in consonants)
    return [v_count, c_count]

print(count("Hello World"))
print(count("JavaScript"))
print(count("Python"))
print(count("freeCodeCamp"))
print(count("Hello, World!"))
print(count("The quick brown fox jumps over the lazy dog."))
