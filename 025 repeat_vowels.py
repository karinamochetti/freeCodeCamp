def repeat_vowels(string):
    VOWELS = "aeiou"
    copy = 0
    result = ""
    for c in string:
        result += c
        if c.lower() in VOWELS:
            result += c.lower()*copy
            copy +=1
    return result

print(repeat_vowels("hello world"))
print(repeat_vowels("freeCodeCamp"))
print(repeat_vowels("AEIOU"))
print(repeat_vowels("I like eating ice cream in Iceland"))
