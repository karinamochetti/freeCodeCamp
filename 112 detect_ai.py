def detect_ai(text):
    if text.count("-") > 1:
        return "AI"
    if text.count("(") > 1 and text.count(")") > 1:
        return "AI"
    words = text.split()
    long_words = [word for word in words if len(word) >= 7]
    if len(long_words) >= 3:
        return "AI"
    return "Human"

print(detect_ai("The quick brown fox jumped over the lazy dog."))
print(detect_ai("The hypersonic brown fox - jumped (over) the lazy dog."))
print(detect_ai("Yes - you're right! I made a mistake there - let me try again."))
print(detect_ai("The extraordinary students were studying vivaciously."))
print(detect_ai("The (excited) student was (coding) in the library."))
