def get_element_size(window_size, element_vw, element_vh):
    width, height = window_size.split("x")
    vw = int(element_vw[:-2])/100
    vh = int(element_vh[:-2])/100
    return f"{int(vw*int(width))} x {int(vh*int(height))}"


print(get_element_size("1200 x 800", "50vw", "50vh"))
print(get_element_size("320 x 480", "25vw", "50vh"))
print(get_element_size("1000 x 500", "7vw", "3vh"))
print(get_element_size("1920 x 1080", "95vw", "100vh"))
print(get_element_size("1200 x 800", "0vw", "0vh"))
print(get_element_size("1440 x 900", "100vw", "114vh"))
