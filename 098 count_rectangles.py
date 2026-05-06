def count_rectangles(width, height):
    total = 0
    for i in range(1, width+1):
        for j in range(1, height+1):
            total += (width-i+1)*(height-j+1)
    return total

print(count_rectangles(1, 3))
print(count_rectangles(3, 2))
print(count_rectangles(1, 2))
print(count_rectangles(5, 4))
print(count_rectangles(11, 19))
