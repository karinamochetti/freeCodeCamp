from collections import Counter

def most_frequent(arr):
    return Counter(arr).most_common(1)[0][0]

print(most_frequent(["a", "b", "a", "c"]))
print(most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]))
print(most_frequent([True, False, "False", "True", False]))
print(most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]))
