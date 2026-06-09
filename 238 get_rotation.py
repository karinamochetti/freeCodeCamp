def get_rotation(n):
    s = str(n)
    l = len(s)
    for i in range(l):
        if int(s[i:] + s[:i]) % l == 0:
            return i
    return "none"

print(get_rotation(123))
print(get_rotation(13579))
print(get_rotation(24681))
print(get_rotation(84138789345))
