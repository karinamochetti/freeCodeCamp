def calculate_age(birthday):
    year,month,day = birthday.split("-")
    age = 2025-int(year)
    if int(month) > 11: 
        age -= 1
    if int(month) == 11 and int(day) > 27: 
        age -= 1
    return age

print(calculate_age("2000-11-20"))
print(calculate_age("2000-12-01"))
print(calculate_age("2014-10-25"))
print(calculate_age("1994-01-06"))
print(calculate_age("1994-12-14"))
