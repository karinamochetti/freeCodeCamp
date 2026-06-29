def connect_three(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    def checkTrio(r, c):
        checks = [
            [(0, -2), (0, -1), (0, 0)],
            [(0, -1), (0, 0), (0, 1)],
            [(0, 0), (0, 1), (0, 2)],

            [(-2, 0), (-1, 0), (0, 0)],
            [(-1, 0), (0, 0), (1, 0)],
            [(0, 0), (1, 0), (2, 0)],

            [(0, 0), (1, 1), (2, 2)],
            [(-1, -1), (0, 0), (1, 1)],
            [(-2, -2), (-1, -1), (0, 0)],

            [(0, 0), (-1, 1), (-2, 2)],
            [(-1, 1), (0, 0), (1, -1)],
            [(2, -2), (-1, 1), (0, 0)],
        ]
        for check in checks:
            if r+min([ch[0] for ch in check]) >= 0 and c+min([ch[1] for ch in check]) >= 0 and r+max([ch[0] for ch in check]) < rows and c+max([ch[1] for ch in check]) < cols:
                if matrix[r+check[0][0]][c+check[0][1]] == matrix[r+check[1][0]][c+check[1][1]] == matrix[r+check[2][0]][c+check[2][1]]:
                    return [[r+check[0][0],c+check[0][1]], [r+check[1][0], c+check[1][1]], [r+check[2][0], c+check[2][1]]]
        return None


    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != "":
                trio = checkTrio(r, c)
                if trio != None: 
                    return [matrix[r][c]] + trio
    return []

print(connect_three([["", "", "", ""], ["", "", "", ""], ["", "Y", "", ""], ["Y", "R", "R", "R"]]))
print(connect_three([["", "", "", ""], ["", "Y", "Y", ""], ["", "Y", "R", "R"], ["", "Y", "R", "R"]]))
print(connect_three([["", "", "Y", "R"], ["", "Y", "R", "Y"], ["", "R", "Y", "R"], ["", "R", "Y", "R"]]))
print(connect_three([["", "Y", "", ""], ["", "Y", "Y", ""], ["", "R", "R", "Y"], ["R", "R", "Y", "R"]]))
print(connect_three([["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"], ["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"]]))
