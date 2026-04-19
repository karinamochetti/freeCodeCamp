import random

def generate_hex(color):
    rand1 = random.randint(1, 254)
    rand2 = random.randint(1, 254)
    if color == "red": return f"FF{rand1:02X}{rand2:02X}" 
    if color == "green": return f"{rand1:02X}FF{rand2:02X}"
    if color == "blue": return f"{rand1:02X}{rand2:02X}FF"
    return "Invalid color"

print(generate_hex("yellow"))
print(generate_hex("red"))
print(generate_hex("red"))
print(generate_hex("red"))
print(generate_hex("red"))
print(generate_hex("green"))
print(generate_hex("blue"))
print(generate_hex("blue"))

