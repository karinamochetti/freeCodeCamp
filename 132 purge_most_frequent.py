from collections import Counter

def purge_most_frequent(arr):
    counter = Counter(arr)
    max_count = max(counter.values())
    return [elem for elem in arr if counter[elem] != max_count]

print(purge_most_frequent([1, 2, 2, 3]))
print(purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"]))
print(purge_most_frequent(["red", "blue", "green", "red", "blue", "green", "blue"]))
print(purge_most_frequent([5, 5, 5, 5]) )
print(purge_most_frequent([10, 12, 7, 3, 7, 7, 12, 12]))
