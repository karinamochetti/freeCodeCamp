def horoscope_match(sign1, sign2):
    SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    DISTANCE = {
        0: "100%",
        1: "40%",
        2: "80%",
        3: "30%",
        4: "90%",
        5: "20%",
        6: "50%",
    }
    idx = abs(SIGNS.index(sign1) - SIGNS.index(sign2))
    return DISTANCE[idx] if idx <= 6 else DISTANCE[12-idx]

print(horoscope_match("Libra", "Sagittarius"))
print(horoscope_match("Gemini", "Scorpio"))
print(horoscope_match("Pisces", "Aries") )
print(horoscope_match("Capricorn", "Cancer"))
print(horoscope_match("Aquarius", "Aquarius"))
print(horoscope_match("Virgo", "Taurus"))
print(horoscope_match("Leo", "Scorpio"))
