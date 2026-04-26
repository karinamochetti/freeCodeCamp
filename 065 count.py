def count(text, parameter):
    n = len(parameter)
    count = 0
    for i in range(len(text)-n+1):
        if parameter == text[i:i+n]: count += 1
    return count

print(count('abcdefg', 'def'))
print(count('hello', 'world'))
print(count('mississippi', 'iss'))
print(count('she sells seashells by the seashore', 'sh'))
print(count('101010101010101010101', '101'))
