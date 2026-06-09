def capitalize_fibonacci(s):
    FIBO = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    new_s = [s.upper() if i in FIBO else s.lower() for i, s in enumerate(s)]
    return "".join(new_s)


print(capitalize_fibonacci("hello world"))
print(capitalize_fibonacci("HELLO WORLD"))
print(capitalize_fibonacci("hello, world!"))
print(capitalize_fibonacci("The quick brown fox jumped over the lazy dog."))
print(capitalize_fibonacci("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar ex nibh, vel ullamcorper ligula egestas quis. Integer tincidunt fringilla accumsan. Integer et metus placerat, gravida felis at, pellentesque nisl."))
