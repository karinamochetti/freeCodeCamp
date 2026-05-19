def string_sum(s):
    digits = [c if c.isdigit() else " " for c in s ]
    numbers = ("".join(digits)).split()
    return sum(int(number) for number in numbers)

print(string_sum("3apples2bananas"))
print(string_sum("10cats5dogs2birds"))
print(string_sum("125344"))
print(string_sum("a1b20c300"))
print(string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5"))
