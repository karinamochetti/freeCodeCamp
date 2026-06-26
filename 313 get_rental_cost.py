from datetime import datetime, timedelta
import math

def get_rental_cost(rented, returned, tier):
    BASE_COST = {1: 4.99, 3: 3.99, 7: 2.99}
    LATE_FEE = {1: 3.99, 3: 2.99, 7: 0.99}

    dt_rented = datetime.strptime(rented, "%Y-%m-%dT%H:%M:%SZ") + timedelta(days=tier)
    due = dt_rented.strftime("%Y-%m-%d") + "T12:00:00Z"

    dt_due = datetime.strptime(due, "%Y-%m-%dT%H:%M:%SZ")
    dt_returned = datetime.strptime(returned, "%Y-%m-%dT%H:%M:%SZ")

    days_late = math.ceil(max(0, (dt_returned - dt_due).total_seconds())/(3600*24))

    price = BASE_COST[tier] + days_late*LATE_FEE[tier]

    return f"${price:.2f}"

print(get_rental_cost("2026-06-18T18:30:00Z", "2026-06-19T10:30:00Z", 1)) #0
print(get_rental_cost("2026-06-18T14:30:00Z", "2026-06-20T12:30:00Z", 1)) #2
print(get_rental_cost("2026-06-18T10:15:00Z", "2026-06-18T19:45:00Z", 3)) #0
print(get_rental_cost("2026-06-18T15:20:00Z", "2026-06-23T08:10:00Z", 3)) #4
print(get_rental_cost("2026-06-18T12:00:00Z", "2026-06-25T12:00:00Z", 7)) #0
print(get_rental_cost("2026-06-18T08:00:00Z", "2027-06-18T14:00:00Z", 7)) #359
