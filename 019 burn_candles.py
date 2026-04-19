import math

def burn_candles(candles, leftovers_needed):
    return candles + math.ceil(candles/(leftovers_needed-1)) - 1

print(burn_candles(7, 2))
print(burn_candles(10, 5))
print(burn_candles(20, 3))
print(burn_candles(17, 4))
print(burn_candles(2345, 3))
