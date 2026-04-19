def get_laptop_cost(laptops, budget):
    laptops.sort()
    max_laptops = laptops[-2]
    laptops = [laptop for laptop in laptops if laptop <= budget]
    if max_laptops <= budget: return max_laptops
    elif laptops: return laptops[-1]
    else: return 0


print(get_laptop_cost([1500, 2000, 1800, 1400], 1900))
print(get_laptop_cost([1500, 2000, 2000, 1800, 1400], 1900))
print(get_laptop_cost([2099, 1599, 1899, 1499], 2200))
print(get_laptop_cost([2099, 1599, 1899, 1499], 1000))
print(get_laptop_cost([1200, 1500, 1600, 1800, 1400, 2000], 1450))
