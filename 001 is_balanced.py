def is_balanced(string):
    vowels = "aeiouAEIOU"
    left = [s for s in string[:int(len(string)/2)] if s in vowels]
    print(left)
    right = [s for s in string[int((len(string)+1)/2):] if s in vowels]
    return len(left) == len(right)


is_balanced("racecar")
is_balanced("Lorem Ipsum")
is_balanced("Kitty Ipsum")
is_balanced("string")
is_balanced(" ")
is_balanced("abcdefghijklmnopqrstuvwxyz")
is_balanced("123A#b!E&*456-o.U")
