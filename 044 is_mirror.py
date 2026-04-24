def is_mirror(str1, str2):
    str1 = "".join(char for char in str1 if char.isalnum())
    str2 = "".join(char for char in str2 if char.isalnum())
    return str1[::-1] == str2

print(is_mirror("helloworld", "helloworld"))
print(is_mirror("Hello World", "dlroW olleH"))
print(is_mirror("RaceCar", "raCecaR"))
print(is_mirror("RaceCar", "RaceCar"))
print(is_mirror("Mirror", "rorrim"))
print(is_mirror("Hello World", "dlroW-olleH"))
print(is_mirror("Hello World", "!dlroW !olleH"))

