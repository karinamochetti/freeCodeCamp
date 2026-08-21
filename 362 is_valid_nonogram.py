def is_valid_nonogram(clue, cells):
    n = len(cells)
    str_cells = "".join(str(num) for num in cells)
    for i in range(n, 1, -1):
        str_cells = str_cells.replace("1"*i, str(i))
    str_cells = str_cells.replace("0", "")

    n = len(clue)
    str_clue = "".join(str(num) for num in clue)

    return str_clue == str_cells

print(is_valid_nonogram([3, 2], [1, 1, 1, 0, 1, 1]))
print(is_valid_nonogram([3, 2], [0, 1, 1, 1, 1, 1]))
print(is_valid_nonogram([1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1]))
print(is_valid_nonogram([1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]))
print(is_valid_nonogram([3, 2, 3], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0]))
print(is_valid_nonogram([3, 2, 3], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]))
