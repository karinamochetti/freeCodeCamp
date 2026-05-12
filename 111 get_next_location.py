def get_next_location(matrix):

    # find locations
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                one_loc = [i, j]
            if matrix[i][j] == 2:
                two_loc = [i, j]

    i = two_loc[0]-one_loc[0]
    j = two_loc[1]-one_loc[1]
    final_loc = [two_loc[0]+i, two_loc[1]+j]
    if final_loc[0] < 0 or final_loc[0] >= n:
        final_loc[0] -= 2*i
    if final_loc[1] < 0 or final_loc[1] >= m:
        final_loc[1] -= 2*j

    return final_loc

print(get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]))
print(get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]))
print(get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]))
print(get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]))
print(get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]))