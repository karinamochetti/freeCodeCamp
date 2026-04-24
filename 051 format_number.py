def format_number(number):
    return f"+{number[0]} ({number[1:4]}) {number[4:7]}-{number[7:]}"

print(format_number("05552340182"))
print(format_number("15554354792"))