def get_deepest_brackets(s):
    stack = []
    level = 0
    max_level = 0
    max_word = ""
    for c in s:
        if c in [")", "]", "}"]:
            stack_c = stack.pop()
            word = stack_c
            while stack_c not in ["(", "[", "{"]:
                stack_c = stack.pop()
                word += stack_c
            if level > max_level:
                max_level = level
                max_word = word
            level -= 1
        else:
            if c in ["(", "[", "{"]:
                level += 1
            stack.append(c)
    return max_word[-2::-1]

print(get_deepest_brackets("(hello (world))"))
print(get_deepest_brackets("[outer [inner] outer]"))
print(get_deepest_brackets("{a{b}c{d{e}f}g}"))
print(get_deepest_brackets("[the {quick (brown [fox] jumped) over (the) lazy} dog]"))
print(get_deepest_brackets("f[(r)e{e}C{o[(d){e(C)}a]m}]p"))
