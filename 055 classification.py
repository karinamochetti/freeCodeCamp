def classification(temp):
    if temp >= 30000: return "O"
    if temp >= 10000: return "B"
    if temp >= 7500: return "A"
    if temp >= 6000: return "F"
    if temp >= 5200: return "G"
    if temp >= 3700: return "K"
    if temp >= 0: return "M"

print(classification(5778))
print(classification(2400))
print(classification(9999))
print(classification(3700))
print(classification(3699))
print(classification(210000))
print(classification(6000))
print(classification(11432))
