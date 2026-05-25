def to_consonant_case(s):
    VOWELS = "AEIOU"
    s = s.replace("-", "_")
    s = s.upper()
    c_list = [c.lower() if c in VOWELS else c for c in s]
    return "".join(c_list)

print(to_consonant_case("helloworld"))
print(to_consonant_case("HELLOWORLD"))
print(to_consonant_case("_hElLO-WOrlD-"))
print(to_consonant_case("_~-generic_~-variable_~-name_~-here-~_"))
