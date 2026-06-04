def is_valid_domino_chain(dominoes):
    for p1, p2 in zip(dominoes[:-1], dominoes[1:]):
        if p1[1] != p2[0]:
            return False
    return True


print(is_valid_domino_chain([[1, 3], [3, 6], [6, 5]]) )
print(is_valid_domino_chain([[6, 2], [3, 4], [4, 1]]))
print(is_valid_domino_chain([[2, 5], [5, 6], [5, 1]]))
print(is_valid_domino_chain([[4, 3], [3, 1], [1, 6], [6, 6], [6, 5], [5, 1], [1, 1], [1, 4], [4, 4], [4, 2]]))
print(is_valid_domino_chain([[2, 3], [3, 3], [3, 6], [6, 1], [1, 4], [3, 5], [5, 5], [5, 4], [4, 2], [2, 2]]))
