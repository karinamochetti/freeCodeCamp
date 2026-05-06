from datetime import datetime

def days_until_weekend(date_string):
    date = datetime.strptime(date_string, "%Y-%m-%d")
    if 0 <= date.weekday() <= 3:
        return f"{5-date.weekday()} days until the weekend."
    if date.weekday() == 4:
        return f"1 day until the weekend."
    return "It's the weekend!"

print(days_until_weekend("2025-11-14"))
print(days_until_weekend("2025-01-01"))
print(days_until_weekend("2025-12-06"))
print(days_until_weekend("2026-01-27"))
print(days_until_weekend("2026-09-07"))
print(days_until_weekend("2026-11-29"))
