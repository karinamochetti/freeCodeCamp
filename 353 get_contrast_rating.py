def get_contrast_rating(l1, l2, is_large_text):
    wcag = (l1 + 0.05)/(l2 + 0.05)

    if is_large_text:
        if wcag >= 4.5: return "AAA"
        elif wcag >= 3.0: return "AA"
        else: return "Fail"

    if not is_large_text:
        if wcag >= 7.0: return "AAA"
        elif wcag >= 4.5: return "AA"
        else: return "Fail"

print(get_contrast_rating(1.0, 0.0, False))
print(get_contrast_rating(0.9015, 0.1364, False))
print(get_contrast_rating(0.8965, 0.1628, False))
print(get_contrast_rating(0.7469, 0.0957, True))
print(get_contrast_rating(0.7489, 0.2018, True))
print(get_contrast_rating(0.6571, 0.1974, True))
