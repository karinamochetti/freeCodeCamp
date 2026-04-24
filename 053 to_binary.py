def to_binary(decimal):
    binary = ""
    while decimal != 0:
        binary += str(decimal%2)
        decimal //= 2
    return binary[::-1]

print(to_binary(5))
print(to_binary(12))
print(to_binary(50))
print(to_binary(99))
