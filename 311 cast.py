def cast(spells):
    BASE = {
        "f": 3,
        "l": 3,
        "i": 2,
        "w": 2,
        "h": 1,
        "s": 1,
    }
    CAT = {
        "f": "destruction",
        "l": "destruction",
        "i": "control",
        "w": "control",
        "h": "restoration",
        "s": "restoration",
    }
    score = BASE[spells[0]]
    mult = 1
    for s_prev, s in zip(spells[:-1], spells[1:]):
        if CAT[s_prev] != CAT[s]:
            mult += 1
        else:
            mult = 1
        score += BASE[s]*mult
    return score

print(cast("fihwl"))
print(cast("lwswfi"))
print(cast("wislhfl"))
print(cast("sihwlih"))
print(cast("wishlfihwslwifihl"))

