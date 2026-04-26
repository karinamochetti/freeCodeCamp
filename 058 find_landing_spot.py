def find_landing_spot(matrix):
    min_risk = 9*4
    indices = [-1, -1]
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                risk = 0
                if i-1 >= 0: risk += matrix[i-1][j]
                if i+1 < n: risk += matrix[i+1][j]
                if j-1 >= 0: risk += matrix[i][j-1]
                if j+1 < m: risk += matrix[i][j+1]
                if risk < min_risk:
                    indices[0] = i
                    indices[1] = j
                    min_risk = risk
    return indices

print(find_landing_spot([[1, 0], [2, 0]]))
print(find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]))
print(find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]))
print(find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]))
