def difference(arr1, arr2):
    s1, s2 = set(arr1), set(arr2)
    return [x for x in arr1 if x not in s2] + [x for x in arr2 if x not in s1]


print(difference([1, 2, 3], [3, 4, 5]))
print(difference(["a", "b"], ["c", "b"]))
print(difference([1, "a", 2], [2, "b", "a"]))
print(difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
