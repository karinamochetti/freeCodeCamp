def pascal_row(n):
    row = [1]
    row_idx = n - 1 
    
    val = 1
    for k in range(1, n):
        val = val * (n - k) // k
        row.append(val)
    return row

print(pascal_row(5))
print(pascal_row(3))
print(pascal_row(1))
print(pascal_row(10))
print(pascal_row(15))
