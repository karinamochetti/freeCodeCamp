def has_no_repeats(s):
    for c1, c2 in zip(s[:-1], s[1:]):
        if c1 == c2:
            return False
    return True

print(has_no_repeats("hi world"))
print(has_no_repeats("hello world"))
print(has_no_repeats("abcdefghijklmnopqrstuvwxyz"))
print(has_no_repeats("freeCodeCamp"))
print(has_no_repeats("The quick brown fox jumped over the lazy dog."))
print(has_no_repeats("Mississippi"))
