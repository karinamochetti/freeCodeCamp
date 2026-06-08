from datetime import datetime

def can_retake(finish_time, current_time):
    finish_dt = datetime.strptime(finish_time,"%Y-%m-%dT%H:%M:%S")
    current_dt = datetime.strptime(current_time,"%Y-%m-%dT%H:%M:%S")
    if (current_dt - finish_dt).days >= 2:
        return True
    return False

print(can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00"))
print(can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00"))
print(can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00"))
print(can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59"))
