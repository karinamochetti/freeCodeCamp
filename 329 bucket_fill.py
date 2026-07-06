def bucket_fill(grid, pos, new_value):
    r, c = pos
    old_value = grid[r][c]

    def filling(pos, old_value, new_value):
        r, c = pos
        if grid[r][c] == old_value:
            grid[r][c] = new_value
            if r-1 >= 0:
                filling([r-1, c], old_value, new_value)
            if c-1 >= 0:
                filling([r, c-1], old_value, new_value)
            if r+1 < len(grid):
                filling([r+1, c], old_value, new_value)
            if c+1 < len(grid[0]):
                filling([r, c+1], old_value, new_value)

    filling(pos, old_value, new_value)
    return grid

print(bucket_fill([["R", "G"], ["R", "G"]], [0, 1], "B"))
print(bucket_fill([["Y", "G", "G"], ["Y", "Y", "Y"], ["B", "Y", "R"]], [1, 2], "B"))
print(bucket_fill([["O", "O", "P"], ["P", "O", "O"], ["P", "P", "O"]], [2, 0], "R"))
print(bucket_fill([["T", "T", "R", "T"], ["R", "T", "R", "T"], ["R", "T", "R", "T"], ["T", "T", "T", "T"]], [0, 3], "Y"))
print(bucket_fill([["G", "B", "G", "B"], ["R", "B", "B", "G"], ["B", "G", "B", "R"], ["B", "G", "G", "B"]], [2, 2], "G"))
