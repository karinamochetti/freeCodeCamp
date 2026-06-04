def is_flat(arr):
    return not any(elem for elem in arr if isinstance(elem, list))

print(is_flat([1, 2, 3, 4]))
print(is_flat([1, [2, 3], 4]))
print(is_flat([1, 0, False, True, "a", "b"]))
print(is_flat([1, 0, False, True, "a", "b"]))
print(is_flat([1, [2, [3, [4, [5]]]], 6]))
