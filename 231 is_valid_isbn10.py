def is_valid_isbn10(s):
    s = s.replace("-", "")

    if len(s) != 10:
        return False

    i = s.find("X")
    if i != -1 and i != 9:
        return False

    values = [int(c) if c.isdigit() else 10 for c in s]
    if sum((i+1)*v for i, v in enumerate(values))%11 != 0:
        return False

    return True

print(is_valid_isbn10("0-306-40615-2"))
print(is_valid_isbn10("0-306-40615-1"))
print(is_valid_isbn10("0-8044-2957-X"))
print(is_valid_isbn10("X-306-40615-2"))
print(is_valid_isbn10("0-6822-2589-4"))
