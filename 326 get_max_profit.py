def get_max_profit(prices, budget):
    buy, sell = 1, 1
    for i in range(len(prices)):
        for j in range(i,len(prices)):
            p1, p2 = prices[i], prices[j]
            if p2-p1 > sell-buy:
                buy, sell = p1, p2
    return f"{(budget//buy)*(sell-buy):.2f}"



print(get_max_profit([5, 6], 50))
print(get_max_profit([8, 2, 5, 10], 20))
print(get_max_profit([4, 5, 3, 6], 20))
print(get_max_profit([54.40, 51.22, 53.99, 50.28, 53.01, 52.84], 200))
print(get_max_profit([15.38, 15.01, 14.99, 14.62, 14.28], 80))
print(get_max_profit([121.45, 126.82, 122.91, 124.65, 128.83, 128.83, 127.33], 1230.25))
