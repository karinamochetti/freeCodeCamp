from itertools import cycle

def decode(message):
    KEY = cycle("VLHCGMDLNH")
    decoded = []
    i = 0
    for c in message:
        if c.isalpha():
            key_char = next(KEY)
            shift = (ord(c) - ord(key_char)) % 26
            decoded_char = chr(ord("A") + shift - 1)
            decoded.append(decoded_char)
        else:
            decoded.append(" ")
    return "".join(decoded)

print(decode("YAVJYNXE"))
print(decode("YALLUT PQUMJP"))
print(decode("UAC DYR EISAKYM"))
print(decode("GQMS NBMZU"))
print(decode("W IQQURV UG I ZDMDTRV IVW JQDHY TMHSA QB"))
