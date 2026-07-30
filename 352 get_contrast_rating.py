def get_contrast_rating(ratio, is_large_text):
    ratio = float(ratio)

    if not is_large_text: 
        if ratio >= 7: return "AAA"
        elif ratio >= 4.5: return "AA"
        else: return "Fail"

    if is_large_text: 
        if ratio >= 4.5: return "AAA"
        elif ratio >= 3.0: return "AA"
        else: return "Fail"


print(get_contrast_rating("7.5", False))
print(get_contrast_rating("4.8", False))
print(get_contrast_rating("4.2", False))
print(get_contrast_rating("4.5", True))
print(get_contrast_rating("3.0", True))
print(get_contrast_rating("2.7", False))
