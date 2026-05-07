def is_fizz_buzz(sequence):
    for i in range(1, len(sequence)+1):
        word = ""
        if i%3 == 0: word += "Fizz"
        if i%5 == 0: word += "Buzz"
        value = word or i
        if sequence[i-1] != value:
            return False
    return True

print(is_fizz_buzz([1, 2, "Fizz", 4]))
print(is_fizz_buzz([1, 2, 3, 4]))
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 7]))
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "FizzBuzz"]))
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Fizz"]))
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Buzz"]))
print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]))
