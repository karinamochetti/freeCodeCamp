def decode(string):
    stack = []
    for char in string:
        if char == ")":
            temp = []
            while stack and stack[-1] != "(":
                temp.append(stack.pop())
            if stack and stack[-1] == "(":
                stack.pop() 
            stack += temp
        else:
            stack.append(char)
    return "".join(stack)

print(decode("abc"))
print(decode("(f(b(dc)e)a)"))
print(decode("((is?)(a(t d)h)e(n y( uo)r)aC)"))
print(decode("f(Ce(re))o((e(aC)m)d)p"))

