def is_sorted(arr):
    if sorted(arr) == arr:
        return "Ascending"
    if sorted(arr) == arr[::-1]:
        return "Descending"
    return "Not sorted"

print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([10, 8, 6, 4, 2]))
print(is_sorted([1, 3, 2, 4, 5]))
print(is_sorted([3.14, 2.71, 1.61, 0.57]))
print(is_sorted([12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9]))
print(is_sorted([0.4, 0.5, 0.3]))
