def speed_check(speed_mph, speed_limit_kph):
    speed_kph = speed_mph * 1.60934 
    if speed_kph < speed_limit_kph:
        return "Not Speeding"
    if speed_kph - speed_limit_kph <= 5:
        return "Warning"
    if speed_kph - speed_limit_kph > 5:
        return "Ticket"

print(speed_check(30, 70))
print(speed_check(40, 60))
print(speed_check(40, 65))
print(speed_check(60, 90))
print(speed_check(65, 100))
print(speed_check(88, 40))
