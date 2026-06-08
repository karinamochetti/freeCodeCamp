def truncate_text(s):

    def lenght(c):
        if c in "ilI.": return 1
        if c in "fjrt ": return 2
        if c in "abcdeghkmnopqrstuvwxyzJL": return 3
        if c in "ABCDEFGHKMNOPQRSTUVWXYZ": return 4
        return 0

    width = 0
    for i, c in enumerate(s):
        c = s[i]
        width += lenght(c)
        if width == 47 and i != len(s)-1:
            return s[:i+1] + "..."
        if width > 47:
            return s[:i] + "..."
    return s

print(truncate_text("The quick brown fox"))
print(truncate_text("The silky smooth sloth"))
print(truncate_text("THE LOUD BRIGHT BIRD"))
print(truncate_text("The fast striped zebra"))
print(truncate_text("The big black bear"))
