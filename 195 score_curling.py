def score_curling(house):

    def dist2x2(i, j):
        if i==2 and j==2:
            return 0
        if abs(2-i) <= 1 and abs(2-j) <= 1:
            return 1
        return 2 

    ring0 = []
    ring1 = []
    ring2 = []

    for i in range(5):
        for j in range(5):
            if house[i][j] != ".":
                if dist2x2(i, j) == 0:
                    ring0.append(house[i][j])
                if dist2x2(i, j) == 1:
                    ring1.append(house[i][j])
                if dist2x2(i, j) == 2:
                    ring2.append(house[i][j])

    winner = None
    if len(set(ring0)) == 1:
        winner = ring0[0]
        points = 1
    
    if len(set(ring1)) == 2:
        if winner == None:
            return "No points awarded"
        else:
            return f"{winner}: {points}"
    if len(set(ring1)) == 1:
        if winner == None:
            winner = ring1[0]
            points = ring1.count(winner)
        elif winner == ring1[0]:
            points += ring1.count(winner)
        else:
            return f"{winner}: {points}"

        if len(set(ring2)) == 2:
            if winner == None:
                return "No points awarded"
            else:
                return f"{winner}: {points}"
        elif len(set(ring2)) == 1:
            if winner == None:
                winner = ring2[0]
                points = ring2.count(winner)
            elif winner == ring2[0]:
                points += ring2.count(winner)
            else:
                return f"{winner}: {points}"

    return "No points awarded"


print(score_curling([[".", ".", "R", ".", "."], [".", "R", ".", ".", "."], ["Y", ".", ".", ".", "."], [".", "R", ".", ".", "."], [".", ".", ".", ".", "."]]))
print(score_curling([[".", ".", "R", ".", "."], [".", ".", ".", ".", "."], [".", ".", "Y", ".", "R"], [".", ".", "Y", "Y", "."], [".", "Y", "R", "R", "."]]))
print(score_curling([[".", "R", "Y", ".", "."], ["Y", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", "Y", "R", "Y", "."], [".", ".", "R", "R", "."]]))
print(score_curling([[".", "Y", "Y", ".", "."], ["Y", ".", ".", "R", "."], [".", ".", "R", ".", "."], [".", ".", "R", "R", "."], [".", "Y", "R", "Y", "."]]))
print(score_curling([["Y", "Y", "Y", "Y", "Y"], ["Y", "R", "R", "R", "Y"], ["Y", "R", "Y", "R", "Y"], ["Y", "R", "R", "R", "Y"], ["Y", "Y", "Y", "Y", "Y"]]))
print(score_curling([["Y", "R", "Y", "R", "Y"], ["R", ".", ".", ".", "R"], ["Y", ".", ".", ".", "Y"], ["R", ".", ".", ".", "R"], ["Y", ".", ".", "R", "Y"]]))

