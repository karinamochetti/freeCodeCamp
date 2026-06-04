def card_values(cards):
    values = []
    for card in cards:
        number = card[:-1]
        if number.isalpha():
            if number == "A": values.append(1)
            else: values.append(10)
        else: values.append(int(number))
    return values

print(card_values(["3H", "4D", "5S"]))
print(card_values(["AS", "10S", "10H", "6D", "7D"]))
print(card_values(["8D", "QS", "2H", "JC", "9C"]))
print(card_values(["AS", "KS"]))
print(card_values(["10H", "JH", "QH", "KH", "AH"]))
