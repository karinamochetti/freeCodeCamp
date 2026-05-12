def game_of_life(grid):
    rows = len(grid)
    cols = len(grid[0])

    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def live_neighbors(grid, r, c):
        count = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue                
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    count += grid[nr][nc]
        return count

    for r in range(rows):
        for c in range(cols):
            neighbors = live_neighbors(grid, r, c)
            if grid[r][c] == 1:
                new_grid[r][c] = 1 if neighbors in (2, 3) else 0
            else:
                new_grid[r][c] = 1 if neighbors == 3 else 0
            
    return new_grid

print(game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]]))
print(game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]))
print(game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]]))
