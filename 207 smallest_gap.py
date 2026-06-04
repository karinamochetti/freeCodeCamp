def smallest_gap(s):
    min_dist = len(s)
    index = -1
    for i, letter in enumerate(s):
        j = s.find(letter, i+1)
        if i != -1 and j != -1 and j-i < min_dist:
            min_dist = j-i
            index = i
    return s[index+1:index+min_dist]




print(smallest_gap("ABCDAC"))
print(smallest_gap("racecar"))
print(smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4"))
print(smallest_gap("Hello World"))
print(smallest_gap("The quick brown fox jumps over the lazy dog."))
