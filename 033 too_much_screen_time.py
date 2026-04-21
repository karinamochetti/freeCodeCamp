def too_much_screen_time(hours):
    over_10 = len([x for x in hours if x >= 10]) > 0
    over_8 = len([i for i in range(len(hours)-2) if sum(hours[i:i+3])/3 >= 8]) > 0
    over_6 = sum(hours)/len(hours) >= 6
    return over_10 or over_8 or over_6

print(too_much_screen_time([1, 2, 3, 4, 5, 6, 7]))
print(too_much_screen_time([7, 8, 8, 4, 2, 2, 3]))
print(too_much_screen_time([5, 6, 6, 6, 6, 6, 6]))
print(too_much_screen_time([1, 2, 3, 11, 1, 3, 4]))
print(too_much_screen_time([1, 2, 3, 10, 2, 1, 0]))
print(too_much_screen_time([3, 3, 5, 8, 8, 9, 4]))
print(too_much_screen_time([3, 9, 4, 8, 5, 7, 6]))
