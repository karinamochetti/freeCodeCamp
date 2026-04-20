def build_acronym(string):
    ignore_words = ["a", "for", "an", "and", "by", "of"]
    string = string.lower()
    words = string.split(" ")
    acronym = [word[0].upper() for i, word in enumerate(words) if word not in ignore_words or i == 0]
    return "".join(acronym)

print(build_acronym("Search Engine Optimization"))
print(build_acronym("Frequently Asked Questions"))
print(build_acronym("National Aeronautics and Space Administration"))
print(build_acronym("Federal Bureau of Investigation"))
print(build_acronym("For your information"))
print(build_acronym("By the way"))
print(build_acronym("An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily"))


