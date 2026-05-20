def array_swap(arr):
    arr[0], arr[1] = arr[1], arr[0]
    return arr

print(array_swap(["A", "B"]))
print(array_swap([25, 20]))
print(array_swap([True, False]))
print(array_swap(["1", 1]))
