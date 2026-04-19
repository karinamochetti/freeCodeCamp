from itertools import cycle

def evaluate(numbers, operators):
    result = numbers[0]
    op = 0
    for number, op in zip(numbers[1:], cycle(operators)):
        if op == "+": result += number
        if op == "-": result -= number
        if op == "*": result *= number
        if op == "/": result /= number
        if op == "%": result %= number
    return result

print(evaluate([5, 6, 7, 8, 9], ['+', '-']))
print(evaluate([17, 61, 40, 24, 38, 14], ['+', '%']))
print(evaluate([20, 2, 4, 24, 12, 3], ['*', '/']))
print(evaluate([11, 4, 10, 17, 2], ['*', '*', '%']))
print(evaluate([33, 11, 29, 13], ['/', '-']))
