import string

def decode(message, shift):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    shifted_lower = lower[-shift:] + lower[:-shift]
    shifted_upper = upper[-shift:] + upper[:-shift]
    table = str.maketrans(lower + upper, shifted_lower + shifted_upper)
    
    return message.translate(table)



print(decode("Xlmw mw e wigvix qiwweki.", 4))
print(decode("Byffi Qilfx!", 20))
print(decode("Zqd xnt njzx?", -1))
print(decode("oannLxmnLjvy", 9))
