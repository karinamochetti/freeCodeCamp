from datetime import date

def days_until_birthday(today, birthday):
    y, m, d = map(int, today.split("-"))
    date_start = date(y, m, d)
    m, d = map(int, birthday.split("/"))

    while True:
        try:
            date_end = date(y, m, d)
            delta = date_end - date_start
            if delta.days > 0: 
                return delta.days
        except:
            pass
        y += 1


print(days_until_birthday("2026-07-16", "9/7"))
print(days_until_birthday("2026-07-16", "3/22"))
print(days_until_birthday("2026-07-16", "7/16"))
print(days_until_birthday("2024-02-28", "3/1"))
print(days_until_birthday("2023-04-24", "12/30"))
print(days_until_birthday("2024-03-01", "2/29"))
print(days_until_birthday("2096-03-01", "2/29"))
