def sum_letters(s):
    s = s.lower()
    return sum(ord(c)-ord('a')+1 for c in s if c.isalpha())

print(sum_letters("Hello"))
print(sum_letters("freeCodeCamp"))
print(sum_letters("The quick brown fox jumps over the lazy dog."))
print(sum_letters("</404>"))
