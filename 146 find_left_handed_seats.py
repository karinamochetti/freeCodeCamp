def find_left_handed_seats(table):
    available_top = [
        seat 
        for i, seat in enumerate(table[0]) 
        if seat=="U" and (i == len(table[0])-1 or table[0][i+1] != "R")
    ]
    available_bottom = [
        seat 
        for i, seat in enumerate(table[1]) 
        if seat=="U" and (i == 0 or table[1][i-1] != "R")
    ]
    return len(available_top) + len(available_bottom)

print(find_left_handed_seats([["U", "R", "U", "L"], ["U", "R", "R", "R"]]))
print(find_left_handed_seats([["U", "U", "U", "U"], ["U", "U", "U", "U"]]))
print(find_left_handed_seats([["U", "R", "U", "R"], ["L", "R", "R", "U"]]))
print(find_left_handed_seats([["L", "U", "R", "R"], ["L", "U", "R", "R"]]))
print(find_left_handed_seats([["U", "R", "U", "U"], ["U", "U", "L", "U"]]))
