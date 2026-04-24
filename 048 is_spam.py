def is_spam(number):
    numbers = number.split()

    if len(numbers[0][1:]) > 2 or numbers[0][1] != '0':
        return True

    if int(numbers[1][1:-1]) < 200 or int(numbers[1][1:-1]) > 900:
        return True

    sum_dig = str(int(numbers[2][0])+int(numbers[2][1])+int(numbers[2][2]))
    if sum_dig in numbers[2][4:]:
        return True

    digits = [char for char in number if char.isdigit()]
    count = 1
    for prev_digit, digit in zip(digits[:-1], digits[1:]):
        if prev_digit == digit:
            count += 1
        else:
            count = 1
        if count >= 4:
            return True

    return False

print(is_spam("+0 (200) 234-0182"))
print(is_spam("+091 (555) 309-1922"))
print(is_spam("+1 (555) 435-4792"))
print(is_spam("+0 (955) 234-4364"))
print(is_spam("+0 (155) 131-6943"))
print(is_spam("+0 (555) 135-0192"))
print(is_spam("+0 (555) 564-1987"))
print(is_spam("+00 (555) 234-0182"))
