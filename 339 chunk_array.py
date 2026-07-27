def chunk_array(arr, size):
    n = len(arr)
    return [arr[i:min(i+size, n)] for i in range(0, n, size)]

print(chunk_array([1, 2, 3, 4, 5, 6], 3))
print(chunk_array([1, "two", 3, "four", 5, "six", 7, "eight"], 2))
print(chunk_array([1, 2, 3, 4, 5], 3))
print(chunk_array(["a", "b", "c", "d", "e"], 1))
print(chunk_array([1, 2, 3], 5))
