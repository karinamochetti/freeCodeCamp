def golf_score(par, strokes):
    if strokes == 1: return "Hole in one!"
    if strokes+2 == par: return "Eagle"
    if strokes+1 == par: return "Birdie"
    if strokes == par: return "Par"
    if strokes == par+1: return "Bogey"
    if strokes == par+2: return "Double bogey"

print(golf_score(3, 3))
print(golf_score(4, 3))
print(golf_score(3, 1))
print(golf_score(5, 7))
print(golf_score(4, 5))
print(golf_score(5, 3))
