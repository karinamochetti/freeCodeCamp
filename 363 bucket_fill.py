def bucket_fill(grid, target_color): 
    regions = 0 
    rows = len(grid) 
    cols = len(grid[0]) 
    
    def find_neighbors(grid, i, j): 
        color = grid[i][j] 
        stack = [(i, j)] 
        while len(stack) > 0: 
            i, j = stack.pop() 
            grid[i][j] = regions 
            if i+1 < rows and grid[i+1][j] == color: 
                stack.append((i+1, j)) 
            if i-1 >= 0 and grid[i-1][j] == color: 
                stack.append((i-1, j)) 
            if j+1 < cols and grid[i][j+1] == color: 
                stack.append((i, j+1)) 
            if j-1 >= 0 and grid[i][j-1] == color: 
                stack.append((i, j-1)) 
        return 
        
    for i in range(len(grid)): 
        for j in range(len(grid[i])): 
            if not isinstance(grid[i][j], int) and grid[i][j] != target_color: 
                regions += 1 
                find_neighbors(grid, i, j) 
    
    return regions
        
print(bucket_fill([["R", "R"], ["R", "R"]], "G"))
print(bucket_fill([["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]], "B"))
print(bucket_fill([["G", "Y", "Y"], ["G", "Y", "G"], ["Y", "Y", "G"]], "R"))
print(bucket_fill([["G", "G", "P", "Y"], ["O", "P", "P", "P"], ["O", "O", "P", "G"], ["G", "O", "O", "G"]], "P"))
print(bucket_fill([["G", "G", "C", "C", "O"], ["B", "Y", "B", "Y", "O"], ["B", "J", "O", "J", "B"], ["G", "Y", "Y", "Y", "B"], ["G", "P", "P", "G", "G"]], "Y"))