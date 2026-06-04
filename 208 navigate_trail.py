def navigate_trail(map):
    n = len(map)
    m = len(map[0])

    directions = [
        ((0, 1), "R"),
        ((0, -1), "L"),
        ((1, 0), "D"),
        ((-1, 0), "U"),
    ]

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "C":
                pos = [i, j]
    prev = (None, None)
    moves = ""
    pos_x, pos_y = pos

    while map[pos_x][pos_y] != "G":
        prev_x, prev_y = prev
        pos_x, pos_y = pos
        for (i, j), move in directions:
            new = (pos_x+i, pos_y+j)
            new_x, new_y = new
            if 0 <= new_x < n and 0 <= new_y < m:
                if new != prev and map[new_x][new_y] in ["T", "G"]:
                    moves += move
                    prev = pos
                    pos = new
                    break
        pos_x, pos_y = pos
    return moves


print(navigate_trail(["-CT--", "--T--", "--TT-", "---T-", "---G-"]))
print(navigate_trail(["-----", "--TTG", "--T--", "--T--", "CTT--"]))
print(navigate_trail(["-C----", "TT----", "T-----", "TTTTT-", "----G-"]))
print(navigate_trail(["--------", "-CTTT---", "----T---", "---GT---", "--------"]))
print(navigate_trail(["TTTTTTT-", "T-----T-", "T-----T-", "TTTT--TG", "---C----"]))
