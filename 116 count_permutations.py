import math
import string

def count_permutations(s):
    n = math.factorial(len(s))
    p = []
    for c in string.ascii_lowercase:
        if s.count(c) > 1:
            p.append(s.count(c))
    for i in p:
        n /= math.factorial(i)
    return n

print(count_permutations("abb"))
print(count_permutations("abc"))
print(count_permutations("racecar"))
print(count_permutations("freecodecamp"))
