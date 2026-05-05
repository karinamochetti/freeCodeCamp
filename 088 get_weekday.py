from datetime import datetime

def get_weekday(date_string):
    date = datetime.strptime(date_string, "%Y-%m-%d")
    return date.strftime("%A")

print(get_weekday("2025-11-06"))
print(get_weekday("1999-12-31"))
print(get_weekday("1111-11-11"))
print(get_weekday("2112-12-21"))
print(get_weekday("2345-10-01"))
