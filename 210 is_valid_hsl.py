def is_valid_hsl(hsl):
    if hsl[:4] != "hsl(":
        return False
    hsl = hsl[4:]
    hsl = hsl.replace(" ", "")
    hsl = hsl.replace(")", "")
    hsl = hsl.replace(";", "")
    hsl = hsl.split(",")

    if hsl[1][-1] != "%" or hsl[2][-1] != "%":
        return False

    h = int(hsl[0])
    s = int(hsl[1][:-1])
    l = int(hsl[2][:-1])

    if h < 0 or h > 360:
        return False
    if s < 0 or s > 100:
        return False
    if l < 0 or l > 100:
        return False
    return True

print(is_valid_hsl("hsl(240, 50%, 50%)"))
print(is_valid_hsl("hsl( 200 , 50% , 75% )"))
print(is_valid_hsl("hsl(99,60%,80%);"))
print(is_valid_hsl("hsl(0, 0%, 0%) ;"))
print(is_valid_hsl("hsl(  10  ,  20%   ,  30%   )    ;"))
print(is_valid_hsl("hsl(361, 50%, 80%)"))
print(is_valid_hsl("hsl(300, 101%, 70%)"))
print(is_valid_hsl("hsl(200, 55%, 75)"))
print(is_valid_hsl("hsl (80, 20%, 10%)"))
