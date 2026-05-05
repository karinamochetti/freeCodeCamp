def build_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

print(build_matrix(2, 3))
print(build_matrix(3, 2))
print(build_matrix(4, 3))
print(build_matrix(9, 1))
