def buy_items(funds, items):
    rate = {
        "USD": 1,
        "EUR": 1.1,
        "GBP": 1.25,
        "JPY": 0.007,
        "CAD": 0.75,
    }

    value = float(funds[0])
    if funds[1] != "USD":
        value = value*rate[funds[1]]
    num = 0
    for price, curr in items:
        price = float(price)
        price = price*rate[curr]
        if value - price >= 0:
            value -= price
            num += 1
        else:
            break;
    if num == len(items):
        return "Buy them all!"
    if num > 0:
        return f"Buy the first {num} items."
    return "Not enough money"

print(buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]))
print(buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]))
print(buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]))
print(buy_items(["5000", "JPY"], [["3.00", "USD"], ["1000", "JPY"], ["5.00", "CAD"], ["2.00", "EUR"], ["4.00", "USD"], ["2000", "JPY"]]))
print(buy_items(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]]))
