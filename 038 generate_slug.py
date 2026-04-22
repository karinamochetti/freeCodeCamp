def generate_slug(string):
    words = string.lower().split()
    list_srt = []
    for word in words:
        w = [char for char in word if char.isalnum()]
        list_srt.append("".join(w))


    return "%20".join(list_srt)

print(generate_slug("helloWorld"))
print(generate_slug("hello world!"))
print(generate_slug(" hello-world "))
print(generate_slug("hello  world"))
print(generate_slug("  ?H^3-1*1]0! W[0%R#1]D  "))
