def vowel_case(s):
    VOWEL = "aeiou"
    s = s.lower()
    result = [c.upper() if c in VOWEL else c for c in s]
    return "".join(result)

print(vowel_case("vowelcase"))
print(vowel_case("coding is fun"))
print(vowel_case("HELLO, world!"))
print(vowel_case("git cherry-pick"))
print(vowel_case("HEAD~1"))
