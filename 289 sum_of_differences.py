def sum_of_differences(arr):
    diffs = [a2-a1 for a1, a2 in zip(arr[:-1], arr[1:])]
    return sum(diffs)

print(sum_of_differences([1, 3, 4]))
print(sum_of_differences([5, -3, 3, 9, 10]))
print(sum_of_differences([9, 6, 15, -20, 33, 14, 25, 16, -7]))
print(sum_of_differences([50, 102, -46, 82, -49, 29, 71, 902, -237, 111, -61, 75]))
