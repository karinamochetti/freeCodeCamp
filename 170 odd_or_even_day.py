from datetime import datetime, timezone

def odd_or_even_day(timestamp):
    date = datetime.fromtimestamp(timestamp//1000, tz=timezone.utc)
    if date.day%2 == 0: return "even"
    return "odd"

print(odd_or_even_day(1769472000000))
print(odd_or_even_day(1769444440000))
print(odd_or_even_day(6739456780000))
print(odd_or_even_day(1))
print(odd_or_even_day(86400000))
