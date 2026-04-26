from datetime import date

def moon_phase(date_string):
    day = int(date_string[8:10])
    month = int(date_string[5:7])
    year = int(date_string[0:4])
    days = (date(year, month, day) - date(2000, 1, 6)).days
    if 1 <= (days%28)+1 <= 7: return "New"
    if 8 <= (days%28)+1 <= 14: return "Waxing"
    if 15 <= (days%28)+1 <= 21: return "Full"
    if 22 <= (days%28)+1 <= 28: return "Waning"
    return ""

print(moon_phase("2000-01-12"))
print(moon_phase("2000-01-13"))
print(moon_phase("2014-10-15"))
print(moon_phase("2012-10-21"))
print(moon_phase("2022-12-14"))
