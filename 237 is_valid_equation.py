def is_valid_equation(equation):
    equation = equation.split()
    result = int(equation[-1])
    equation = equation[:-2]
    
    stack = []
    current_op = "+" 
    
    for elem in equation:
        if elem in ["+", "-", "*", "/"]:
            current_op = elem
        else:
            num = int(elem)
            
            if current_op == "+":
                stack.append(num)
            elif current_op == "-":
                stack.append(-num)  
            elif current_op == "*":
                stack.append(stack.pop() * num)
            elif current_op == "/":
                stack.append(stack.pop() // num) 

    return sum(stack) == result

print(is_valid_equation("2 + 2 = 4"))
print(is_valid_equation("2 + 3 - 1 = 4"))
print(is_valid_equation("8 / 2 = 4"))
print(is_valid_equation("10 * 5 = 50"))
print(is_valid_equation("2 - 2 = 0"))
print(is_valid_equation("2 + 9 / 3 = 5"))
print(is_valid_equation("20 - 2 * 3 = 14"))
print(is_valid_equation("2 + 5 = 6"))
print(is_valid_equation("10 - 2 * 3 = 24"))
print(is_valid_equation("3 + 9 / 3 = 4"))
