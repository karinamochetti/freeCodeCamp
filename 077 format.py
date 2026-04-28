def format(seconds):
    h = seconds//3600
    m = (seconds%3600)//60
    s = (seconds%3600)%60
    if h > 0: return f"{h}:{m:02d}:{s:02d}"
    else: return f"{m}:{s:02d}"

print(format(500))
print(format(4000))
print(format(1))
print(format(5555))
print(format(99999))
