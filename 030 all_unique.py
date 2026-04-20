def all_unique(s):
    return len(list(s)) == len(set(s))

print(all_unique("abc"))
print(all_unique("aA"))
print(all_unique("QwErTy123!@"))
print(all_unique("~!@#$%^&*()_+"))
print(all_unique("hello"))
print(all_unique("freeCodeCamp"))
print(all_unique("!@#*$%^&*()aA"))
