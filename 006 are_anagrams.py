def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").upper()
    str2 = str2.replace(" ", "").upper()

    return "".join(sorted(str1)) == "".join(sorted(str2))

print(are_anagrams("listen", "silent"))
print(are_anagrams("School master", "The classroom"))
print(are_anagrams("A gentleman", "Elegant man"))
print(are_anagrams("Hello", "World"))
print(are_anagrams("apple", "banana"))
print(are_anagrams("cat", "dog"))