def check_strength(password):
    rules = 0

    if len(password) >= 8:
        rules += 1

    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        rules += 1    

    if any(c.isdigit() for c in password):
        rules += 1

    if any(c in "!@#$%^&*" for c in password):
        rules += 1

    if rules < 2: return "weak"
    if rules == 4: return "strong"
    return "medium"
    
print(check_strength("123456"))
print(check_strength("pass!!!"))
print(check_strength("Qwerty"))
print(check_strength("PASSWORD"))
print(check_strength("PASSWORD!"))
print(check_strength("PassWord%^!"))
print(check_strength("qwerty12345"))
print(check_strength("S3cur3P@ssw0rd"))
print(check_strength("C0d3&Fun!"))
