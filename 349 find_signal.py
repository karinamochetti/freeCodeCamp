def find_signal(grid):

    def get_neighbors(i, j, n):
        return {(i + dr, j + dc) for dr in (-n, 0, n) for dc in (-n, 0, n) if dr != 0 or dc != 0}

    towers = [
        get_neighbors(r, c, val)
        for r, row in enumerate(grid)
        for c, val in enumerate(row)
        if val != 0
    ]
        
    shared_signals = set.intersection(*towers)
    return list(shared_signals.pop()) if shared_signals else []

print(find_signal([[0, 0, 1], [0, 1, 0], [0, 0, 1]]))
print(find_signal([[0, 2, 0], [1, 0, 0], [0, 0, 1]]))
print(find_signal([[0, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 1]]))
print(find_signal([[0, 3, 0, 0, 0], [0, 0, 0, 0, 2], [0, 0, 0, 0, 0], [4, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
print(find_signal([[3, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 2]]))