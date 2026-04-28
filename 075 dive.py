def dive(map, coordinates):
    x, y = coordinates
    if map[x][y] == "-":
        return "Empty"
    else: 
        map[x][y] = "X"
        if any("O" in row for row in map):
            return "Found"
        else: 
            return "Recovered"

print(dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]))
print(dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0]))
print(dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]))
print(dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2]))
print(dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]))
print(dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2]))
