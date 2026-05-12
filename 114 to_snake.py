def to_snake(camel):
    snake = ""
    for c in camel:
        if c.isupper(): snake += "_"
        snake += c.lower()
    return snake

print(to_snake("helloWorld"))
print(to_snake("myVariableName"))
print(to_snake("freecodecampDailyChallenges"))
