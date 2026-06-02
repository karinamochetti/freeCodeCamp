def count_letters_and_numbers(s):

    letters = sum(1 if c.isalpha() else 0 for c in s)
    numbers = sum(1 if c.isdigit() else 0 for c in s)

    not1letter = ""
    if letters != 1: not1letter = "s"
    not1number = ""
    if numbers != 1: not1number = "s"

    return f"The string has {letters} letter{not1letter} and {numbers} number{not1number}."

print(count_letters_and_numbers("helloworld123"))
print(count_letters_and_numbers("Catch 22"))
print(count_letters_and_numbers("A1!"))
print(count_letters_and_numbers("12345"))
print(count_letters_and_numbers("password"))
