def get_spoken_duration(seconds):
    h = seconds//3600
    m = (seconds%3600)//60
    s = (seconds%3600)%60
    str = ""
    if h != 0:
        str += f"{h} hours, " if h > 1 else f"{h} hour, "
    if m != 0:
        str += f"{m} minutes, " if m > 1 else f"{m} minute, "
    if s != 0:
        str += f"{s} seconds, " if s > 1 else f"{s} second, "
    str = str[:-2] 
    i = str.rfind(", ")
    if i != -1:
        str = str[:i] + " and " + str[i + 2:]
    return str

print(get_spoken_duration(3723))
print(get_spoken_duration(7295))
print(get_spoken_duration(8521))
print(get_spoken_duration(435))
print(get_spoken_duration(14455))
print(get_spoken_duration(72000))
print(get_spoken_duration(1))
