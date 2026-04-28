def sequence(n):
    string = [str(i+1) for i in range(n)]
    return "".join(string)

print(sequence(5))
print(sequence(10))
print(sequence(1))
print(sequence(27))
