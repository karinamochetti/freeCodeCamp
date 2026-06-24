def is_valid_isbn_13(s):
    VALID_CHAR = "0123456789-"
    if any(c not in VALID_CHAR for c in s):
        return False
    s = s.replace("-", "")
    if len(s) != 13:
        return False
    if sum(int(c) * (3 if idx % 2 != 0 else 1) for idx, c in enumerate(s))%10 != 0:
        return False
    return True

print(is_valid_isbn_13("9780306406157"))
print(is_valid_isbn_13("97803064061570"))
print(is_valid_isbn_13("978-0-13-595705-9"))
print(is_valid_isbn_13("978-030-64061A-4"))
print(is_valid_isbn_13("9-7-8-0-1-3-4-7-5-7-5-9-9"))
