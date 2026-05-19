def nth_fibonacci(n):
    if n == 1:
        return 0

    fibo = 1
    fibo_prev = 0
    for _ in range(n-2):
        fibo, fibo_prev = fibo_prev+fibo, fibo
    return fibo

print(nth_fibonacci(4))
print(nth_fibonacci(10))
print(nth_fibonacci(15))
print(nth_fibonacci(40))
print(nth_fibonacci(75))
