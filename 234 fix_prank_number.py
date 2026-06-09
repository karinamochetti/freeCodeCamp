from collections import Counter

def fix_prank_number(arr):

    diff_arr = [a2-a1 for a1, a2 in zip(arr[:-1], arr[1:])]
    diff = Counter(diff_arr).most_common(1)[0][0]

    if diff_arr[0] != diff and diff_arr[1] == diff:
        start = arr[1]-diff
    else:
        start = arr[0]

    return [start + i * diff for i in range(len(arr))]

print(fix_prank_number([2, 4, 7, 8, 10]))
print(fix_prank_number([10, 10, 8, 7, 6]))
print(fix_prank_number([12, 24, 36, 48, 61, 72, 84, 96]))
print(fix_prank_number([4, 1, -2, -5, -8, -5]))
print(fix_prank_number([0, 100, 200, 300, 150, 500]))
print(fix_prank_number([400, 425, 400, 375, 350, 325, 300]))
print(fix_prank_number([-5, 5, 10, 15, 20]))