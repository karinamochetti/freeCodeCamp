def verify(message, key, signature):
    value = 0
    for c in message + key:
        if 'a' <= c <= 'z': 
            value += ord(c)-ord('a')+1
        if 'A' <= c <= 'Z': 
            value += ord(c)-ord('A')+27
    return value == signature

print(verify("foo", "bar", 57))
print(verify("foo", "bar", 54))
print(verify("freeCodeCamp", "Rocks", 238))
print(verify("Is this valid?", "Yes", 210))
print(verify("Is this valid?", "Yes", 233))
print(verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514))
