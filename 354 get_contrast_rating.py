def get_contrast_rating(rgb1, rgb2, is_large_text):
    chan1 = [
        (c/255) /12.92 if c/255 <= 0.04045 
        else (((c/255)+0.055)/1.055)**2.4
        for c in rgb1
    ]

    chan2 = [
        (c/255) /12.92 if c/255 <= 0.04045 
        else (((c/255)+0.055)/1.055)**2.4
        for c in rgb2
    ]

    lum1 = 0.2126*chan1[0] + 0.7152*chan1[1] + 0.0722*chan1[2]
    lum2 = 0.2126*chan2[0] + 0.7152*chan2[1] + 0.0722*chan2[2]

    wcag = (lum1+0.05)/(lum2+0.05)

    if not is_large_text:
        if wcag >= 7.0: return "AAA"
        elif wcag >= 4.5: return "AA"
        else: return "Fail"

    if is_large_text:
        if wcag >= 4.5: return "AAA"
        elif wcag >= 3.0: return "AA"
        else: return "Fail"

print(get_contrast_rating([255, 255, 255], [0, 0, 0], False))
print(get_contrast_rating([215, 188, 188], [55, 55, 55], False))
print(get_contrast_rating([143, 144, 210], [46, 47, 61], False))
print(get_contrast_rating([167, 167, 210], [53, 10, 53], True))
print(get_contrast_rating([135, 147, 155], [60, 70, 90], True))
print(get_contrast_rating([125, 210, 195], [105, 130, 90], True))
