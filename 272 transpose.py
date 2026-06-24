def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

print(transpose([[1, 2, 3], [4, 5, 6]]))
print(transpose([[1, 2], [3, 4], [5, 6]]))
print(transpose([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(transpose([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]]))
print(transpose([[True, False, True, False], [False, True, False, True], [True, True, False, False], [False, False, True, True], [True, False, False, True]]))
