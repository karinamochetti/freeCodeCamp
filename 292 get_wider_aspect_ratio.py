import math

def get_wider_aspect_ratio(a, b):
    aw, ah = [int(x) for x in a.split("x")]
    bw, bh = [int(x) for x in b.split("x")]
    if aw/ah > bw/bh:
        div = math.gcd(aw, ah)
        return f"{int(aw)//div}:{int(ah)//div}"
    else:
        div = math.gcd(bw, bh)
        return f"{int(bw)//div}:{int(bh)//div}"


print(get_wider_aspect_ratio("1920x1080", "800x600"))
print(get_wider_aspect_ratio("1080x1350", "2048x1536"))
print(get_wider_aspect_ratio("640x480", "2440x1220"))
print(get_wider_aspect_ratio("360x640", "1080x1920"))
print(get_wider_aspect_ratio("3440x1440", "2048x858"))
print(get_wider_aspect_ratio("12345x61234", "12534x51234"))
