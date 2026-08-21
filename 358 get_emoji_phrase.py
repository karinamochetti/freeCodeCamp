def get_emoji_phrase(s):
    EMOJI = {
        "👶": "baby",
        "🐱": "cat",
        "🐕": "dog",
        "🐟": "fish",
        "🥵": "hot",
        "🧊": "ice",
        "🪨": "rock",
        "🦈": "shark",
        "🍲": "soup",
        "⭐": "star",
    }
    return " ".join([EMOJI[e] for e in s])

print(get_emoji_phrase("🪨⭐"))
print(get_emoji_phrase("🥵🐕"))
print(get_emoji_phrase("👶🦈"))
print(get_emoji_phrase("⭐🐟"))
print(get_emoji_phrase("🧊🧊👶"))
print(get_emoji_phrase("🐱🐟🍲"))
