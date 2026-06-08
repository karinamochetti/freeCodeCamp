def get_captured_value(pieces):
    total_points = 8*1 + 2*5 + 2*3 + 2*3 + 1*9 + 1*0
    value = {
        "P": 1,
        "R": 5,
        "N": 3,
        "B": 3,
        "Q": 9,
        "K": 0,
    }
    if "K" not in pieces:
        return "Checkmate"
    for piece in pieces:
        total_points -= value[piece]
    return total_points

print(get_captured_value(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"]))
print(get_captured_value(["P", "P", "P", "P", "P", "R", "B", "K"]))
print(get_captured_value(["K", "P", "P", "N", "P", "P", "R", "P", "B", "P", "N", "B"]))
print(get_captured_value(["P", "Q", "N", "P", "P", "B", "K", "P", "R", "R", "P", "P", "B", "P"]))
print(get_captured_value(["P", "K"]))
print(get_captured_value(["N", "P", "P", "B", "K", "P", "Q", "N", "P", "P", "R", "R", "P", "P", "P", "B"]))
print(get_captured_value(["N", "P", "P", "B", "P", "R", "Q", "P", "P", "P", "B"]))
