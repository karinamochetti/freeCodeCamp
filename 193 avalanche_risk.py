def avalanche_risk(snow_depth, slope):
    if snow_depth != "Shallow" and slope != "Gentle":
        return "Risky"
    return "Safe"

print(avalanche_risk("Shallow", "Gentle"))
print(avalanche_risk("Shallow", "Steep"))
print(avalanche_risk("Shallow", "Very Steep"))
print(avalanche_risk("Moderate", "Gentle"))
print(avalanche_risk("Moderate", "Steep"))
print(avalanche_risk("Moderate", "Very Steep"))
print(avalanche_risk("Deep", "Gentle"))
print(avalanche_risk("Deep", "Steep"))
print(avalanche_risk("Deep", "Very Steep"))
