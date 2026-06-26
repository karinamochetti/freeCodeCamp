def get_zone_violations(grid):

    RULES = {
        "i": ["R", "I"],
        "A": ["C"],
        "R": ["i", "C"],
        "I": ["i"],
        "C": ["R", "A"],
        "": [],
    }

    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    violators = []
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in RULES and any(
            0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] in RULES[grid[r][c]]
            for dr, dc in directions):
                violators.append([r,c])

    return violators

print(get_zone_violations([["R", "C"], ["", "C"]]))
print(get_zone_violations([["", "i"], ["", "R"], ["R", "I"]]))
print(get_zone_violations([["A", "i", "C"], ["A", "", "C"], ["R", "R", "I"]]))
print(get_zone_violations([["R", "R", "C", "R", "R"], ["R", "I", "C", "", "A"], ["R", "R", "", "i", "A"]]))
print(get_zone_violations([["R", "A", "A", "", "i", "i"], ["R", "I", "", "C", "i", "i"], ["R", "", "C", "C", "A", "A"], ["R", "R", "C", "I", "R", "R"]]))
