def solve_magic_square(grid):
    for i, j in zip(range(3), range(3)):
        if grid[i][j] == 0: break

    target_sum = sum(grid[i-1])
    missing_value = target_sum - sum(grid[i])
    grid[i][j] = missing_value

    row = sum(grid[i])
    col = sum(grid[k][j] for k in range(3))
    diag1 = sum(grid[k][k] for k in range(3))
    diag2 = sum(grid[k][2-k] for k in range(3))

    if row == col == diag1 == diag2:
        return grid[i][j]
    else:
        return "impossible"

print(solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]]))
print(solve_magic_square([[0, 14, 12], [18, 10, 2], [8, 6, 16]]))
print(solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]]))
print(solve_magic_square([[15, 35, 31], [43, 27, 11], [23, 19, 0]]))
print(solve_magic_square([[26, 41, 14], [47, 35, 0], [32, 29, 44]]))
