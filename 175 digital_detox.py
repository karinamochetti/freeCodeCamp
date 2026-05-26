from datetime import datetime, timedelta

def digital_detox(logs):
    logs.sort()

    days = [date[:10] for date in logs]
    if len(days) > 2:
        for prev, now in zip(days[0:], days[2:]):
            if prev == now:
                return False

    logs_datetime = [datetime.strptime(date, "%Y-%m-%d %H:%M:%S") for date in logs]
    if len(days) > 1:
        for prev, now in zip(logs_datetime[0:], logs_datetime[1:]):
            if now - prev <= timedelta(hours=4):
                return False

    return True

print(digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]))
print(digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"]))
print(digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"]))
print(digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"]))
print(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]))
print(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]))
