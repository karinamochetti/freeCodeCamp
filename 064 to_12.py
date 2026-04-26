def to_12(time):
    hour = int(time[0:2])
    minute = int(time[2:4])
    if hour <= 12: ap ="A"
    else: ap = "P"
    hour %= 12
    if hour == 0: hour += 12
    return f"{hour}:{minute:02d} {ap}M"

print(to_12("1124"))
print(to_12("0900"))
print(to_12("1455"))
print(to_12("2346"))
print(to_12("0030"))
