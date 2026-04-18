def squares_with_three(n):
    count = 0
    for i in range(1, n):
        if '3' in str(i*i):
            count += 1
    return count


print(squares_with_three(1))
print(squares_with_three(10))
print(squares_with_three(100))
print(squares_with_three(1000))
print(squares_with_three(10000))