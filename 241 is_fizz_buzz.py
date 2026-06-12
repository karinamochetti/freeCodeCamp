def is_fizz_buzz(arr):

    start = next((val - idx for idx, val in enumerate(arr) if isinstance(val, int)), None)
    if start is None: return False

    for num,a in zip(range(start,start+len(arr)+1), arr):
        if num % 15 == 0:
            if a != "FizzBuzz": return False
        elif num % 5 == 0:
            if a != "Buzz": return False
        elif num % 3 == 0:
            if a != "Fizz": return False
        else:
            if a != num: return False
    return True

print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz"]))
print(is_fizz_buzz([13, 14, "FizzBuzz", 16, 17]))
print(is_fizz_buzz([1, 2, "Fizz", 4, 5]))
print(is_fizz_buzz(["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]))
print(is_fizz_buzz([1, 2, "Fizz", "Buzz", 5]))
print(is_fizz_buzz([97, 98, "Buzz", "Fizz", 101, "Fizz", 103]))
print(is_fizz_buzz(["Fizz", "Buzz", 101, "Fizz", 103, 104, "FizzBuzz"]))
