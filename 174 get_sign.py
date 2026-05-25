def get_sign(date_str): 
	zodiac = { 
		1: [20, "Capricorn", "Aquarius"], 
		2: [19, "Aquarius", "Pisces"], 
		3: [21, "Pisces", "Aries"], 
		4: [20, "Aries", "Taurus"], 
		5: [21, "Taurus", "Gemini"], 
		6: [21, "Gemini", "Cancer"], 
		7: [23, "Cancer", "Leo"], 
		8: [23, "Leo", "Virgo"], 
		9: [23, "Virgo", "Libra"], 
		10: [23, "Libra", "Scorpio"], 
		11: [22, "Scorpio", "Sagittarius"], 
		12: [22, "Sagittarius", "Capricorn"], 
	} 

	month = int(date_str[5:7])
	day = int(date_str[8:10])
	cutoff_day, early_sign, late_sign = zodiac[month]

	return early_sign if day < cutoff_day else late_sign 

print(get_sign("2026-01-31"))
print(get_sign("2001-06-10"))
print(get_sign("1985-09-07"))
print(get_sign("2023-03-19"))
print(get_sign("2045-11-05"))
print(get_sign("1985-12-06"))
print(get_sign("2025-12-30"))
print(get_sign("2018-10-08"))
print(get_sign("1958-05-04"))
