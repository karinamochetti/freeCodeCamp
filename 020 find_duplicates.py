def find_duplicates(arr):
    seen = set()
    duplicates = set()
    
    for x in arr:
        if x in seen:
            duplicates.add(x)
        else:
            seen.add(x)

    return sorted(list(duplicates))

print(find_duplicates([1, 2, 3, 4, 5]))
print(find_duplicates([1, 2, 3, 4, 1, 2]))
print(find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]))
