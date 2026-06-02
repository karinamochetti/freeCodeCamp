def find_differences(arr):
    return [j-i for i, j in zip(arr, arr[1:]+arr[-1:])]

print(find_differences([1, 2, 4, 7]))
print(find_differences([10, 15, 19, 22, 24, 25]))
print(find_differences([25, 20, 16, 13, 11, 10]))
print(find_differences([0, 1, 2, 2, 3, 3, 4, 5]))
print(find_differences([1, 2, 5, 12, 34, -15, -1, 41, 113, -222, -99, -40, 10, -18, -6, -2, -1]))

