def get_due_date(date_str):
    MAX_DAY = [31,28,31,30,31,30,31,31,30,31,30,31]
    y,m,d = date_str.split("-")
    new_m = int(m) + 9
    new_y = int(y)
    new_d = int(d)
    if new_m > 12:
        new_y += 1
        new_m %= 12
    if new_d > MAX_DAY[new_m-1]: new_d = MAX_DAY[new_m-1]
    return f"{new_y:04d}-{new_m:02d}-{new_d:02d}"



print(get_due_date("2025-03-30"))
print(get_due_date("2025-04-27") )
print(get_due_date("2025-05-29"))
print(get_due_date("2026-06-30"))
print(get_due_date("2026-10-11"))
