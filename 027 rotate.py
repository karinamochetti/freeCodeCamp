def rotate(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rot_matrix = []
    for j in range(m):
        row = []
        for i in range(n-1, -1, -1):
            row.append(matrix[i][j])
        rot_matrix.append(row)
    return rot_matrix

print(rotate([[1]]))
print(rotate([[1, 2], [3, 4]]))
print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate([[0, 1, 0], [1, 0, 1], [0, 0, 0]]))
