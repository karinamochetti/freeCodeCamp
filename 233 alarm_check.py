def alarm_check(alarm_time, wake_time):
    alarm_h, alarm_m = alarm_time.split(":")
    alarm_min = int(alarm_h*60) + int(alarm_m)
    wake_h, wake_m = wake_time.split(":")
    wake_min = int(wake_h*60) + int(wake_m)

    if wake_min < alarm_min: return "early"
    if wake_min <= alarm_min+10: return "on time"
    if alarm_min+10 < wake_min: return "late"

print(alarm_check("07:00", "06:45"))
print(alarm_check("06:30", "06:30"))
print(alarm_check("08:10", "08:15"))
print(alarm_check("09:30", "09:45"))
print(alarm_check("08:15", "08:25"))
print(alarm_check("05:45", "05:56"))
print(alarm_check("04:30", "04:00"))
