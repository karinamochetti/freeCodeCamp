def sum_of_squares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i
    return sum

print(sum_of_squares(5))
print(sum_of_squares(10))
print(sum_of_squares(25))
print(sum_of_squares(500))
print(sum_of_squares(1000))
