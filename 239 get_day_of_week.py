from datetime import datetime, timezone

def get_day_of_week(timestamp):
    date = datetime.fromtimestamp(timestamp / 1000.0, tz=timezone.utc)
    return date.strftime('%A')

    
print(get_day_of_week(1775492249000))
print(get_day_of_week(1766246400000))
print(get_day_of_week(33791256000000))
print(get_day_of_week(1773576000000))
print(get_day_of_week(0))
