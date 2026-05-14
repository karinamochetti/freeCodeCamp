def pairwise(arr, target):
    n = len(arr)
    values = 0
    for i, num_i in enumerate(arr):
        for j, num_j in enumerate(arr[i:], start=i):
            if i != j and num_i+num_j == target:
                values += i+j

    return values

print(pairwise([2, 3, 4, 6, 8], 10))
print(pairwise([4, 1, 5, 2, 6, 3], 7))
print(pairwise([-30, -15, 5, 10, 15, -5, 20, -40], -20))
print(pairwise([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24))