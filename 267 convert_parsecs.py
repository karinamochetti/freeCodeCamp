def convert_parsecs(parsecs):
    return parsecs*2 if parsecs%2 else parsecs*3

print(convert_parsecs(1))
print(convert_parsecs(2))
print(convert_parsecs(31))
print(convert_parsecs(88))
print(convert_parsecs(17))
print(convert_parsecs(14))
