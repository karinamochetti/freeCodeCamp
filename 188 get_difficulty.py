def get_difficulty(track):
    points = 0
    for prev, now in zip(track[0:], track[1:]):
        if (prev == "R" and now == "L") or (prev == "L" and now == "R"):
            points +=15
        elif now == "R" or now == "L":
            points += 5
    if points <= 100: return "Easy"
    elif points <= 200: return "Medium"
    else: return "Hard"
    return points

print(get_difficulty("SLSLLSRRLSRLRL"))
print(get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS"))
print(get_difficulty("SRRRRLSLLRLRSSRLSRL"))
print(get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL"))
print(get_difficulty("SLLSSLRLSLSLRSLSSLRL"))
print(get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR"))
