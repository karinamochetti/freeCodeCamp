def shift_matrix(matrix, shift):
    rows, cols = len(matrix), len(matrix[0])
    total_elements = rows * cols

    flat = [cell for row in matrix for cell in row]
    shift = shift % total_elements

    shifted_flat = flat[-shift:] + flat[:-shift]

    return [shifted_flat[i * cols : (i + 1) * cols] for i in range(rows)]

print(shift_matrix([[1, 2, 3], [4, 5, 6]], 1))
print(shift_matrix([[1, 2, 3], [4, 5, 6]], -1))
print(shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5))
print(shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -6))
print(shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 7))
print(shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], -54))
