def rgb_to_hex(rgb):
    values = rgb[4:-1].split(", ")
    print(values)
    return f"#{int(values[0]):02x}{int(values[1]):02x}{int(values[2]):02x}"

print(rgb_to_hex("rgb(255, 255, 255)"))
print(rgb_to_hex("rgb(1, 11, 111)"))
print(rgb_to_hex("rgb(173, 216, 230)"))
print(rgb_to_hex("rgb(79, 123, 201)"))
