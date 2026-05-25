def scale_image(size, scale):
    w, h = size.split("x")
    return f"{int(int(w)*scale)}x{int(int(h)*scale)}"

print(scale_image("800x600", 2))
print(scale_image("100x100", 10))
print(scale_image("1024x768", 0.5))
print(scale_image("300x200", 1.5))
