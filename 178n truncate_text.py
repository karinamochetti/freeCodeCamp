def truncate_text(text):
    if len(text) <= 20: 
        return text
    else:
        return text[:17] + "..."

print(truncate_text("Hello, world!"))
print(truncate_text("This string should get truncated."))
print(truncate_text("Exactly twenty chars"))
print(truncate_text("....................."))
