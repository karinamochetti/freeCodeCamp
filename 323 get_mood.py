def get_mood(genre, bpm):
    MOOD = {
        "classical": {109: "focus", 180: "happy"},
        "pop": {180: "happy"},
        "electronic": {89: "focus", 134: "happy", 180: "hype"},
        "rock": {129: "happy", 180: "hype"},
    }
    for b in MOOD[genre]:
        if bpm <= b: return MOOD[genre][b]

print(get_mood("rock", 111))
print(get_mood("electronic", 74))
print(get_mood("classical", 180))
print(get_mood("rock", 155))
print(get_mood("electronic", 90))
print(get_mood("classical", 67))
print(get_mood("pop", 100))
print(get_mood("electronic", 135))

