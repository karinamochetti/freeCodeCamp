def one_hundred(chars):
    times = 100//len(chars)
    extra = 100-(times*len(chars))
    print(times, extra)
    return (chars * times) + chars[:extra]

print(one_hundred("One hundred "))
print(one_hundred("freeCodeCamp "))
print(one_hundred("daily challenges "))
print(one_hundred("!"))
