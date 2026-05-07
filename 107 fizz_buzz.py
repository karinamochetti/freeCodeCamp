def fizz_buzz(n):
    result = []
    for i in range(1, n+1):
        word = ""
        if i % 3 == 0: word += "Fizz"
        if i % 5 == 0: word += "Buzz"
        result.append(word or i)
    return result

print(fizz_buzz(2))
print(fizz_buzz(4))
print(fizz_buzz(8))
print(fizz_buzz(20))
print(fizz_buzz(50))
