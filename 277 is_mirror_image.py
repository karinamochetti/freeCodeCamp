def is_mirror_image(s1, s2):
    MIRROR_CHARS = "WTYUIOHAXVMwoxv08=+:|-_*^!., "
    PAIRS_CHARS = {
        "(":")", ")":"(", 
        "]":"[", "[":"]", 
        "{":"}", "}":"{",
        "<":">", ">":"<",
        "b":"d", "d":"b",
        "q":"p", "p":"q",
        }
    return all(
        (c1 in MIRROR_CHARS and c2 in MIRROR_CHARS and c1 == c2) or (c1 in PAIRS_CHARS and c2 in PAIRS_CHARS and PAIRS_CHARS[c1]==c2)
        for c1, c2 in zip(s1, s2[::-1])
    )

print(is_mirror_image("[HOW]", "[WOH]"))
print(is_mirror_image("MOM", "MOM"))
print(is_mirror_image("vow", "wov"))
print(is_mirror_image("TIM", "TIM"))
print(is_mirror_image("{WOW}", "}WOW{"))
print(is_mirror_image("XXVII", "IIV%X"))
print(is_mirror_image("><(((*>", "<*)))><"))
print(is_mirror_image("WTYUIOHAXVMwoxv08=+:|-_*^!.[]{}<>bdpq()", "()pqbd<>{}[].!^*_-|:+=80vxowMVXAHOIUYTW"))
