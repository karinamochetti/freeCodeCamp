import re

def pig_latin(s):
    words = s.split()
    pig_words = []
    
    consonant_pattern = re.compile(r'^([^aeiouAEIOU]+)')

    for word in words:
        if word[0].lower() in "aeiou":
            pig_words.append(f"{word}way")
            continue

        match = consonant_pattern.match(word)
        if match:
            consonants = match.group(1)
            remainder = word[len(consonants):]
            
            if word.istitle():
                new_word = f"{remainder.capitalize()}{consonants.lower()}ay"
            else:
                new_word = f"{remainder}{consonants.lower()}ay"
                
            pig_words.append(new_word)
        else:
            pig_words.append(word)

    return " ".join(pig_words)

print(pig_latin("universe"))
print(pig_latin("hello"))
print(pig_latin("hello universe"))
print(pig_latin("Hello universe"))
print(pig_latin("Pig Latin is fun"))
print(pig_latin("The quick brown fox jumped over the lazy dog"))
