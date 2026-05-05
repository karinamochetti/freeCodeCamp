import math

def infected(days):
    infected = 1
    for i in range(1, days+1):
        infected *= 2
        if i%3==0:
            infected = math.floor(infected * 0.8)
    return infected


print(infected(1))
print(infected(3))
print(infected(8))
print(infected(17))
print(infected(25))
