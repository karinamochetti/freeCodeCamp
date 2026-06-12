import re

def do_math(s):
    values = re.findall(r'[^\d]+|\d+', s)
    if values[0][0].isalpha(): 
        values = values[1:]
    if values[-1][0].isalpha(): 
        values = values[:-1]

    result = int(values[0])
    for i in range(1,len(values),2):
        sign = 1
        if len(values[i])%2 == 1: 
            sign = -1
        result += int(values[i+1])*sign
    
    return result

print(do_math("3ab10c8"))
print(do_math("6MINUS4"))
print(do_math("9plus3"))
print(do_math("5fkwo#10i#%.<>15P=@20!#B/25"))
print(do_math("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt"))
