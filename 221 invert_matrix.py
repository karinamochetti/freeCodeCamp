def invert_matrix(matrix):
    values = []
    for row in matrix:
        values += row
    v1, v2 = list(set(values))
    swap_map = {v1: v2, v2: v1}
    return [[swap_map[cell] for cell in row] for row in matrix]

print(invert_matrix([["a", "b"], ["a", "a"]]))
print(invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]]))
print(invert_matrix([["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]]))
print(invert_matrix([[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]]))
print(invert_matrix([[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]]))
