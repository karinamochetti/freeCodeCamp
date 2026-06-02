from datetime import datetime, timedelta

def count_business_days(start, end):
    start_dt = datetime.strptime(start, "%Y-%m-%d")
    end_dt = datetime.strptime(end, "%Y-%m-%d")
    
    total_days = (end_dt - start_dt).days + 1
    full_weeks = total_days // 7
    business_days = full_weeks * 5
    
    start_weekday = start_dt.weekday()
    remaining_days = total_days % 7
    for i in range(remaining_days):
        current_weekday = (start_weekday + i) % 7
        # Monday through Friday
        if current_weekday < 5:
            business_days += 1
            
    return business_days

print(count_business_days("2026-06-01", "2026-06-07"))
print(count_business_days("2026-02-24", "2026-02-26"))
print(count_business_days("2026-02-24", "2026-02-28"))
print(count_business_days("2026-02-21", "2026-03-01"))
print(count_business_days("2026-03-08", "2026-03-17"))
print(count_business_days("2026-02-24", "2027-02-24"))
