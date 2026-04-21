def array_diff(arr1, arr2):
    return sorted(list(set(arr1) ^ set(arr2)))

print(array_diff(["apple", "banana"], ["apple", "banana", "cherry"]))
print(array_diff(["apple", "banana", "cherry"], ["apple", "banana"]))
print(array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]))
print(array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"]))
print(array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]))
