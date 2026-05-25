def fizz_buzz_mini(n):
    result = ""
    if n % 3 == 0: result += "Fizz"
    if n % 5 == 0: result += "Buzz"
    if result == "": result = str(n)
    return result

print(fizz_buzz_mini(3))
print(fizz_buzz_mini(4))
print(fizz_buzz_mini(35))
print(fizz_buzz_mini(75))
print(fizz_buzz_mini(98))
