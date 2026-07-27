def elevator_stops(current_floor, stops):
    downward = [f for f in sorted(stops) if f <= current_floor]
    upward = [f for f in sorted(stops) if f > current_floor]

    if current_floor - min(stops) < max(stops) - current_floor:
        return downward[::-1] + upward
    else:
        return upward + downward[::-1]

print(elevator_stops(5, [2, 8, 3, 9]))
print(elevator_stops(6, [2, 10, 8, 3, 1, 9]))
print(elevator_stops(1, [4, 8, 3, 6, 9]))
print(elevator_stops(12, [6, 10, 7, 3, 1, 4]))
print(elevator_stops(11, [2, 8, 23, 5, 12, 10, 6, 9, 19]))
